import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="EcoScan AI | Gemini 3", page_icon="🌱")
st.title("🌱 EcoScan AI")
st.write("Powered by the world's most intelligent multimodal model: **Gemini 3 Pro**")

api_key = st.text_input("Enter Gemini API Key:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # Using the exact string from your documentation
        model = genai.GenerativeModel('gemini-3-pro-preview')

        uploaded_file = st.file_uploader("Upload an item to scan...", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Analyzing with Gemini 3 Pro...', use_container_width=True)
            
            if st.button("Start Environmental Reasoning"):
                with st.spinner('Gemini 3 is thinking (State-of-the-art Reasoning)...'):
                    # Prompting for agentic reasoning as per Gemini 3's strengths
                    prompt = "Analyze this image. Identify materials, recycling instructions, and explain the environmental impact logic."
                    
                    response = model.generate_content([prompt, image])
                    st.success("Analysis Complete!")
                    st.markdown(response.text)
                    
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Please enter your API Key to enable Gemini 3 features.")