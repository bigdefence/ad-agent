# Cosmetic Ad Agent

This agent generates professional cosmetic advertisement images using the `gemini-3-pro-image-preview` model.

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **API Key**:
    Set your Google Cloud API key in a `.env` file or as an environment variable:
    ```
    GOOGLE_API_KEY=your_api_key_here
    ```

## Usage

Run the script with the path to your product image:

```bash
python main.py --image path/to/your/product.jpg
```

## Output

The script will generate two images in the current directory:
1.  `output_product_ad.png`: A high-end ad focusing solely on the product.
2.  `output_model_ad.png`: An ad featuring a realistic model holding the product.
