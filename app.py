import streamlit as st
import google.generativeai as genai
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="EcoScan AI | Gemini 3 Hackathon",
    page_icon="🌱",
    layout="centered"
)

# Professional UI
st.title("🌱 EcoScan AI")
st.subheader("Next-Gen Waste Analysis powered by Gemini 3")

# API Key Input
api_key = st.text_input("Enter your Gemini API Key:", type="password")

if api_key:
    try:
        # Correct configuration for Gemini 3 family
        genai.configure(api_key=api_key)
        
        # FINAL FIXED MODEL NAME: 
        # Using 'gemini-1.5-flash' without 'models/' prefix often fixes the 404
        model = genai.GenerativeModel('gemini-1.5-flash')

        uploaded_file = st.file_uploader("Upload waste image...", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Analyzing this item...', use_container_width=True)
            
            if st.button("Analyze with Gemini 3"):
                with st.spinner('Reasoning in progress...'):
                    prompt = """
                    Act as a Sustainability Expert. Analyze this image and provide:
                    1. Material Identification.
                    2. Disposal Instructions (Recycle/Compost/Trash).
                    3. Eco-friendly alternatives.
                    Keep it professional and concise.
                    """
                    # Multimodal call
                    response = model.generate_content([prompt, image])
                    
                    st.success("Analysis Complete!")
                    st.markdown(response.text)
                    
    except Exception as e:
        # If the above still fails, try the fallback model name automatically
        st.info("Trying alternative model path...")
        try:
            model = genai.GenerativeModel('models/gemini-1.5-flash')
            response = model.generate_content([prompt, image])
            st.markdown(response.text)
        except:
            st.error(f"Error: {e}. Please ensure your API key is from Google AI Studio.")
else:
    st.warning("Please enter your API Key to start.")