from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>個人開発のインフラ構築術｜失敗から学ぶスケーラブル設計</title>

<style>
/* =====================================================================
   base.css — 共通スタイル
   ===================================================================== */
:root {
  --ab-primary: #2563eb;
  --ab-primary-dark: #1d4ed8;
  --ab-accent: #f59e0b;
  --ab-bg: #ffffff;
  --ab-surface: #f8fafc;
  --ab-text: #1f2937;
  --ab-muted: #6b7280;
  --ab-border: #e5e7eb;
  --ab-radius: 12px;
  --ab-shadow: 0 4px 16px rgba(0,0,0,.06);
  --ab-font: "Hiragino Sans", "Hiragino Kaku Gothic ProN", "Noto Sans JP", Meiryo, system-ui, sans-serif;
  --ab-heading-font: var(--ab-font);
  --ab-hero-bg: linear-gradient(135deg, var(--ab-primary), var(--ab-primary-dark));
  --ab-hero-text: #ffffff;
  --ab-cta-bg: var(--ab-accent);
  --ab-cta-text: #ffffff;
  --ab-max-width: 920px;
}

*, *::before, *::after { box-sizing: border-box; }
body { margin: 0; font-family: var(--ab-font); color: var(--ab-text); background: var(--ab-bg); line-height: 1.8; }
img { max-width: 100%; height: auto; display: block; }
a { color: var(--ab-primary); }

/* ---------- 書き出しページ共通 ---------- */
.ab-canvas { max-width: var(--ab-max-width); margin: 0 auto; padding: 0 16px 64px; }
.ab-block { margin: 28px 0; }
.ab-card { background: var(--ab-surface); border: 1px solid var(--ab-border); border-radius: var(--ab-radius); padding: 22px 24px; box-shadow: var(--ab-shadow); }
.ab-muted { color: var(--ab-muted); }

