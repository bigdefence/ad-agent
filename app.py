from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
import io
import base64

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Gemini
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

def generate_concept_prompt(image, target, channel, styles):
    """Generates a detailed prompt for the image generator using a text model."""
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    style_str = ", ".join(styles)
    
    prompt = f"""
    You are a creative director for a high-end cosmetic brand.
    Analyze the provided product image.
    Create a detailed image generation prompt for an advertisement based on the following constraints:
    
    - **Target Audience**: {target}
    - **Channel**: {channel}
    - **Style/Mood**: {style_str}
    
    **CRITICAL INSTRUCTIONS**:
    1. The goal is to use this prompt to edit the background and props while KEEPING THE PRODUCT AND LOGO EXACTLY AS IS.
    2. Describe a scene that fits the style and channel.
    3. Lighting should be flattering for cosmetics.
    4. Output ONLY the prompt text, no other conversational text.
    """
    
    response = model.generate_content([prompt, image])
    return response.text

def generate_ad_image(image, prompt, target_audience, is_model_focus=False):
    """Generates the final ad image using the image preview model."""
    model = genai.GenerativeModel('gemini-3-pro-image-preview')
    
    final_prompt = prompt
    if is_model_focus:
        final_prompt += f" The image MUST be a high-quality upper body portrait of a realistic human model ({target_audience}) HOLDING the product. The model should be holding the product up, potentially near their face or chest, ensuring the product is the focal point while the model's face is also clearly visible and engaging. The pose should be natural, elegant, and professional, typical of high-end beauty campaigns. The lighting should be soft and flattering, highlighting both the model's skin texture and the product details."
    else:
        final_prompt += " Focus solely on the product. The product should be the hero of the image, placed on an elegant surface or background."
        
    final_prompt += " CRITICAL: The product in the image MUST be identical to the product in the input image. Do not change the product's shape, color, logo, or text. The product must be the exact same item, just placed in a new environment/context. If the product has text on it, it must remain legible and unchanged."

    try:
        response = model.generate_content([final_prompt, image])
        
        if response.parts:
            for part in response.parts:
                if part.inline_data:
                    return Image.open(io.BytesIO(part.inline_data.data))
        return None
    except Exception as e:
        print(f"Error generating image: {e}")
        return None

def image_to_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    
    file = request.files['image']
    target = request.form.get('target')
    channel = request.form.get('channel')
    styles = request.form.getlist('styles') # Expecting multiple values if possible, or comma separated
    
    # If styles come as a single string from form, split it
    if len(styles) == 1 and ',' in styles[0]:
        styles = [s.strip() for s in styles[0].split(',')]

    if not file or not target or not styles:
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        image = Image.open(file.stream)
        
        # 1. Generate Concept
        concept_prompt = generate_concept_prompt(image, target, channel, styles)
        
        # 2. Generate Images
        img_product = generate_ad_image(image, concept_prompt, target, is_model_focus=False)
        img_model = generate_ad_image(image, concept_prompt, target, is_model_focus=True)
        
        response_data = {
            'concept': concept_prompt,
            'product_ad': image_to_base64(img_product) if img_product else None,
            'model_ad': image_to_base64(img_model) if img_model else None
        }
        
        return jsonify(response_data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
