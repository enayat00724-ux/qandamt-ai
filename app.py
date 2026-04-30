import streamlit as st
import requests
import base64
from PIL import Image
import io

st.set_page_config(page_title="QANDAMT AI Analyzer", layout="wide")

st.title("📈 QANDAMT 4.0 AI Web-App")

# تنظیمات سایدبار
api_key = st.sidebar.text_input("Enter API Key:", type="password")

def analyze_image(api_key, image_bytes):
    # آدرس مستقیم و بدون واسطه گوگل
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    # تبدیل عکس به فرمت قابل فهم برای اینترنت
    encoded_image = base64.b64encode(image_bytes).decode('utf-8')
    
    payload = {
        "contents": [{
            "parts": [
                {"text": "Analyze this trading chart based on QANDAMT 4.0 strategy. Identify Trend, Origin of Move, SL, and TP in Persian language."},
                {"inline_data": {"mime_type": "image/jpeg", "data": encoded_image}}
            ]
        }]
    }
    
    response = requests.post(url, json=payload)
    return response.json()

if api_key:
    uploaded_file = st.file_uploader("Upload Chart:", type=['png', 'jpg', 'jpeg'])

    if uploaded_file:
        image_bytes = uploaded_file.read()
        st.image(image_bytes, caption='Chart Loaded', use_container_width=True)
        
        if st.button("🚀 Start QANDAMT Analysis"):
            with st.spinner("Connecting directly to Google AI..."):
                try:
                    result = analyze_image(api_key, image_bytes)
                    # استخراج متن پاسخ از دیتای خام گوگل
                    answer = result['candidates'][0]['content']['parts'][0]['text']
                    st.success("تحلیل آماده شد:")
                    st.markdown(answer)
                except Exception as e:
                    st.error("خطا در پاسخ گوگل. احتمالاً کلید API اشتباه است یا محدودیت دارد.")
                    st.write(result) # برای عیب‌یابی دقیق‌تر
else:
    st.info("👈 Please enter your API Key in the sidebar.")
