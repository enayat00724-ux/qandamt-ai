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

st.sidebar.header("تنظیمات")
api_key = st.sidebar.text_input("API Key را وارد کنید:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # تست کردن مدل‌های مختلف برای جلوگیری از ارور 404
        try:
            model = genai.GenerativeModel('gemini-1.5-flash-latest')
        except:
            model = genai.GenerativeModel('gemini-pro-vision')
        
        uploaded_file = st.file_uploader("چارت را آپلود کنید:", type=['png', 'jpg', 'jpeg'])

        if uploaded_file:
            image = Image.open(uploaded_file)
            st.image(image, caption='چارت شما', use_container_width=True)
            
            if st.button("🚀 شروع تحلیل کالبدشکافی QANDAMT"):
                with st.spinner("در حال تحلیل..."):
                    prompt = "تحلیل دقیق چارت طبق استراتژی QANDAMT 4.0 شامل روند، منشا حرکت و سیگنال ورود و خروج به زبان فارسی."
                    # متد تولید محتوا مخصوص تصاویر
                    response = model.generate_content([prompt, image])
                    st.divider()
                    st.markdown(response.text)
    except Exception as e:
        st.error(f"خطا در مدل: {e}\nلطفاً دوباره تلاش کنید.")
else:
    st.info("👈 کلید API را در سمت چپ وارد کنید.")
