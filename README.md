# 個人開発のインフラ構築術｜失敗から学ぶスケーラブル設計 | 口コミ・ランキング・使い方

Affiliate Builder で生成した静的サイトです。サーバー不要・HTML と CSS のみで構成されています。

## 構成
```
index.html          # ページ本体
css/base.css        # 共通スタイル
css/themes/theme07.css   # デザインテーマ
page.json           # ビルダーで再編集するための構成データ（「構成JSONを読み込み」で復元）
render.yaml         # Render Static Site 設定
```

## Render で公開する
1. このフォルダの中身を GitHub リポジトリ直下に push
   ```bash
   git init && git add . && git commit -m "site" && git branch -M main
   git remote add origin https://github.com/<you>/<repo>.git && git push -u origin main
   ```
2. https://dashboard.render.com → New + → **Blueprint** → リポジトリを選択 → Apply
   （または New + → **Static Site** → Publish directory に `.` を指定）
3. `https://affiliate-site.onrender.com` で公開されます。以後 push のたびに自動デプロイ。

Netlify / Vercel / GitHub Pages / Cloudflare Pages でも、ビルドコマンドなし・公開ディレクトリ `.` でそのまま公開できます。

## 再編集
ビルダーの「構成JSONを読み込み」に `page.json` を指定すると、同じ内容をキャンバスに復元できます。
