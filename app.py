import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="EcoScan AI", page_icon="🌱")
st.title("🌱 EcoScan AI")

api_key = st.text_input("Enter Gemini API Key:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # Using Gemini 3 Flash for better quota and speed
        # This model is designed to scale and is part of the Gemini 3 family
        model = genai.GenerativeModel('gemini-3-flash')

        uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Item for Analysis', use_container_width=True)
            
            if st.button("Run AI Scan"):
                with st.spinner('Gemini 3 Flash is processing...'):
                    prompt = "Analyze this image. Identify materials and give recycling steps."
                    response = model.generate_content([prompt, image])
                    st.success("Analysis Complete!")
                    st.write(response.text)
                    
    except Exception as e:
        # Fallback to Gemini 2.5 Flash if 3 Flash is also busy
        st.info("Switching to high-availability model...")
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content([prompt, image])
        st.write(response.text)
else:
    st.info("Enter API Key to enable Gemini 3 features.")