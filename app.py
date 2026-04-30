import streamlit as st
import streamlit.components.v1 as components

# تنظیمات صفحه
st.set_page_config(page_title="QANDAMT 4.0 Dashboard", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stAlert { border-radius: 10px; background-color: #1a1c24; color: white; border: 1px solid #f0a500; }
    h1, h2 { color: #f0a500; }
    </style>
    """, unsafe_allow_html=True)

st.title("📈 QANDAMT 4.0 AI Dashboard")
st.subheader("دستیار هوشمند ترید - نسخه دستی (بدون ارور)")

col1, col2 = st.columns([1, 1])

with col1:
    st.header("۱. دستورالعمل QANDAMT")
    st.markdown("""
    <div style="background-color: #1a1c24; padding: 20px; border-radius: 10px; border: 1px solid #333;">
        <p style="color: #ccc; font-weight: bold; font-size: 1.1em;">
        متن زیر را کپی کن و در کادر چت جمنای (سمت راست) Paste کن. سپس عکست را در آنجا آپلود کن:
        </p>
        <textarea style="width: 100%; height: 250px; background-color: #0e1117; color: #00ff00; border: 1px solid #f0a500; padding: 10px; border-radius: 5px;">
سلام جمنای! لطفاً این چارت را دقیقاً طبق استراتژی QANDAMT 4.0 تحلیل کن:
1. جهت اصلی مارکت (Trend) را مشخص کن.
2. منشاهای حرکت (Origin of Move) را در 8 تا 10 کندل آخر پیدا کن.
3. ترمزهای قیمتی و نواحی نقدینگی را بررسی کن.
4. در نهایت یک سیگنال دقیق به این صورت بده:
   - جهت: (خرید/فروش)
   - نقطه ورود (Entry):
   - حد ضرر (Stop Loss):
   - حد سود (Take Profit):
تحلیل را به زبان فارسی و با لحن حرفه‌ای بنویس.
        </textarea>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.header("۲. جمنای چت")
    st.warning("⚠️ به دلیل محدودیت‌های گوگل در کشور شما، آپلود مستقیم عکس در اینجا غیرفعال شده است. لطفاً از کادر چت زیر استفاده کنید.")
    
    # باز کردن چت جمنای در یک فریم داخلی
    components.iframe("https://gemini.google.com/app", height=600, scrolling=True)

