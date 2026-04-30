import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="QANDAMT AI PRO", layout="wide")
st.title("📈 QANDAMT 4.0 AI - Multi-Model Version")

api_key = st.sidebar.text_input("Enter API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    
    # لیستی از مدل‌ها به ترتیب اولویت برای تست
    model_names = [
        'gemini-1.5-flash', 
        'gemini-1.5-flash-latest', 
        'gemini-1.0-pro-vision-latest'
    ]
    
    uploaded_file = st.file_uploader("Upload Chart:", type=['png', 'jpg', 'jpeg'])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, use_container_width=True)
        
        if st.button("🚀 شروع تحلیل ترکیبی"):
            success = False
            for m_name in model_names:
                try:
                    st.write(f"تلاش با مدل: {m_name}...")
                    model = genai.GenerativeModel(m_name)
                    prompt = "تحلیل چارت طبق استراتژی QANDAMT 4.0 به زبان فارسی."
                    response = model.generate_content([prompt, image])
                    
                    st.success(f"✅ تحلیل با مدل {m_name} انجام شد:")
                    st.markdown(response.text)
                    success = True
                    break # اگر یکی جواب داد، بقیه را چک نکن
                except Exception as e:
                    if "404" in str(e):
                        st.warning(f"مدل {m_name} در دسترس نبود (404).")
                    else:
                        st.error(f"خطای دیگر در {m_name}: {e}")
            
            if not success:
                st.error("❌ متاسفانه تمام مدل‌های گوگل ارور 404 دادند. این یعنی API Key شما اجازه دسترسی به بخش 'تصویر' را ندارد.")
else:
    st.info("👈 کلید API را وارد کنید.")
