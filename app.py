import streamlit as st
import google.generativeai as genai
from PIL import Image

# Page Setup
st.set_page_config(page_title="EcoScan AI", page_icon="🌱")
st.title("🌱 EcoScan AI")

# API Key Input
api_key = st.text_input("Enter Gemini API Key:", type="password")

if api_key:
    try:
        # Standard configuration
        genai.configure(api_key=api_key)
        
        # Try the most stable naming convention for 1.5 Flash (Gemini 3 family)
        # We use 'gemini-1.5-flash' which is the standard identifier
        model = genai.GenerativeModel(model_name='gemini-1.5-flash')

        uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Item to analyze', use_container_width=True)
            
            if st.button("Analyze Environmental Impact"):
                with st.spinner('Gemini 3 is thinking...'):
                    # Professional prompt to leverage Gemini 3's reasoning
                    prompt = "Analyze this image for recycling. Identify the material, give disposal steps, and suggest a green alternative."
                    
                    # Generate content
                    response = model.generate_content([prompt, image])
                    
                    st.success("Analysis Complete!")
                    st.write(response.text)
                    
    except Exception as e:
        # If still 404, the API might be forcing the 'models/' prefix
        st.warning("Retrying with alternative path...")
        try:
            model = genai.GenerativeModel(model_name='models/gemini-1.5-flash')
            response = model.generate_content([prompt, image])
            st.write(response.text)
        except Exception as final_error:
            st.error(f"Technical Error: {final_error}")
            st.info("Check if your API Key is active in Google AI Studio.")
else:
    st.info("Please enter your API Key from Google AI Studio to start.")