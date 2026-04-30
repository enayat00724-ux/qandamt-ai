import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="QANDAMT AI Analyzer", layout="wide")

# استایل ظاهری
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { background-color: #f0a500; color: black; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("📈 QANDAMT 4.0 AI Web-App")

api_key = st.sidebar.text_input("Enter your API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    # مدل قدرتمندتر را انتخاب می‌کنیم
    model = genai.GenerativeModel('gemini-1.5-flash')

    uploaded_file = st.file_uploader("چارت را اینجا آپلود کن...", type=['png', 'jpg', 'jpeg'])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption='چارت آپلود شده', use_column_width=True)
        
        if st.button("شروع تحلیل حرفه‌ای"):
            with st.spinner("در حال کالبدشکافی چارت طبق استراتژی QANDAMT..."):
                # دستورالعمل فوق دقیق برای هوش مصنوعی
                prompt = """
                تو یک تحلیلگر ارشد ترید هستی. این چارت را دقیقاً طبق استراتژی QANDAMT 4.0 تحلیل کن:
                1. شناسایی جهت اصلی مارکت (Trend).
                2. پیدا کردن منشاهای حرکت در 8 تا 10 کندل آخر.
                3. بررسی ترمزهای قیمتی و نواحی نقدینگی.
                4. در نهایت خروجی را به این شکل بده:
                   - جهت: (خرید/فروش)
                   - نقطه ورود (Entry):
                   - حد ضرر (Stop Loss):
                   - حد سود (Take Profit):
                تحلیل را به زبان فارسی و بسیار دقیق ارائه بده.
                """
                response = model.generate_content([prompt, image])
                st.success("تحلیل آماده شد:")
                st.markdown(response.text)
else:
    st.warning("لطفاً ابتدا API Key را در منوی سمت چپ وارد کنید تا سیستم فعال شود.")
