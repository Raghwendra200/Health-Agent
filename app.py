import streamlit as st
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai
import os

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyD9poEyC5txhBbSYABuFVbS-dzdr7mzE_Y"))

# Function to load Google Gemini Pro Vision API and get response
def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{
            "mime_type": uploaded_file.type,
            "data": bytes_data
        }]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit app configuration
st.set_page_config(page_title="Gemini Health App", page_icon="🍏", layout="wide")

# Custom Styles for the page to look like a website with darker color scheme
st.markdown("""
    <style>
    .stApp {
        background-color: #121212; /* Dark background color */
        color: #E0E0E0; /* Light gray text color */
        font-family: 'Arial', sans-serif;
    }
    .stTitle {
        font-size: 2.5em;
        color: #FFD700; /* Gold color for title */
        font-weight: bold;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.7);
    }
    .stHeader {
        font-size: 2em;
        color: #FFD700; /* Gold color for header */
        font-weight: bold;
    }
    .stButton>button {
        background-color: #4CAF50; /* Green button */
        color: white;
        font-size: 18px;
        padding: 15px;
        border-radius: 10px;
        border: none;
        width: 300px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #45a049; /* Darker green on hover */
    }
    .stTextInput>input {
        padding: 10px;
        border-radius: 10px;
        border: 2px solid #4CAF50;
        font-size: 16px;
        width: 100%;
        background-color: #2E2E2E; /* Dark input background */
        color: #E0E0E0; /* Light text color */
    }
    .stFileUploader {
        padding: 10px;
        border-radius: 10px;
        background-color: rgba(255, 255, 255, 0.2); /* Semi-transparent white for uploader */
    }
    .stTextArea>textarea {
        font-size: 16px;
        color: #E0E0E0;
        background-color: #2E2E2E; /* Dark text area */
    }
    .stMarkdown {
        color: #E0E0E0;
        font-size: 18px;
        line-height: 1.6;
    }
    footer {
        background-color: #333; /* Dark footer background */
        color: #E0E0E0;
        text-align: center;
        padding: 20px;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Title and Header
st.markdown('<h1 class="stTitle">Gemini Health App 🍏</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="stHeader">AI-Powered Nutrition Analysis</h2>', unsafe_allow_html=True)

# Instructions
st.markdown("""
    <p class="stMarkdown">
        Upload a picture of your food and let our AI nutrition expert analyze the calories and details of each food item in the image.
        You can also ask specific questions about the food items, and we will generate detailed insights.
    </p>
""", unsafe_allow_html=True)

# Input field for text prompt
input = st.text_input("Enter your prompt to analyze the image:", key="input", placeholder="Describe the image...")

# File uploader for image
uploaded_file = st.file_uploader("Upload an image of food items", type=["jpg", "jpeg", "png"])

# Image preview (if uploaded)
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Submit button
submit = st.button("Analyze the Food and Calculate Calories")

# Define the prompt for the nutrition analysis
input_prompt = """
You are an expert nutritionist. Analyze the food items in the image and calculate the total calories.
Provide details of each food item and its calorie intake in the following format:

1. Item 1 - x calories
2. Item 2 - y calories
...
"""

# If submit button is clicked, process the image and get response
if submit:
    if uploaded_file is not None and input:
        try:
            # Prepare the image data
            image_data = input_image_setup(uploaded_file)
            # Get the Gemini response based on the input prompt and image
            response = get_gemini_response(input, image_data, input_prompt)
            
            # Display response
            st.subheader("Results: Total Calorie Count and Details")
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please upload an image and enter a prompt before submitting.")

# Add Footer (Optional)
st.markdown("""
    <footer>
        <p>&copy; 2025 Gemini Health App | Developed by Your Name</p>
    </footer>
""", unsafe_allow_html=True)