/* review */
.ab-review { border-left: 5px solid var(--ab-accent); }
.ab-review .ab-stars { color: var(--ab-accent); letter-spacing: 2px; margin-bottom: 8px; }
.ab-review .ab-author { display: flex; align-items: center; gap: 10px; margin-top: 14px; }
.ab-avatar { width: 40px; height: 40px; border-radius: 50%; background: var(--ab-primary); color: #fff; display: grid; place-items: center; font-weight: 700; }

/* ranking */
.ab-grid { display: grid; gap: 16px; }
.ab-grid-3 { grid-template-columns: repeat(3, 1fr); }
@media (max-width: 720px) { .ab-grid-3 { grid-template-columns: 1fr; } }
.ab-rank-no { width: 56px; height: 56px; border-radius: 50%; display: grid; place-items: center; font-weight: 800; font-size: 1.3rem; }
.gold { background: #d4a017; color: #fff; }
.silver { background: #9ca3af; color: #fff; }
.bronze { background: #b45309; color: #fff; }

/* table */
.ab-table { width: 100%; border-collapse: collapse; }
.ab-table th, .ab-table td { border: 1px solid var(--ab-border); padding: 10px 12px; }
.ab-table th { background: var(--ab-surface); }

/* CTA */
.ab-cta { text-align: center; padding: 40px 24px; background: var(--ab-surface); border-radius: var(--ab-radius); border: 1px solid var(--ab-border); }
.ab-btn { display: inline-block; background: var(--ab-primary); color: #fff; padding: 14px 32px; border-radius: 999px; text-decoration: none; }

/* disclaimer */
.ab-disclaimer { font-size: .78rem; color: var(--ab-muted); background: var(--ab-surface); padding: 12px 16px; border-radius: 8px; }

/* =====================================================================
   theme07 — ダークテーマ
   ===================================================================== */
body.theme07 {
  --ab-primary: #60a5fa;
  --ab-primary-dark: #3b82f6;
  --ab-accent: #fbbf24;
  --ab-bg: #0f172a;
  --ab-surface: #1e293b;
  --ab-text: #e2e8f0;
  --ab-muted: #94a3b8;
  --ab-border: #334155;
  --ab-radius: 10px;
  --ab-hero-bg: linear-gradient(135deg, #60a5fa, #3b82f6);
  --ab-cta-bg: #fbbf24;
}

/* ★ 広告画像を確実に中央寄せ */
.ad-center img {
  display: block;
  margin: 0 auto;
}
</style>

</head>
<body class="theme07">
<main class="ab-canvas">

<header class="ab-block ab-center">
  <h1>個人開発のインフラ構築術｜失敗から学ぶスケーラブル設計</h1>
</header>

<section class="ab-block ab-card ab-review">
  <h2>口コミレビュー</h2>
  <div class="ab-stars">★★★★★</div>
  <div class="content">
    「XServer」を使う前は、インフラ選定に時間がかかっていました。バックアップや設定ミスで予期せぬ費用が増えた経験から、安定した環境の重要性を実感しました。
  </div>
  <div class="ab-author">
    <div class="ab-avatar">個</div>
    <span class="ab-muted">個人開発者：クラウド料金や設定の複雑さに悩んでいました。</span>
  </div>
</section>

<section class="ab-block ab-card">
  <h2>失敗しない使い方</h2>
  <div class="content">
    1. 維持費の透明性が大事です。<br>
    2. 自動化・バックアップを重視しましょう。<br>
    3. 長期運用の予算管理を考慮しましょう。
  </div>
</section>

<section class="ab-block ab-card ab-latent">
  <h2>まだ気づいていない、本当の悩み</h2>
  <div class="content">
    WebアプリやAPIサーバーを高速かつ安定して動作させるには、次世代の超速サーバー環境が必要です。
  </div>
</section>

<section class="ab-block ab-grid ab-grid-3">
  <div class="ab-card ab-center">
    <div class="ab-rank-no gold">1</div>
    <h3>XServer</h3>
    <p>第5世代 AMD EPYC × オールNVMe</p>
  </div>
  <div class="ab-card ab-center">
    <div class="ab-rank-no silver">2</div>
    <h3>ConoHa WING</h3>
    <p>WordPress特化</p>
  </div>
  <div class="ab-card ab-center">
    <div class="ab-rank-no bronze">3</div>
    <h3>mixhost</h3>
    <p>WordPress特化</p>
  </div>
</section>

<section class="ab-block ab-card">
  <h2>価格比較</h2>
  <table class="ab-table">
    <thead>
      <tr><th>項目</th><th>XServer</th><th>ConoHa WING</th><th>mixhost</th></tr>
    </thead>
    <tbody>
      <tr><td>価格</td><td>693円/月～</td><td>937円/月～</td><td>650円/月～</td></tr>
      <tr><td>容量</td><td>500GB</td><td>500GB</td><td>500GB</td></tr>
      <tr><td>転送量</td><td>無制限</td><td>無制限</td><td>無制限</td></tr>
      <tr><td>独自ドメイン</td><td>無料</td><td>無料</td><td>無料</td></tr>
    </tbody>
  </table>
</section>

<section class="ab-block ab-cta">
  <h2>XServerの公式サイトはこちら</h2>
  <p>今ならキャンペーン実施中</p>

  <div class="ad-center">
    <a href="https://px.a8.net/svt/ejp?a8mat=4BED93+7AK6K2+CO4+6CHB5" rel="nofollow">
      <img border="0" width="350" height="240" alt=""
           src="https://www20.a8.net/svt/bgt?aid=261010839441&wid=001&eno=01&mid=s00000001642001066000&mc=1">
    </a>
    <img border="0" width="1" height="1"
         src="https://www12.a8.net/0.gif?a8mat=4BED93+7AK6K2+CO4+6CHB5" alt="">
  </div>

  <p class="ab-note">※価格・キャンペーン内容は公式サイトでご確認ください</p>
</section>

<section class="ab-block">
  <p class="ab-disclaimer">
    当サイトはアフィリエイトプログラムに参加しており、リンクから購入された場合に報酬を受け取ることがあります。
  </p>
</section>

</main>
</body>
</html>
    """
