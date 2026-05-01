<script>
    // ⚠️ کلید خودت را اینجا وارد کن
    const GEMINI_API_KEY = 'AIzaSyBwjprg28__18g5MFEeMmwwhQJb_yI7UC4'; 

    let lang='en', step=1, market=null, asset=null, assetDir=null, c1=null, c2=null, tf='5M', free=7;

    // ... (آبجکت T برای ترجمه‌ها همان قبلی بماند) ...

    async function fetchSuggestions(m) {
        const t = T[lang];
        document.getElementById('sugLoad').classList.add('show');
        document.getElementById('sugContent').style.display = 'none';
        
        // پاک کردن ویجت‌های قبلی برای جلوگیری از تکرار
        const oldWidget = document.getElementById('live-widget-container');
        if(oldWidget) oldWidget.remove();

        // ایجاد ویجت زنده بر اساس بازار انتخاب شده
        let widgetHtml = '<div id="live-widget-container" style="margin-bottom:20px;">';
        if (m === 'crypto') {
            widgetHtml += `<iframe src="https://cryptobubbles.net/" style="width:100%; height:450px; border:2px solid #222; border-radius:15px;"></iframe>`;
        } else if (m === 'forex') {
            widgetHtml += `<iframe src="https://www.tradingview.com/embed-widget/heatmap/?colorTheme=dark" style="width:100%; height:450px; border:2px solid #222; border-radius:15px;"></iframe>`;
        } else if (m === 'gold') {
            widgetHtml += `<iframe src="https://www.tradingview.com/widgetembed/?symbol=OANDA%3AXAUUSD&interval=H&theme=dark" style="width:100%; height:450px; border:2px solid #222; border-radius:15px;"></iframe>`;
        }
        widgetHtml += '</div>';

        const prompts = {
            crypto: `Check current top crypto gainers/losers. Identify the strongest coin (1H volume/price) for BUY and the weakest for SELL. Return JSON ONLY: {"buy":{"symbol":"BTC","reason":"..."},"sell":{"symbol":"SOL","reason":"..."}}`,
            forex: `Check FX heatmap for strongest/weakest pairs. Return JSON ONLY: {"buy":{"symbol":"GBPUSD","reason":"..."},"sell":{"symbol":"USDJPY","reason":"..."}}`,
            gold: `Analyze gold (XAUUSD) current intraday sentiment. Return JSON ONLY: {"buy":{"symbol":"XAUUSD","reason":"..."},"sell":{"symbol":"XAUUSD","reason":"..."}}`
        };

        try {
            // فراخوانی مستقیم API جمنای برای پیدا کردن بهترین ارز
            const r = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${GEMINI_API_KEY}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ contents: [{ parts: [{ text: prompts[m] }] }] })
            });
            const d = await r.json();
            let txt = d.candidates[0].content.parts[0].text.replace(/```json|```/g, '').trim();
            const data = JSON.parse(txt);

            document.getElementById('sugLoad').classList.remove('show');
            const content = document.getElementById('sugContent');
            content.style.display = 'block';
            content.insertAdjacentHTML('afterbegin', widgetHtml); // نمایش هیت‌مپ زنده بالای پیشنهادها
            
            showSuggestions(data);
        } catch (e) {
            console.error("API Error:", e);
            // لود کردن ویجت حتی اگر API خطا داد
            document.getElementById('sugLoad').classList.remove('show');
            document.getElementById('sugContent').style.display = 'block';
            document.getElementById('sugContent').insertAdjacentHTML('afterbegin', widgetHtml);
        }
    }

    async function runAnalysis() {
        if(!c1 || !c2) return;
        goStep(4);
        document.getElementById('anaLoad').classList.add('show');
        
        const b1 = await b64(c1);
        const b2 = await b64(c2);
        
        const prompt = `Analyze these 2 charts using QANDAMT 4.0 strategy (Tayane). 
        Asset: ${asset} | Market: ${market}
        Chart 1 (1H): Find trend, DNA Range, and Power Candles.
        Chart 2 (${tf}): Find exact entry, SL, and TP. 
        Follow QANDAMT rules for R:R (1:1 for range, 1:3 for trend).
        Response language: ${lang === 'fa' ? 'Persian' : 'English'}`;

        try {
            const r = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${GEMINI_API_KEY}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    contents: [{
                        parts: [
                            {inline_data: {mime_type: c1.type, data: b1}},
                            {inline_data: {mime_type: c2.type, data: b2}},
                            {text: prompt}
                        ]
                    }]
                })
            });
            const d = await r.json();
            const resTxt = d.candidates[0].content.parts[0].text;
            
            document.getElementById('anaLoad').classList.remove('show');
            document.getElementById('resBox').classList.add('show');
            document.getElementById('resTxt').textContent = resTxt;
            // استخراج اعداد سیگنال با Regex (اختیاری برای نمایش در کادرهای پایین)
        } catch (err) {
            document.getElementById('anaLoad').textContent = "Error: " + err.message;
        }
    }

    // سایر توابع کمکی (goStep, b64, restart, etc.) همان کدهای قبلی هستند
</script>
