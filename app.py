import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="EcoScan AI", page_icon="🌱")
st.title("🌱 EcoScan AI")

api_key = st.text_input("Enter Gemini API Key:", type="password")

if api_key:
    try:
        # Explicitly setting the API to v1beta for Gemini 3 family models
        genai.configure(api_key=api_key)
        
        # Try a more direct way to call the model
        model = genai.GenerativeModel('gemini-1.5-pro')

        uploaded_file = st.file_uploader("Upload waste image...", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Analyzing...', use_container_width=True)
            
            if st.button("Analyze Now"):
                with st.spinner('Gemini 3 is reasoning...'):
                    # Prompt for Gemini 3's reasoning capabilities
                    prompt = "Identify the material in this image, provide recycling steps, and an eco-friendly alternative."
                    
                    # Force multimodal generation
                    response = model.generate_content([prompt, image])
                    
                    st.success("Analysis Complete!")
                    st.write(response.text)
                    
    except Exception as e:
        st.error(f"Error: {e}")
        st.info("Try using 'gemini-1.5-pro' if flash persists in error.")
else:
    st.warning("Please enter your API Key from Google AI Studio.")