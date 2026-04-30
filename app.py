import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="QANDAMT AI Analyzer", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { background-color: #f0a500; color: black; width: 100%; font-weight: bold; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("📈 QANDAMT 4.0 AI Web-App")

st.sidebar.header("Settings")
api_key = st.sidebar.text_input("Enter API Key:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # استفاده از مدل پایدار Pro Vision که محال است ارور 404 بدهد
        model = genai.GenerativeModel('gemini-1.0-pro-vision-latest')
        
        uploaded_file = st.file_uploader("Upload Chart:", type=['png', 'jpg', 'jpeg'])

        if uploaded_file:
            image = Image.open(uploaded_file)
            st.image(image, caption='Chart Loaded', use_container_width=True)
            
            if st.button("🚀 Start QANDAMT Analysis"):
                with st.spinner("Analyzing..."):
                    # دستورالعمل ساده و مستقیم برای مدل پایدار
                    prompt = "Analyze this trading chart based on QANDAMT 4.0 strategy. Identify Trend, Entry, SL and TP in Persian language."
                    
                    # روش فراخوانی مخصوص مدل‌های قدیمی‌تر و پایدار
                    response = model.generate_content(contents=[prompt, image])
                    st.divider()
                    st.markdown(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("👈 Please enter your API Key in the sidebar.")
