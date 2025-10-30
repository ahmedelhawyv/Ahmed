<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>أداة فحص الروابط والإيميلات - Cyber Check</title>
  <link rel="stylesheet" href="styles.css" />
</head>
<body>

  <header>
    <h1>🛡️ Cyber Check</h1>
    <p>أداة ذكية لفحص الروابط والإيميلات وكشف التهديدات</p>
  </header>

  <main>
    <div class="container">
      <div class="tabs">
        <button id="emailTab" class="tab">تحليل إيميل</button>
        <button id="urlTab" class="tab active">فحص رابط</button>
      </div>

      <div id="urlChecker" class="content active">
        <label>ضع الرابط لفحصه:</label>
        <input type="text" id="urlInput" placeholder="https://example.com" />
        <label>دومين متوقّع (اختياري):</label>
        <input type="text" id="domainInput" placeholder="google.com" />
        <button onclick="checkURL()">تحليل الرابط 🔍</button>
        <pre id="urlResult"></pre>
      </div>

      <div id="emailAnalyzer" class="content">
        <label>الصق محتوى البريد الإلكتروني هنا:</label>
        <textarea id="emailContent" placeholder="أدخل نص أو HTML الإيميل..."></textarea>
        <button onclick="analyzeEmail()">تحليل الإيميل 📧</button>
        <pre id="emailResult"></pre>
      </div>
    </div>
  </main>

  <footer>
    <p>© 2025 - مشروع الأمن السيبراني | <strong>Cyber Check</strong></p>
  </footer>

  <script>
    // Tabs control
    const emailTab = document.getElementById('emailTab');
    const urlTab = document.getElementById('urlTab');
    const emailSection = document.getElementById('emailAnalyzer');
    const urlSection = document.getElementById('urlChecker');

    emailTab.onclick = () => {
      emailTab.classList.add('active');
      urlTab.classList.remove('active');
      emailSection.classList.add('active');
      urlSection.classList.remove('active');
    };

    urlTab.onclick = () => {
      urlTab.classList.add('active');
      emailTab.classList.remove('active');
      urlSection.classList.add('active');
      emailSection.classList.remove('active');
    };

    function checkURL() {
      const url = document.getElementById('urlInput').value.trim();
      const domain = document.getElementById('domainInput').value.trim().toLowerCase();
      const resultBox = document.getElementById('urlResult');

      if (!url) {
        resultBox.textContent = "⚠️ من فضلك أدخل رابط.";
        return;
      }

      let issues = [];
      if (url.includes('@')) issues.push("يحتوي على @ (محاولة إخفاء وجهة الرابط)");
      if (url.split('.').length < 2) issues.push("بنية الرابط غير صحيحة");
      if (url.startsWith("http://")) issues.push("يستخدم HTTP وليس HTTPS");
      if (domain && !url.includes(domain)) issues.push(`لا يحتوي على الدومين المتوقع (${domain})`);

      resultBox.innerHTML =
        issues.length === 0
          ? "✅ الرابط آمن مبدئيًا."
          : "⚠️ تحذير! المشاكل المكتشفة:\n- " + issues.join("\n- ");
    }

    function analyzeEmail() {
      const content = document.getElementById('emailContent').value.trim();
      const resultBox = document.getElementById('emailResult');

      if (!content) {
        resultBox.textContent = "⚠️ من فضلك أدخل نص البريد الإلكتروني.";
        return;
      }

      let issues = [];
      if (content.includes("http://")) issues.push("روابط غير آمنة (HTTP)");
      if (content.match(/(free|win|click here|urgent)/gi)) issues.push("كلمات مريبة (free, win, urgent, click here)");
      if (content.includes("@")) issues.push("قد يحتوي على إيميل مريب أو مزيف");

      resultBox.innerHTML =
        issues.length === 0
          ? "✅ لا توجد علامات مريبة في البريد."
          : "⚠️ تحذير! تم اكتشاف:\n- " + issues.join("\n- ");
    }
  </script>
</body>
</html>
