# LUMIÈRE AI Studio - AI Cosmetic Ad Generator

**LUMIÈRE AI Studio** is an AI-powered web application designed to generate professional-grade cosmetic advertisements. By analyzing a product image and user-defined constraints, it creates high-quality ad concepts and final visuals using Google's Gemini models.

## 🌟 Features

-   **AI Concept Generation**: Uses `gemini-2.5-flash` to analyze product images and generate detailed, creative ad prompts based on target audience and brand mood.
-   **Dual Ad Generation**:
    -   **Product Focus**: Generates a high-end ad visual where the product is the hero.
    -   **Model Focus**: Generates a realistic lifestyle ad featuring a model matching the target audience.
-   **Powered by Gemini 3**: Utilizes the `gemini-3-pro-image-preview` model for state-of-the-art image generation.
-   **Web Interface**: Easy-to-use Flask web application for uploading images and setting parameters.

## 🛠️ Tech Stack

-   **Python**
-   **Flask** (Web Framework)
-   **Google Gemini API** (`gemini-2.5-flash`, `gemini-3-pro-image-preview`)
-   **Pillow (PIL)** (Image Processing)

## 🚀 Setup

1.  **Clone the repository**:
    ```bash
    git clone [repository-url]
    cd [repository-directory]
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Configuration**:
    Create a `.env` file in the root directory and add your Google Cloud API key:
    ```
    GOOGLE_API_KEY=your_api_key_here
    ```

## 💻 Usage

1.  **Start the Application**:
    ```bash
    python app.py
    ```

2.  **Access the Web Interface**:
    Open your browser and navigate to `http://localhost:5000`.

3.  **Generate Ads**:
    -   **Upload Image**: Select your cosmetic product image.
    -   **Target Audience**: Specify the target demographic (e.g., "20s Female", "Luxury Skincare Users").
    -   **Channel**: Choose the ad platform (e.g., "Instagram").
    -   **Styles**: Select or enter style keywords (e.g., "Minimalist", "Elegant", "Neon").
    -   Click **Generate** to create your ad campaign.

## 📂 Project Structure

-   `app.py`: Main Flask application file containing routes and Gemini API integration logic.
-   `templates/`: HTML templates for the web interface.
-   `requirements.txt`: List of Python dependencies.
