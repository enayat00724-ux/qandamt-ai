import streamlit as st

st.set_page_config(page_title="QANDAMT 4.0 Pro", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; text-align: center; }
    .stButton>button { background-color: #f0a500; color: black; font-weight: bold; padding: 20px; border-radius: 15px; width: 100%; }
    .instruction-box { background-color: #1a1c24; padding: 20px; border-radius: 15px; border: 1px solid #f0a500; margin-bottom: 20px; text-align: right; direction: rtl; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 سیستم تحلیلگر QANDAMT 4.0")
st.write("به دلیل محدودیت‌های API، از روش مستقیم و بدون خطا استفاده می‌کنیم")

# بخش کپی متن
st.markdown('<div class="instruction-box">', unsafe_allow_html=True)
st.markdown("### ۱. کپی کردن دستورالعمل")
prompt = """لطفاً این چارت را طبق استراتژی QANDAMT 4.0 تحلیل کن. 
روند اصلی، منشاهای حرکت (Origin)، ترمزهای قیمت و نقدینگی را مشخص کن. 
در آخر سیگنال ورود (Entry)، حد ضرر (SL) و حد سود (TP) را به فارسی بگو."""

st.code(prompt, language="text")
st.info("متن بالا را کپی کنید")
st.markdown('</div>', unsafe_allow_html=True)

# بخش دکمه ورود
st.markdown('<div class="instruction-box">', unsafe_allow_html=True)
st.markdown("### ۲. آپلود عکس و دریافت تحلیل")
st.write("بعد از کلیک روی دکمه زیر، در صفحه باز شده عکس چارت را آپلود کرده و متنی که کپی کردید را بفرستید.")

# دکمه با لینک مستقیم که در تب جدید باز می‌شود
st.link_button("🔥 ورود به بخش تحلیل و آپلود عکس", "https://gemini.google.com/app")
st.markdown('</div>', unsafe_allow_html=True)

st.warning("نکته: چون مستقیماً از هوش مصنوعی اصلی گوگل استفاده می‌کنید، تحلیل‌ها بسیار دقیق‌تر از قبل خواهد بود.")
