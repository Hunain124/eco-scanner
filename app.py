import streamlit as st
import google.generativeai as genai
from PIL import Image

# Page Configuration for a professional look
st.set_page_config(
    page_title="EcoScan AI | Gemini 3 Hackathon",
    page_icon="🌱",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #2e7d32;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌱 EcoScan AI")
st.subheader("Next-Gen Waste Analysis powered by Gemini 3")
st.write("Upload an image of any household item or waste to get instant recycling guidance and sustainable alternatives.")

# API Key Input
api_key = st.text_input("Enter your Gemini API Key to begin:", type="password", help="Get your key from Google AI Studio")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # Using the latest Gemini 1.5 model (Gemini 3 family base)
        model = genai.GenerativeModel('models/gemini-1.5-flash-latest')

        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Target Item', use_container_width=True)
            
            submit = st.button("Analyze Environmental Impact")

            if submit:
                with st.spinner('Gemini 3 is analyzing the material composition...'):
                    # Professional Prompt for Gemini 3
                    prompt = """
                    You are a professional Sustainability Consultant. Analyze the provided image carefully and provide:
                    1. **Material Identification**: What is this item made of?
                    2. **Disposal Instructions**: Precise steps for recycling, composting, or safe disposal.
                    3. **Sustainability Score**: Rate the item's eco-friendliness from 1-10.
                    4. **Green Alternatives**: Suggest 2-3 eco-friendly alternatives to this product.
                    5. **Did You Know?**: An interesting environmental fact related to this material.
                    
                    Please use clear headings and bullet points. Keep the tone professional and encouraging.
                    """
                    
                    response = model.generate_content([prompt, image])
                    
                    st.success("Analysis Complete!")
                    st.markdown("---")
                    st.markdown(response.text)
                    
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.warning("Please enter your Gemini API Key to enable the AI features.")

# Footer
st.markdown("---")
st.caption("Built with Google Gemini 3 for the Global Hackathon 2026.")