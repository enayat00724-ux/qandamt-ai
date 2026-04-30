import streamlit as st
import google.generativeai as genai
from PIL import Image

# تنظیمات صفحه
st.set_page_config(page_title="QANDAMT AI Analyzer", layout="wide")

# استایل ظاهری برای زیبایی بیشتر
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { background-color: #f0a500; color: black; width: 100%; font-weight: bold; border-radius: 10px; }
    .stAlert { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("📈 QANDAMT 4.0 AI Web-App")
st.subheader("تحلیلگر هوشمند چارت بر اساس استراتژی اختصاصی")

# سایدبار برای تنظیمات
st.sidebar.header("تنظیمات سیستم")
api_key = st.sidebar.text_input("لطفاً API Key خود را وارد کنید:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # استفاده از مدل 1.5-flash با ساختار صحیح برای جلوگیری از ارور NotFound
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        st.success("✅ سیستم با موفقیت به هوش مصنوعی متصل شد.")
        
        uploaded_file = st.file_uploader("یک تصویر از چارت (JPG/PNG) انتخاب کنید:", type=['png', 'jpg', 'jpeg'])

        if uploaded_file:
            image = Image.open(uploaded_file)
            st.image(image, caption='چارت آپلود شده', use_container_width=True)
            
            if st.button("🚀 شروع تحلیل کالبدشکافی QANDAMT"):
                with st.spinner("در حال آنالیز لایه‌های قیمتی..."):
                    prompt = """
                    بعنوان یک تریدر حرفه‌ای مسلط به استراتژی QANDAMT 4.0، این چارت را تحلیل کن:
                    1. روند اصلی (Trend) را مشخص کن.
                    2. منشاهای حرکت (Origin of Move) را در 10 کندل آخر شناسایی کن.
                    3. ترمزهای قیمتی و نواحی نقدینگی را پیدا کن.
                    4. در نهایت یک سیگنال دقیق شامل:
                       - Direction (Buy/Sell)
                       - Entry Price
                       - Stop Loss
                       - Take Profit 1 & 2
                    ارائه بده. پاسخ را به زبان فارسی و با لحن حرفه‌ای بنویس.
                    """
                    # ارسال عکس و متن به مدل
                    response = model.generate_content([prompt, image])
                    
                    st.divider()
                    st.markdown("### 📊 نتیجه تحلیل:")
                    st.markdown(response.text)
    except Exception as e:
        st.error(f"یک خطا رخ داد: {e}")
else:
    st.info("👈 برای شروع، ابتدا کلید API را در منوی سمت چپ وارد کنید.")
    st.warning("اگر کلید ندارید، باید آن را از Google AI Studio دریافت کنید.")
