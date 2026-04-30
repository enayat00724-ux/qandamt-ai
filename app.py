import streamlit as st
import google.generativeai as genai
from PIL import Image

# تنظیمات ظاهر سایت
st.set_page_config(page_title="QANDAMT AI Analyzer", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { background-color: #f0a500; color: black; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("📈 QANDAMT 4.0 AI Web-App")

# تنظیم API Key (بعداً در تنظیمات امنیتی وارد می‌کنیم)
api_key = st.sidebar.text_input("Enter your API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    uploaded_file = st.file_uploader("چارت را اینجا آپلود کن...", type=['png', 'jpg', 'jpeg'])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption='چارت شما', use_column_width=True)
        
        if st.button("شروع آنالیز QANDAMT"):
            with st.spinner("در حال تحلیل..."):
                prompt = "تحلیل بر اساس استراتژی QANDAMT 4.0: جهت مارکت، منشاهای ۸-۱۰ کندل آخر، ترمز قیمتی و نقدینگی را بررسی کن و Entry, SL, TP بده."
                response = model.generate_content([prompt, image])
                st.markdown(response.text)
else:
    st.info("لطفاً کلید API خود را در سمت چپ وارد کنید.")

