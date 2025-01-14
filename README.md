# Gemini Health App 🍏

The **Gemini Health App** is an AI-powered application that allows users to upload food images and analyze their nutritional content. It uses Google Gemini's advanced AI capabilities to generate detailed insights, including calorie counts and food item breakdowns.

## Features

- **Food Image Upload**: Upload images of food items to analyze.
- **Calorie Calculation**: AI calculates the total calories in the uploaded food image and breaks down the nutritional content.
- **Detailed Insights**: The app provides a detailed response for each food item in the image with calorie information.

## Technologies Used

- **Streamlit**: For building and deploying the interactive web app.
- **Google Gemini API**: For analyzing food images and generating nutritional information.
- **Python**: For app logic and API integration.
- **PIL (Pillow)**: For image processing and manipulation.
- **Dotenv**: For managing environment variables securely.

## Setup Instructions

Follow the steps below to run the app locally:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/gemini-health-app.git
cd gemini-health-app

3. Set up environment variables
Create a .env file in the root directory and add your Google API key:

GOOGLE_API_KEY=your_google_api_key_here

 Run the app

 streamlit run app.py

App Features
Input Prompt: Enter a custom prompt to analyze the uploaded food image.
Image Upload: Upload images in .jpg, .jpeg, or .png formats.
Calorie Insights: After submitting, the app will display a detailed list of food items with their respective calorie content. 
