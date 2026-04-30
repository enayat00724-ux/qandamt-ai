import streamlit as st

st.set_page_config(page_title="QANDAMT Professional Terminal", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stTabs [data-baseweb="tab"] { color: white; font-size: 18px; }
    .instruction-box { background-color: #1a1c24; padding: 15px; border-radius: 10px; border: 1px solid #f0a500; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ ترمینال معاملاتی QANDAMT 4.0")

# ایجاد تب‌های مختلف برای ابزارهای متفاوت
tab1, tab2, tab3, tab4 = st.tabs(["🔍 تحلیل هوشمند", "📊 هیت‌مپ و بابلز", "💰 قیمت‌های زنده", "📅 تقویم اقتصادی"])

with tab1:
    col_a, col_b = st.columns([1, 1])
    with col_a:
        st.subheader("۱. کپی دستورالعمل مخصوص")
        option = st.selectbox("نوع دارایی را انتخاب کنید:", ["کریپتو", "طلا (XAUUSD)", "جفت ارز (Forex)"])
        
        if option == "کریپتو":
            prompt = "تحلیل چارت کریپتو بر اساس QANDAMT 4.0: بررسی نقدینگی صرافی‌ها و ساختار بازار."
        elif option == "طلا (XAUUSD)":
            prompt = "تحلیل اختصاصی انس جهانی طلا: بررسی کورولیشن دلار و ترمزهای قیمتی QANDAMT."
        else:
            prompt = "تحلیل جفت ارز: بررسی قدرت ارزها و منشاهای حرکت در تایم‌فریم بالا."
            
        st.code(prompt, language="text")
        st.link_button("🔥 ورود به بخش آپلود عکس در جمنای", "https://gemini.google.com/app")
    
    with col_b:
        st.info("💡 راهنما: ابتدا نوع دارایی را انتخاب، متن را کپی و سپس در جمنای عکس را آپلود کنید.")

with tab2:
    st.subheader("نقشه حرارتی بازار و حباب‌های کریپتو")
    # قرار دادن هیت مپ زنده
    st.components.v1.iframe("https://coin360.com/", height=500)
    st.divider()
    st.components.v1.iframe("https://cryptobubbles.net/", height=500)

with tab3:
    st.subheader("قیمت لحظه‌ای طلا و جفت ارزها")
    # ویجت تریدینگ ویو برای قیمت‌ها
    st.components.v1.html("""
        <div class="tradingview-widget-container">
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-market-overview.js" async>
          {
          "container_id": "tv-medium-widget",
          "symbols": [["Gold", "OANDA:XAUUSD|1D"], ["Bitcoin", "BINANCE:BTCUSDT|1D"], ["Euro/Dollar", "FX:EURUSD|1D"]],
          "width": "100%", "height": "400", "showChart": true, "locale": "fa"
          }
          </script>
        </div>
    """, height=450)

with tab4:
    st.subheader("رویدادهای مهم اقتصادی")
    st.components.v1.iframe("https://sslecal2.forexprostools.com/?columns=exc_flags,exc_currency,exc_importance,exc_actual,exc_forecast,exc_previous&features=datepicker,timezone&countries=1,2,3,4,5,6,7,8,9,10&calType=day&timeZone=55&lang=1", height=500)
