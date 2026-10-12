from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
<html lang="ja" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>電気柵の本体選び｜12kV・1.2J・最大10kmは畑で何を意味するか</title>
<meta name="description" content="足跡を見つけた翌日に止まっている人へ。1万円前後の電気柵本体4機種と国産セット1台を、電源方式・出力・付属品の同じ物差しで並べました。周囲長から総延長を計算する判定ツール付き。">
<meta property="og:title" content="電気柵の本体選び｜12kV・1.2J・最大10kmは畑で何を意味するか">
<meta property="og:description" content="1万円前後の電気柵本体を、電源方式・出力・付属品で横並びに比較。総延長の判定ツールと、レビューで多かった不満の対処つき。">
<meta property="og:type" content="article">
<meta name="theme-color" content="#0e1720">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%230e1720'/%3E%3Cpath d='M3 16h26' stroke='%23e0a800' stroke-width='2'/%3E%3Ccircle cx='16' cy='16' r='4' fill='%23f0bb2a'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Zen+Old+Mincho:wght@500;700&family=Zen+Kaku+Gothic+New:wght@400;500;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
/* =========================================================
   電気柵 本体の選び方 — style.css
   Design tokens / layout / components
   ========================================================= */

/* ---------- 1. Tokens ---------- */
:root {
  /* 亜鉛メッキ・石灰を思わせる冷たい白。クリーム色の定番は避けている */
  --paper:      #eceeea;
  --paper-2:    #e2e6e2;
  --surface:    #f7f8f5;
  --hero-bg:    #0e1720;
  --hero-2:     #14212c;

  --ink:        #141e26;
  --ink-2:      #4b5960;
  --ink-3:      #69757b;
  --on-dark:    #e9eeea;
  --on-dark-2:  #a7b4ba;

  --rule:       #cfd6d2;
  --rule-2:     #b6bfba;

  /* 通電の黄。警告板の色をそのまま持ってきている */
  --volt-fill:  #e9b308;
  --volt-text:  #a97900;
  --live:       #1c7a63;
  --warn:       #9d4429;

  --shadow:     0 1px 0 var(--rule), 0 18px 40px -32px rgba(20, 30, 38, .5);

  --f-disp: "Zen Old Mincho", "Hiragino Mincho ProN", "Yu Mincho", "YuMincho", serif;
  --f-body: "Zen Kaku Gothic New", -apple-system, BlinkMacSystemFont, "Hiragino Kaku Gothic ProN", "Yu Gothic", "Meiryo", sans-serif;
  --f-mono: "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;

  --sheet-max: 1120px;
  --sheet-pad: 32px;
  --rail-w:    104px;
  --rail-gap:  44px;
  --header-h:  60px;

  --radius:    4px;
  --ease:      cubic-bezier(.2, .7, .2, 1);
}

[data-theme="dark"] {
  --paper:      #0e1720;
  --paper-2:    #121c25;
  --surface:    #16222c;
  --hero-bg:    #0a1118;
  --hero-2:     #101b24;

  --ink:        #e9eeea;
  --ink-2:      #a7b4ba;
  --ink-3:      #859298;
  --on-dark:    #e9eeea;
  --on-dark-2:  #a7b4ba;

  --rule:       #25343f;
  --rule-2:     #32434f;

  --volt-text:  #f0bb2a;
  --live:       #4eb99a;
  --warn:       #e08561;

  --shadow:     0 1px 0 var(--rule), 0 18px 40px -30px rgba(0, 0, 0, .8);
}

/* ---------- 2. Base ---------- */
*, *::before, *::after { box-sizing: border-box; }

html {
  -webkit-text-size-adjust: 100%;
  scroll-behavior: smooth;
  scroll-padding-top: calc(var(--header-h) + 16px);
}

body {
  margin: 0;
  background: var(--paper);
  color: var(--ink);
  font-family: var(--f-body);
  font-size: 16.5px;
  line-height: 1.9;
  letter-spacing: .01em;
  font-feature-settings: "palt" 1;
  overflow-x: hidden;
  transition: background-color .3s var(--ease), color .3s var(--ease);
}

h1, h2, h3 { margin: 0; font-weight: 500; line-height: 1.4; text-wrap: balance; }
p { margin: 0; }
ul, ol, dl, dd { margin: 0; padding: 0; }
li { list-style: none; }
img, svg { max-width: 100%; display: block; }
button { font: inherit; color: inherit; background: none; border: 0; cursor: pointer; }
a { color: var(--ink); text-decoration-color: var(--rule-2); text-underline-offset: .22em; }
a:hover { text-decoration-color: var(--volt-text); }

.mono {
  font-family: var(--f-mono);
  font-variant-numeric: tabular-nums;
  letter-spacing: .01em;
}

.sr-only {
  position: absolute; width: 1px; height: 1px;
  padding: 0; margin: -1px; overflow: hidden;
  clip: rect(0 0 0 0); white-space: nowrap; border: 0;
}

.skip {
  position: absolute; left: 16px; top: -64px; z-index: 100;
  background: var(--ink); color: var(--paper);
  padding: 10px 16px; border-radius: var(--radius);
  transition: top .2s var(--ease);
}
.skip:focus { top: 12px; }

:focus-visible {
  outline: 2px solid var(--volt-fill);
  outline-offset: 3px;
  border-radius: 2px;
}

/* ---------- 3. Topbar ---------- */
.topbar {
  position: sticky; top: 0; z-index: 50;
  background: color-mix(in srgb, var(--paper) 88%, transparent);
  backdrop-filter: saturate(1.4) blur(10px);
  border-bottom: 1px solid var(--rule);
}
@supports not (backdrop-filter: blur(2px)) {
  .topbar { background: var(--paper); }
}

.topbar__inner {
  max-width: var(--sheet-max);
  margin: 0 auto;
  padding: 0 var(--sheet-pad);
  height: var(--header-h);
  display: flex; align-items: center; justify-content: space-between; gap: 16px;
}

.brand { display: flex; align-items: center; gap: 10px; text-decoration: none; }
.brand__mark {
  width: 26px; height: 10px; position: relative; flex: none;
  background: linear-gradient(var(--rule-2), var(--rule-2)) center/100% 1px no-repeat;
}
.brand__mark::after {
  content: ""; position: absolute; left: 8px; top: 50%;
  width: 7px; height: 7px; margin-top: -3.5px; border-radius: 50%;
  background: var(--volt-fill);
  box-shadow: 0 0 0 3px color-mix(in srgb, var(--volt-fill) 22%, transparent);
}
.brand__text {
  font-family: var(--f-disp); font-size: .95rem; letter-spacing: .04em;
  white-space: nowrap;
}

.topbar__tools { display: flex; align-items: center; gap: 8px; }

.toc-btn, .theme-btn {
  height: 34px; border: 1px solid var(--rule); border-radius: var(--radius);
  background: var(--surface);
  transition: border-color .2s var(--ease), background-color .2s var(--ease);
}
.toc-btn { padding: 0 14px; font-size: .8rem; letter-spacing: .08em; }
.toc-btn:hover, .theme-btn:hover { border-color: var(--rule-2); }
.toc-btn[aria-expanded="true"] { border-color: var(--volt-text); color: var(--volt-text); }

.theme-btn { width: 34px; display: grid; place-items: center; }
.theme-btn__icon {
  width: 13px; height: 13px; border-radius: 50%;
  border: 1.5px solid var(--ink-2);
  background: linear-gradient(90deg, var(--ink-2) 0 50%, transparent 50% 100%);
}
[data-theme="dark"] .theme-btn__icon {
  border-color: var(--volt-fill);
  background: var(--volt-fill);
  box-shadow: 0 0 0 3px color-mix(in srgb, var(--volt-fill) 20%, transparent);
}

.toc {
  max-width: var(--sheet-max); margin: 0 auto;
  padding: 8px var(--sheet-pad) 20px;
  border-top: 1px dashed var(--rule);
}
.toc ol { display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 2px 28px; }
.toc a {
  display: flex; gap: 10px; align-items: baseline;
  padding: 7px 4px; font-size: .88rem; text-decoration: none;
  border-bottom: 1px solid transparent;
}
.toc a::before {
  content: ""; width: 6px; height: 6px; flex: none; border-radius: 50%;
  border: 1.5px solid var(--rule-2);
}
.toc a:hover { color: var(--volt-text); }
.toc a:hover::before { border-color: var(--volt-fill); background: var(--volt-fill); }
.toc li { counter-increment: toc; }
.toc ol { counter-reset: toc; }
.toc a::after {
  content: counter(toc, decimal-leading-zero);
  margin-left: auto; font-family: var(--f-mono); font-size: .7rem; color: var(--ink-3);
}

.progress { height: 2px; background: transparent; }
.progress__bar {
  display: block; height: 100%; width: 0;
  background: var(--volt-fill);
  transition: width .1s linear;
}

/* ---------- 4. Hero ---------- */
.hero {
  position: relative;
  background: var(--hero-bg);
  color: var(--on-dark);
  padding: clamp(48px, 8vw, 104px) 0 0;
  overflow: hidden;
}
.hero::before {
  content: "";
  position: absolute; inset: 0;
  background:
    radial-gradient(120% 80% at 82% 8%, rgba(233,179,8,.13), transparent 58%),
    radial-gradient(90% 60% at 6% 100%, rgba(255,255,255,.05), transparent 60%);
  pointer-events: none;
}
.hero__grid {
  position: relative;
  max-width: var(--sheet-max); margin: 0 auto;
  padding: 0 var(--sheet-pad) clamp(40px, 6vw, 76px);
  display: grid; grid-template-columns: minmax(0, 1.15fr) minmax(300px, .85fr);
  gap: clamp(28px, 5vw, 64px); align-items: center;
}

.hero__eyebrow {
  font-family: var(--f-mono); font-size: .72rem; letter-spacing: .18em;
  color: var(--volt-fill); margin-bottom: 22px;
}
.hero__title {
  font-family: var(--f-disp); font-weight: 500;
  font-size: clamp(2.1rem, 6.2vw, 4.1rem);
  line-height: 1.06; letter-spacing: -0.015em;
  display: flex; flex-wrap: wrap; align-items: baseline; gap: 0 .18em;
}
.hero__num { white-space: nowrap; }
.hero__dot { color: var(--volt-fill); }
.hero__sub {
  margin-top: 18px;
  font-family: var(--f-disp); font-size: clamp(1rem, 2.1vw, 1.3rem);
  line-height: 1.7; color: var(--on-dark);
}
.hero__lead {
  margin-top: 20px; max-width: 40em; color: var(--on-dark-2);
  font-size: .95rem; line-height: 1.95;
}
.hero__cta { margin-top: 30px; display: flex; flex-wrap: wrap; gap: 12px; }

.btn {
  display: inline-flex; align-items: center; gap: 9px;
  height: 46px; padding: 0 22px; border-radius: var(--radius);
  font-size: .9rem; letter-spacing: .04em; text-decoration: none;
  transition: transform .18s var(--ease), background-color .18s var(--ease), border-color .18s var(--ease);
}
.btn:hover { transform: translateY(-1px); }
.btn--volt { background: var(--volt-fill); color: #141e26; font-weight: 500; }
.btn--volt:hover { background: #f3c62c; }
.btn--ghost { border: 1px solid rgba(233,238,234,.32); color: var(--on-dark); }
.btn--ghost:hover { border-color: var(--volt-fill); color: var(--volt-fill); }

/* instrument panel */
.panel {
  background: linear-gradient(180deg, var(--hero-2), rgba(20, 33, 44, .55));
  border: 1px solid rgba(233, 238, 234, .14);
  border-radius: 6px;
  padding: 22px 22px 20px;
}
.panel__head {
  display: flex; align-items: center; justify-content: space-between;
  padding-bottom: 16px;
}
.panel__label { font-family: var(--f-mono); font-size: .68rem; letter-spacing: .2em; color: var(--on-dark-2); }
.panel__state {
  display: inline-flex; align-items: center; gap: 8px;
  font-family: var(--f-mono); font-size: .72rem; color: var(--volt-fill);
}
.lamp {
  width: 8px; height: 8px; border-radius: 50%; background: var(--volt-fill);
  animation: blink 1.2s steps(1, end) infinite;
}
@keyframes blink { 0%, 62% { opacity: 1; } 63%, 100% { opacity: .22; } }

/* the wire: signature element */
.wire { position: relative; height: 54px; margin: 2px 0 18px; }
.wire__line {
  position: absolute; left: 0; right: 0; top: 50%; height: 1px;
  background: linear-gradient(90deg, rgba(233,238,234,.16), rgba(233,238,234,.5) 20%, rgba(233,238,234,.5) 80%, rgba(233,238,234,.16));
}
.wire__post {
  position: absolute; top: calc(50% - 15px); width: 1px; height: 30px;
  background: rgba(233, 238, 234, .3);
}
.wire__post--1 { left: 14%; } .wire__post--2 { left: 51%; } .wire__post--3 { left: 86%; }
.wire__pulse {
  position: absolute; top: 50%; left: 0; width: 46px; height: 2px;
  margin-top: -1px; border-radius: 2px;
  background: linear-gradient(90deg, transparent, var(--volt-fill));
  filter: drop-shadow(0 0 6px rgba(233, 179, 8, .8));
  animation: travel 1.2s linear infinite;
}
@keyframes travel {
  0%   { transform: translateX(0); opacity: 0; }
  8%   { opacity: 1; }
  92%  { opacity: 1; }
  100% { transform: translateX(calc(100% + 100%)); opacity: 0; }
}

.readout { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1px; background: rgba(233,238,234,.12); }
.readout__cell { background: var(--hero-bg); padding: 12px 10px 10px; }
.readout dt { font-size: .68rem; letter-spacing: .1em; color: var(--on-dark-2); }
.readout dd { margin: 6px 0 0; }
.readout .mono { font-size: clamp(1.05rem, 2.6vw, 1.45rem); color: var(--on-dark); }

.panel__note {
  margin-top: 16px; font-size: .78rem; line-height: 1.8; color: var(--on-dark-2);
}

.hazard {
  height: 8px;
  background: repeating-linear-gradient(-45deg, var(--volt-fill) 0 12px, #141e26 12px 24px);
}

/* ---------- 5. Sheet & sections ---------- */
.sheet {
  position: relative;
  max-width: var(--sheet-max);
  margin: 0 auto;
  padding: 0 var(--sheet-pad);
}

.wire-rail {
  position: absolute; top: 0; bottom: 0; left: var(--sheet-pad);
  width: 1px; background: var(--rule); overflow: hidden;
}
.wire-rail__fill {
  display: block; width: 100%; height: 0;
  background: linear-gradient(180deg, var(--volt-fill), color-mix(in srgb, var(--volt-fill) 35%, transparent));
}

.sec {
  display: grid;
  grid-template-columns: var(--rail-w) minmax(0, 1fr);
  column-gap: var(--rail-gap);
}
.sec__rail { position: relative; padding-top: 46px; }
.sec__rail::before {
  content: ""; position: absolute; left: 0; top: 0; bottom: 0;
  width: 1px; background: var(--rule);
}
.node {
  position: relative; display: block;
  width: 11px; height: 11px; margin-left: -5px;
  border-radius: 50%; border: 2px solid var(--rule-2);
  background: var(--paper);
}
.sec.is-in .node { border-color: var(--volt-fill); background: var(--volt-fill); }
.sec__tag {
  display: block; margin-top: 10px;
  font-family: var(--f-mono); font-size: .68rem; letter-spacing: .16em;
  color: var(--ink-3); writing-mode: horizontal-tb;
}

.sec__body { padding: 46px 0 84px; min-width: 0; }
.sec:last-of-type .sec__body { padding-bottom: 96px; }

.h2 {
  font-family: var(--f-disp); font-size: clamp(1.42rem, 2.9vw, 2rem);
  line-height: 1.42; letter-spacing: -0.005em;
  margin-bottom: 18px;
}
.lead-para {
  max-width: 46em; color: var(--ink-2); font-size: .95rem; line-height: 1.95;
  margin-bottom: 34px;
}

.prose { max-width: 44em; }
.prose p + p { margin-top: 18px; }
.prose strong { font-weight: 700; }
.prose p { text-wrap: pretty; }

/* reveal
   本文は決して隠さない（描画タイミングで内容が消える実装を避ける）。
   動きは碍子の点灯と通電パルスだけに絞る。 */
.sec .node { transition: border-color .45s var(--ease), background-color .45s var(--ease); }

/* callout */
.callout {
  margin-top: 30px; max-width: 44em;
  border-left: 2px solid var(--volt-fill);
  background: color-mix(in srgb, var(--volt-fill) 7%, var(--surface));
  padding: 20px 22px;
}
.callout__label {
  font-family: var(--f-mono); font-size: .68rem; letter-spacing: .16em;
  color: var(--volt-text); margin-bottom: 8px;
}
.callout p:last-child { font-size: .92rem; line-height: 1.95; }
.callout--warn { border-left-color: var(--warn); }
.callout--warn .callout__label { color: var(--warn); }

/* exclude list */
.exclude { display: grid; gap: 2px; max-width: 46em; }
.exclude > li {
  display: grid; grid-template-columns: 44px minmax(0, 1fr);
  gap: 18px; padding: 22px 0; border-top: 1px solid var(--rule);
}
.exclude > li:last-child { border-bottom: 1px solid var(--rule); }
.exclude__mark {
  font-size: .72rem; color: var(--ink-3); padding-top: 5px;
}
.exclude h3 { font-family: var(--f-disp); font-size: 1.05rem; line-height: 1.6; margin-bottom: 7px; }
.exclude p { font-size: .9rem; line-height: 1.9; color: var(--ink-2); text-wrap: pretty; }

/* criteria */
.crit { display: grid; gap: 22px; }
.crit__item {
  border: 1px solid var(--rule); background: var(--surface);
  padding: 26px 26px 24px;
}
.crit__no {
  font-size: .7rem; letter-spacing: .18em; color: var(--volt-text);
  margin-bottom: 12px;
}
.crit__item h3 { font-family: var(--f-disp); font-size: 1.16rem; line-height: 1.6; margin-bottom: 12px; }
.crit__item > p { max-width: 44em; font-size: .93rem; line-height: 1.95; color: var(--ink-2); text-wrap: pretty; }
.crit__item > p + p { margin-top: 12px; }
.crit__points { margin-top: 18px; display: grid; gap: 10px; }
.crit__points li {
  position: relative; padding-left: 22px;
  font-size: .88rem; line-height: 1.85; color: var(--ink-2);
}
.crit__points li::before {
  content: ""; position: absolute; left: 0; top: .68em;
  width: 10px; height: 1px; background: var(--rule-2);
}
.crit__points strong { color: var(--ink); font-weight: 700; }

.mini { margin-top: 20px; overflow-x: auto; }
.mini__table { border-collapse: collapse; width: 100%; min-width: 420px; font-size: .86rem; }
.mini__table caption {
  caption-side: top; text-align: left; font-family: var(--f-mono);
  font-size: .68rem; letter-spacing: .12em; color: var(--ink-3); padding-bottom: 8px;
}
.mini__table th, .mini__table td { text-align: left; padding: 10px 14px; border-bottom: 1px solid var(--rule); }
.mini__table th { width: 34%; font-weight: 500; color: var(--ink); white-space: nowrap; }
.mini__table td { color: var(--ink-2); }

/* ---------- 6. Tool ---------- */
.sec--tool .sec__body { position: relative; }
.tool {
  display: grid; grid-template-columns: minmax(0, 1fr) minmax(260px, 340px);
  border: 1px solid var(--rule); background: var(--surface);
}
.tool__in { padding: 26px; border-right: 1px solid var(--rule); }

.field { border: 0; padding: 0; margin: 0 0 26px; }
.field:last-child { margin-bottom: 0; }
.field legend, .field label {
  display: flex; align-items: baseline; justify-content: space-between; gap: 12px;
  font-size: .82rem; letter-spacing: .06em; color: var(--ink-2);
  padding: 0 0 12px;
}
.field label { width: 100%; }
.field output { color: var(--ink); font-size: 1rem; }

.seg { display: flex; flex-wrap: wrap; gap: 6px; }
.seg__btn {
  display: inline-flex; align-items: center; gap: 7px;
  padding: 9px 13px; border: 1px solid var(--rule);
  background: var(--paper); border-radius: var(--radius);
  font-size: .86rem;
  transition: border-color .18s var(--ease), background-color .18s var(--ease);
}
.seg__btn:hover { border-color: var(--rule-2); }
.seg__btn.is-on {
  border-color: var(--volt-fill);
  background: color-mix(in srgb, var(--volt-fill) 16%, var(--surface));
  font-weight: 500;
}
.seg__hint {
  font-family: var(--f-mono); font-size: .66rem; color: var(--ink-3);
}
.seg__btn.is-on .seg__hint { color: var(--volt-text); }
.field__note {
  margin-top: 12px; font-size: .8rem; line-height: 1.8; color: var(--ink-3);
  max-width: 40em; text-wrap: pretty;
}
.field__note.is-alert { color: var(--warn); }

input[type="range"] {
  -webkit-appearance: none; appearance: none;
  width: 100%; height: 26px; background: transparent; cursor: pointer;
}
input[type="range"]::-webkit-slider-runnable-track {
  height: 2px; background: var(--rule-2); border-radius: 2px;
}
input[type="range"]::-moz-range-track {
  height: 2px; background: var(--rule-2); border-radius: 2px;
}
input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none; appearance: none;
  width: 18px; height: 18px; margin-top: -8px; border-radius: 50%;
  background: var(--volt-fill); border: 3px solid var(--surface);
  box-shadow: 0 0 0 1px var(--rule-2);
}
input[type="range"]::-moz-range-thumb {
  width: 14px; height: 14px; border-radius: 50%;
  background: var(--volt-fill); border: 3px solid var(--surface);
  box-shadow: 0 0 0 1px var(--rule-2);
}
.field__scale {
  display: flex; justify-content: space-between;
  font-size: .64rem; color: var(--ink-3); margin-top: 2px;
}

.tool__out {
  padding: 26px; background: var(--hero-bg); color: var(--on-dark);
}
[data-theme="dark"] .tool__out { background: #0a1118; }
.tool__label {
  font-family: var(--f-mono); font-size: .66rem; letter-spacing: .16em;
  color: var(--on-dark-2);
}
.tool__label--mt { margin-top: 26px; }
.tool__total { display: flex; align-items: baseline; gap: 6px; margin-top: 8px; }
.tool__total .mono { font-size: clamp(2rem, 5vw, 2.6rem); line-height: 1.1; color: var(--volt-fill); }
.tool__unit { font-size: .9rem; color: var(--on-dark-2); }
.tool__formula { font-size: .72rem; color: var(--on-dark-2); margin-top: 4px; }
.chips { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; }
.chip {
  display: inline-flex; align-items: center; gap: 7px;
  padding: 6px 10px; border: 1px solid rgba(233,238,234,.22);
  border-radius: var(--radius); font-size: .76rem;
  background: rgba(233, 238, 234, .04);
}
.chip .mono { font-size: .68rem; color: var(--volt-fill); }
.chip--none { border-color: rgba(224,133,97,.5); color: var(--on-dark-2); }
.tool__note { margin-top: 14px; font-size: .74rem; line-height: 1.8; color: var(--on-dark-2); text-wrap: pretty; }

/* ---------- 7. Compare table ---------- */
.filters {
  display: flex; flex-wrap: wrap; gap: 20px 34px;
  padding: 16px 0 20px; border-top: 1px solid var(--rule);
}
.filters__group { display: flex; flex-wrap: wrap; align-items: center; gap: 6px; }
.filters__label {
  font-family: var(--f-mono); font-size: .66rem; letter-spacing: .14em;
  color: var(--ink-3); margin-right: 4px;
}
.chip-btn {
  padding: 7px 12px; border: 1px solid var(--rule);
  border-radius: 999px; font-size: .8rem;
  transition: border-color .18s var(--ease), background-color .18s var(--ease), color .18s var(--ease);
}
.chip-btn:hover { border-color: var(--rule-2); }
.chip-btn.is-on {
  background: var(--ink); border-color: var(--ink); color: var(--paper);
}

.table-wrap {
  overflow-x: auto; -webkit-overflow-scrolling: touch;
  overscroll-behavior-x: contain;
  border: 1px solid var(--rule); background: var(--surface);
}
.table-wrap::after {
  /* 狭い画面で横スクロールできることを示す細い目印 */
  content: "";
  position: sticky; left: 0;
  display: block; height: 3px;
  background: linear-gradient(90deg, var(--rule-2), transparent);
  opacity: .5;
}
.compare {
  /* collapse だと sticky 有効時にヘッダーが1行目へ重なる報告があるため separate を使う。
     罫線は各セル側に付けてあるので見た目は変わらない */
  border-collapse: separate; border-spacing: 0;
  width: 100%; min-width: 880px;
  font-size: .86rem;
}
.compare thead th {
  /* sticky を付けない。固定ヘッダーが1行目に重なって行を隠す事故を防ぐ */
  background: var(--paper-2);
  font-family: var(--f-mono); font-size: .68rem; font-weight: 500;
  letter-spacing: .1em; color: var(--ink-2);
  text-align: left; padding: 12px 16px;
  border-bottom: 1px solid var(--rule-2);
  white-space: nowrap;
}
.compare th[scope="row"], .compare td {
  text-align: left; vertical-align: top;
  padding: 16px; border-bottom: 1px solid var(--rule);
}
.compare th[scope="row"] {
  /* 1列目も固定しない。横スクロール時に見出しの下へ潜り込ませない */
  background: var(--surface); min-width: 240px;
  font-weight: 400;
}
.compare tbody tr:hover th[scope="row"],
.compare tbody tr:hover td { background: color-mix(in srgb, var(--volt-fill) 6%, var(--surface)); }
.compare tbody tr:last-child th, .compare tbody tr:last-child td { border-bottom: 0; }
.compare .mono { font-size: .84rem; }
.t-id { display: block; font-size: .68rem; color: var(--volt-text); margin-bottom: 5px; }
.t-name { display: block; line-height: 1.6; }
.t-model { display: block; font-family: var(--f-mono); font-size: .72rem; color: var(--ink-3); }
.t-sub { display: block; font-size: .76rem; color: var(--ink-3); line-height: 1.65; margin-top: 3px; }
.compare tbody tr.is-out { display: none; }

.notes { margin-top: 22px; display: grid; gap: 10px; max-width: 48em; }
.notes p { font-size: .8rem; line-height: 1.85; color: var(--ink-3); text-wrap: pretty; }

/* ---------- 8. Product cards ---------- */
.card {
  border: 1px solid var(--rule); background: var(--surface);
  padding: 26px; margin-bottom: 22px;
}
.card:last-child { margin-bottom: 0; }
.card--outside { border-style: dashed; border-color: var(--rule-2); }
.card__head { display: flex; flex-wrap: wrap; align-items: baseline; gap: 8px 16px; }
.card__id { font-size: .72rem; color: var(--volt-text); }
.card__name {
  font-family: var(--f-disp); font-size: 1.14rem; line-height: 1.6;
  flex: 1 1 320px;
}
.card__model { font-family: var(--f-mono); font-size: .74rem; color: var(--ink-3); }
.card__price .mono { font-size: 1.05rem; }
.card__spec {
  margin-top: 12px; font-size: .76rem; line-height: 1.8; color: var(--ink-2);
  padding: 10px 12px; border-left: 2px solid var(--rule-2); background: var(--paper);
  word-break: break-word;
}
.card__split {
  margin-top: 20px; display: grid;
  grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 1px;
  background: var(--rule);
}
.fit { background: var(--surface); padding: 16px 18px; }
.fit--yes { border-top: 2px solid var(--live); }
.fit--no { border-top: 2px solid var(--warn); }
.fit__label {
  font-family: var(--f-mono); font-size: .68rem; letter-spacing: .12em;
  margin-bottom: 10px;
}
.fit--yes .fit__label { color: var(--live); }
.fit--no .fit__label { color: var(--warn); }
.fit ul { display: grid; gap: 7px; }
.fit li {
  position: relative; padding-left: 20px;
  font-size: .86rem; line-height: 1.8; color: var(--ink-2); text-wrap: pretty;
}
.fit--yes li::before {
  content: ""; position: absolute; left: 2px; top: .72em;
  width: 8px; height: 1px; background: var(--live);
}
.fit--no li::before {
  content: ""; position: absolute; left: 2px; top: .72em;
  width: 8px; height: 1px; background: var(--warn);
}
.card__note {
  margin-top: 18px; max-width: 46em; font-size: .88rem; line-height: 1.95;
  color: var(--ink-2); text-wrap: pretty;
}

/* ---------- 9. Accordion ---------- */
.acc { max-width: 48em; border-top: 1px solid var(--rule); }
.acc__item { border-bottom: 1px solid var(--rule); }
.acc__item summary {
  display: flex; align-items: center; gap: 14px;
  padding: 20px 4px; cursor: pointer; list-style: none;
  transition: color .18s var(--ease);
}
.acc__item summary::-webkit-details-marker { display: none; }
.acc__item summary::before {
  content: ""; flex: none; width: 9px; height: 9px;
  border-right: 1.5px solid var(--ink-2); border-bottom: 1.5px solid var(--ink-2);
  transform: rotate(-45deg); margin-left: 4px;
  transition: transform .25s var(--ease), border-color .18s var(--ease);
}
.acc__item[open] summary::before { transform: rotate(45deg); border-color: var(--volt-fill); }
.acc__item summary:hover { color: var(--volt-text); }
.acc__q { font-family: var(--f-disp); font-size: 1.02rem; flex: 1 1 auto; }
.acc__meta {
  font-size: .66rem; letter-spacing: .1em; color: var(--ink-3);
  border: 1px solid var(--rule); padding: 3px 8px; border-radius: 999px;
  white-space: nowrap;
}
.acc__body { padding: 0 4px 24px 27px; }
.acc__body p { font-size: .9rem; line-height: 1.95; color: var(--ink-2); max-width: 42em; text-wrap: pretty; }

/* ---------- 10. Fit list ---------- */
.fitlist { display: grid; gap: 1px; background: var(--rule); border: 1px solid var(--rule); }
.fitlist__row {
  background: var(--surface); padding: 20px 22px;
  display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(0, 1fr) minmax(0, 1.3fr);
  gap: 8px 28px; align-items: baseline;
}
.fitlist__cond { font-family: var(--f-disp); font-size: .98rem; line-height: 1.65; }
.fitlist__pick { font-size: .9rem; display: flex; flex-wrap: wrap; gap: 8px; align-items: baseline; }
.fitlist__pick .mono:first-child { color: var(--volt-text); font-size: .72rem; }
.fitlist__why { font-size: .84rem; line-height: 1.8; color: var(--ink-3); text-wrap: pretty; }

/* ---------- 11. Checklist ---------- */
.check { border: 1px solid var(--rule); background: var(--surface); padding: 24px 26px 26px; }
.check__bar { height: 2px; background: var(--rule); overflow: hidden; }
.check__fill { display: block; height: 100%; width: 0; background: var(--volt-fill); transition: width .35s var(--ease); }
.check__count { margin-top: 12px; font-size: .72rem; color: var(--ink-3); }
.check__count .mono { color: var(--ink); }
.check__list { margin-top: 18px; display: grid; gap: 2px; }
.check__list li { border-top: 1px solid var(--rule); }
.check__list li:first-child { border-top: 0; }
.check__list label { display: flex; align-items: flex-start; gap: 14px; padding: 14px 0; cursor: pointer; }
.check__list input {
  -webkit-appearance: none; appearance: none;
  flex: none; width: 18px; height: 18px; margin-top: 3px;
  border: 1.5px solid var(--rule-2); border-radius: 2px; background: var(--paper);
  transition: background-color .18s var(--ease), border-color .18s var(--ease);
}
.check__list input:checked { background: var(--volt-fill); border-color: var(--volt-fill); }
.check__list input:checked::after {
  content: ""; display: block; width: 9px; height: 5px; margin: 3px 0 0 3.5px;
  border-left: 2px solid #141e26; border-bottom: 2px solid #141e26;
  transform: rotate(-45deg);
}
.check__list span { font-size: .9rem; line-height: 1.85; text-wrap: pretty; }
.check__list input:checked + span { color: var(--ink-3); text-decoration: line-through; text-decoration-color: var(--rule-2); }

/* ---------- 12. Footer ---------- */
.foot { background: var(--hero-bg); color: var(--on-dark-2); }
.foot__inner {
  max-width: var(--sheet-max); margin: 0 auto;
  padding: 56px var(--sheet-pad) 40px;
}
.foot__lead {
  font-family: var(--f-mono); font-size: .68rem; letter-spacing: .18em;
  color: var(--volt-fill); margin-bottom: 18px;
}
.foot__list { display: grid; gap: 12px; max-width: 52em; }
.foot__list li {
  position: relative; padding-left: 18px;
  font-size: .82rem; line-height: 1.9;
}
.foot__list li::before {
  content: ""; position: absolute; left: 0; top: .85em;
  width: 8px; height: 1px; background: rgba(233, 238, 234, .35);
}
.foot__end { margin-top: 30px; padding-top: 22px; border-top: 1px solid rgba(233,238,234,.14); }
.foot__end a { color: var(--on-dark-2); font-size: .82rem; text-decoration: none; }
.foot__end a:hover { color: var(--volt-fill); }

/* ---------- 13. To top ---------- */
.totop {
  position: fixed; right: 20px; bottom: 20px; z-index: 40;
  width: 44px; height: 44px; border-radius: 50%;
  background: var(--ink); border: 1px solid var(--rule-2);
  display: grid; place-items: center;
  box-shadow: 0 10px 24px -14px rgba(0, 0, 0, .6);
  transition: transform .2s var(--ease), opacity .2s var(--ease);
}
.totop:hover { transform: translateY(-2px); }
.totop__arrow {
  width: 9px; height: 9px; margin-top: 3px;
  border-left: 1.5px solid var(--paper); border-top: 1.5px solid var(--paper);
  transform: rotate(45deg);
}

/* ---------- 14. Responsive ---------- */
@media (max-width: 980px) {
  :root { --rail-w: 0px; --rail-gap: 0px; }
  .hero__grid { grid-template-columns: 1fr; }
  .tool { grid-template-columns: 1fr; }
  .tool__in { border-right: 0; border-bottom: 1px solid var(--rule); }
  .wire-rail { display: none; }
  .sec { grid-template-columns: minmax(0, 1fr); }
  .sec__rail { padding-top: 34px; display: flex; align-items: center; gap: 10px; }
  .sec__rail::before { display: none; }
  .node { margin-left: 0; width: 9px; height: 9px; }
  .sec__tag { margin-top: 0; }
  .sec__body { padding: 8px 0 68px; }
  .fitlist__row { grid-template-columns: 1fr; gap: 6px; }
  .compare th[scope="row"] { min-width: 200px; }
}

@media (max-width: 620px) {
  :root { --sheet-pad: 20px; --header-h: 56px; }
  body { font-size: 16px; }
  .hero { padding-top: 40px; }
  .panel { padding: 18px 16px; }
  .readout { grid-template-columns: 1fr 1fr; }
  .readout__cell:last-child { grid-column: 1 / -1; }
  .card, .crit__item, .check { padding: 20px 18px; }
  .tool__in, .tool__out { padding: 20px 18px; }
  .exclude > li { grid-template-columns: 30px minmax(0, 1fr); gap: 12px; }
  .acc__body { padding-left: 0; }
  .filters { gap: 14px; }
  .totop { right: 14px; bottom: 14px; }
}

@media print {
  .topbar, .totop, .hero__cta, .filters, .seg, input[type="range"] { display: none !important; }
  body { background: #fff; font-size: 10.5pt; }
  .hero { background: #fff; color: #000; padding: 0 0 12px; }
  .hero__title, .hero__sub, .hero__lead, .panel__note { color: #000; }
  .panel, .card, .tool, .check { break-inside: avoid; }
  a { text-decoration: none; }
}

/* ---------- 15. Motion preferences ---------- */
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  .wire__pulse, .lamp { animation: none; }
  .wire__pulse { opacity: .7; }
  .sec .node { transition: none; }
  * { transition-duration: .01ms !important; }
}

</style>
</head>
<body>

<a class="skip" href="#main">本文へスキップ</a>

<header class="topbar" id="topbar">
  <div class="topbar__inner">
    <a class="brand" href="#hero">
      <span class="brand__mark" aria-hidden="true"></span>
      <span class="brand__text">電気柵 本体の選び方</span>
    </a>
    <div class="topbar__tools">
      <button class="toc-btn" type="button" aria-expanded="false" aria-controls="toc">目次</button>
      <button class="theme-btn" type="button" aria-pressed="false" aria-label="表示テーマを切り替える">
        <span class="theme-btn__icon" aria-hidden="true"></span>
      </button>
    </div>
  </div>
  <nav class="toc" id="toc" aria-label="目次" hidden>
    <ol>
      <li><a href="#scene">足跡を見つけた朝</a></li>
      <li><a href="#who">この記事が向いていない人</a></li>
      <li><a href="#criteria">見るのは3つだけ</a></li>
      <li><a href="#tool">総延長の判定ツール</a></li>
      <li><a href="#table">同じ物差しで並べる</a></li>
      <li><a href="#models">1機種ずつ、向き・不向き</a></li>
      <li><a href="#voices">レビューで多かった不満</a></li>
      <li><a href="#fit">状況別のおすすめ</a></li>
      <li><a href="#after">買ったあと、最初にやること</a></li>
    </ol>
  </nav>
  <div class="progress" aria-hidden="true"><span class="progress__bar" id="progressBar"></span></div>
</header>

<!-- ============ HERO ============ -->
<section class="hero" id="hero">
  <div class="hero__grid">
    <div class="hero__copy">
      <p class="hero__eyebrow">獣害対策 ／ 電気柵 本体の選び方</p>
      <h1 class="hero__title">
        <span class="hero__num">12kV</span><span class="hero__dot">・</span><span class="hero__num">1.2J</span><span class="hero__dot">・</span><span class="hero__num">最大10km</span>
      </h1>
      <p class="hero__sub">その3つの数字は、あなたの畑で何を意味するのか。</p>
      <p class="hero__lead">足跡を見つけた翌日、ホームセンターの箱の前で止まった。値段だけ見て帰ってきた。夜、Amazonで「電気柵 本体」と検索して、星の数だけを見ている。そんな段階の人のために、1万円前後で買える本体4機種と、比較対象の国産セット1台を、同じ物差しで並べました。</p>
      <div class="hero__cta">
        <a class="btn btn--volt" href="#tool">総延長を計算する</a>
        <a class="btn btn--ghost" href="#table">比較表を見る</a>
      </div>
    </div>

    <div class="panel" aria-label="電気柵本体の表示例">
      <div class="panel__head">
        <span class="panel__label">POWER UNIT</span>
        <span class="panel__state"><span class="lamp" aria-hidden="true"></span>通電中</span>
      </div>
      <div class="wire" aria-hidden="true">
        <span class="wire__line"></span>
        <span class="wire__pulse"></span>
        <span class="wire__post wire__post--1"></span>
        <span class="wire__post wire__post--2"></span>
        <span class="wire__post wire__post--3"></span>
      </div>
      <dl class="readout">
        <div class="readout__cell">
          <dt>出力電圧</dt>
          <dd><span class="mono" data-count="12" data-suffix="kV">12kV</span></dd>
        </div>
        <div class="readout__cell">
          <dt>出力エネルギー</dt>
          <dd><span class="mono" data-count="1.2" data-suffix="J" data-decimals="1">1.2J</span></dd>
        </div>
        <div class="readout__cell">
          <dt>パルス周期</dt>
          <dd><span class="mono" data-count="1.0" data-suffix="秒" data-decimals="1">1.0秒</span></dd>
        </div>
      </dl>
      <p class="panel__note">この3つが読めれば、本体選びはほぼ終わります。読み方をこの記事でほどいていきます。</p>
    </div>
  </div>
  <div class="hazard" aria-hidden="true"></div>
</section>

<main class="sheet" id="main">
  <span class="wire-rail" aria-hidden="true"><span class="wire-rail__fill" id="railFill"></span></span>

  <!-- ============ 01 SCENE ============ -->
  <section class="sec" id="scene">
    <div class="sec__rail"><span class="node" aria-hidden="true"></span><span class="sec__tag">場面</span></div>
    <div class="sec__body">
      <h2 class="h2">足跡を見つけた朝</h2>
      <div class="prose">
        <p>畑に出て、まず足跡に気づきます。次に、葉っぱが食われている。ここから数日は、朝いちばんに畑を見に行く生活になります。</p>
        <p>対策は電気柵しかない、と腹は決まっている。問題は、その先です。棚に並ぶ箱には大きな文字で数字が書かれているのに、どれが自分の畑に必要なのか分からない。結局いちばん安いものを買うか、いちばん高いものを買うか。判断の材料がないまま、そのどちらかに落ちてしまう。</p>
        <p>この記事でやりたいのは、その数字の読み方の整理です。そして、いちばん大事な前提を先に言っておきます。<strong>本体だけ買っても、柵にはなりません。</strong>支柱と柵線とアース棒が要ります。この点を後回しにすると、あとから出費がじわじわ増えます。</p>
      </div>
      <aside class="callout callout--warn">
        <p class="callout__label">先に知っておくこと</p>
        <p>電気柵は「張って終わり」の道具ではありません。草が伸びれば電圧が落ちます。電圧が落ちた柵は、獣に「痛くない」と教えてしまいます。生き物を相手にする設備なので、そこだけは前提として受け取っておいてください。</p>
      </aside>
    </div>
  </section>

  <!-- ============ 02 WHO ============ -->
  <section class="sec" id="who">
    <div class="sec__rail"><span class="node" aria-hidden="true"></span><span class="sec__tag">外す人</span></div>
    <div class="sec__body">
      <h2 class="h2">この記事が向いていない人</h2>
      <p class="lead-para">先に外します。次のどれかに当てはまるなら、ここで読むのをやめても大丈夫です。</p>
      <ul class="exclude">
        <li>
          <span class="exclude__mark mono">01</span>
          <div>
            <h3>被害が一度きりで、その後ぱったり止まっている</h3>
            <p>まず様子を見たほうが安く済みます。電気柵は設置もメンテナンスも手がかかる設備です。</p>
          </div>
        </li>
        <li>
          <span class="exclude__mark mono">02</span>
          <div>
            <h3>獣の種類がまだ特定できていない</h3>
            <p>イノシシなら2段、シカなら4段、アライグマなどの中型なら下を細かく4段。必要な段数がまったく違います。段数が決まらないと、本体の選定に入れません。足跡と食害の形から先に絞り込んでください。</p>
          </div>
        </li>
        <li>
          <span class="exclude__mark mono">03</span>
          <div>
            <h3>人の通る場所、犬の散歩道に面している</h3>
            <p>電気柵は正しく設置されていれば人や動物の命に関わるものではない、というのが基本的な説明です。ただしそれは正しい設置と管理が前提の話。住宅密集地では、別の選択肢を検討する場面だと思います。</p>
          </div>
        </li>
        <li>
          <span class="exclude__mark mono">04</span>
          <div>
            <h3>「これさえ買えば獣が来なくなる」を期待している</h3>
            <p>段数と高さが合っていても、入られることはあります。一度入れた個体は、無理にでも入ろうとすることが知られています。柵は、管理とセットで効くものです。</p>
          </div>
        </li>
      </ul>
    </div>
  </section>

  <!-- ============ 03 CRITERIA ============ -->
  <section class="sec" id="criteria">
    <div class="sec__rail"><span class="node" aria-hidden="true"></span><span class="sec__tag">見る基準</span></div>
    <div class="sec__body">
      <h2 class="h2">本体を選ぶとき、見るのは3つだけ</h2>
      <p class="lead-para">カタログには10個くらい数字が並んでいますが、判断に効くのはこの3つです。順番もこのままで。</p>

      <ol class="crit">
        <li class="crit__item">
          <p class="crit__no mono">Criterion 01</p>
          <h3>電源方式と、現地での充電の現実</h3>
          <p>AC100Vが引ける畑なら話は早いです。電圧が安定して、電池切れの心配もない。ただし延長コードと防水の手当てが要ります。引けない畑は、ソーラーかバッテリーか乾電池になります。</p>
          <ul class="crit__points">
            <li><strong>乾電池</strong> — 設置場所を選ばない。切れるタイミングが分かりにくく、電池代が続く。</li>
            <li><strong>バッテリー</strong> — 繰り返し使える。定期的な充電と電圧チェックが必要。</li>
            <li><strong>ソーラー</strong> — 手間は最小。日当たりの悪い場所では弱く、バッテリーが消耗品になる。</li>
            <li><strong>AC100V</strong> — 出力が安定し、管理の負担が軽い。電源のない畑では選べない。</li>
          </ul>
        </li>

        <li class="crit__item">
          <p class="crit__no mono">Criterion 02</p>
          <h3>出力（J）と、柵線の総延長に対する余裕</h3>
          <p>ここが商品ページでいちばん読み取りにくいところです。「最大10km」はカタログ上の到達距離で、日本の細かい畑でそのまま出る数字ではありません。</p>
          <p>見る順番はこうです。自分の畑の周囲長を出す。段数を掛ける。それが総延長。その総延長に対して、本体の実力に余裕があるかどうか。出力の目安が総延長ギリギリだと、些細な漏電が柵全体に影響して、管理がとてもシビアになります。余裕のある機種を選ぶほうが、結果的に楽です。</p>
        </li>

        <li class="crit__item">
          <p class="crit__no mono">Criterion 03</p>
          <h3>付属品と、買い足しの総額</h3>
          <p>支柱、柵線、アース棒、検電器。この4つは別売です。計算に入れないと、本体代より高くつきます。セット品が高いのには、理由があります。</p>
          <div class="mini">
            <table class="mini__table">
              <caption>本体だけで買った場合に足すもの</caption>
              <tbody>
                <tr><th>支柱</th><td>周囲長 ÷ 支柱間隔（2〜3mが目安）× 段数</td></tr>
                <tr><th>柵線</th><td>総延長 ＋ 引き回しの余長</td></tr>
                <tr><th>アース棒</th><td>必要な本数と深さ。乾いた石の多い土では増える</td></tr>
                <tr><th>検電器</th><td>電圧が見えないと、止まっていることに気づけない</td></tr>
              </tbody>
            </table>
          </div>
        </li>
      </ol>
    </div>
  </section>

  <!-- ============ 04 TOOL ============ -->
  <section class="sec sec--tool" id="tool">
    <div class="sec__rail"><span class="node" aria-hidden="true"></span><span class="sec__tag">判定</span></div>
    <div class="sec__body">
      <h2 class="h2">畑の周囲長から、必要な機種を逆算する</h2>
      <p class="lead-para">周囲長と段数を入れると、総延長が出ます。公表されている対応距離と突き合わせて、候補を絞り込みます。公開情報にもとづく目安なので、最終判断は各商品ページと地域の普及指導機関で確認してください。</p>

      <div class="tool">
        <div class="tool__in">
          <fieldset class="field">
            <legend>守りたい相手</legend>
            <div class="seg" role="radiogroup" aria-label="守りたい相手">
              <button type="button" class="seg__btn is-on" role="radio" aria-checked="true" data-beast="boar" data-rows="2">イノシシ<span class="seg__hint">2段</span></button>
              <button type="button" class="seg__btn" role="radio" aria-checked="false" data-beast="deer" data-rows="4">シカ<span class="seg__hint">4段</span></button>
              <button type="button" class="seg__btn" role="radio" aria-checked="false" data-beast="mid" data-rows="4">中型<span class="seg__hint">4段</span></button>
              <button type="button" class="seg__btn" role="radio" aria-checked="false" data-beast="monkey" data-rows="">サル<span class="seg__hint">要確認</span></button>
              <button type="button" class="seg__btn" role="radio" aria-checked="false" data-beast="unknown" data-rows="">不明<span class="seg__hint">—</span></button>
            </div>
            <p class="field__note" id="beastNote">イノシシは最下段を地上20cm、その上の段を20cm間隔の2段が基本とされています。</p>
          </fieldset>

          <div class="field">
            <label for="perimeter">畑の周囲長 <output class="mono" id="perimeterOut">80 m</output></label>
            <input type="range" id="perimeter" min="10" max="400" step="5" value="80">
            <div class="field__scale mono" aria-hidden="true"><span>10m</span><span>200m</span><span>400m</span></div>
          </div>

          <div class="field">
            <label for="rows">柵線の段数 <output class="mono" id="rowsOut">2 段</output></label>
            <input type="range" id="rows" min="1" max="8" step="1" value="2">
            <div class="field__scale mono" aria-hidden="true"><span>1段</span><span>4段</span><span>8段</span></div>
          </div>
        </div>

        <div class="tool__out" aria-live="polite">
          <p class="tool__label">柵線の総延長</p>
          <p class="tool__total"><span class="mono" id="totalOut">160</span><span class="tool__unit">m</span></p>
          <p class="tool__formula mono" id="formulaOut">80m × 2段</p>

          <p class="tool__label tool__label--mt">公表値を満たす機種</p>
          <ul class="chips" id="chips"><!-- JS --></ul>
          <p class="tool__note" id="toolNote">総延長に対して公表値がギリギリの機種は、草の接触による漏電で電圧が落ちやすくなります。1ランク上を選ぶと管理が楽になります。</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ============ 05 TABLE ============ -->
  <section class="sec" id="table">
    <div class="sec__rail"><span class="node" aria-hidden="true"></span><span class="sec__tag">比較</span></div>
    <div class="sec__body">
      <h2 class="h2">同じ物差しで並べる</h2>
      <p class="lead-para">価格・電源・出力・公表の対応距離・付属品。この5列に揃えると、箱の前での迷いが減ります。絞り込みと並べ替えができます。</p>

      <div class="filters">
        <div class="filters__group" role="group" aria-label="絞り込み">
          <span class="filters__label">絞り込み</span>
          <button type="button" class="chip-btn is-on" data-filter="all">すべて</button>
          <button type="button" class="chip-btn" data-filter="solar">ソーラー可</button>
          <button type="button" class="chip-btn" data-filter="ac">ACで使える</button>
          <button type="button" class="chip-btn" data-filter="kit">セット品</button>
        </div>
        <div class="filters__group" role="group" aria-label="並べ替え">
          <span class="filters__label">並べ替え</span>
          <button type="button" class="chip-btn" data-sort="price">価格が安い順</button>
          <button type="button" class="chip-btn" data-sort="power">出力電圧が高い順</button>
          <button type="button" class="chip-btn" data-sort="dist">対応距離が長い順</button>
        </div>
      </div>

      <div class="table-wrap">
        <table class="compare" id="compareTable">
          <caption class="sr-only">電気柵本体とセット品の比較表</caption>
          <thead>
            <tr>
              <th scope="col">商品</th>
              <th scope="col">価格（税込）</th>
              <th scope="col">電源方式</th>
              <th scope="col">出力</th>
              <th scope="col">公表の対応距離</th>
              <th scope="col">付属</th>
            </tr>
          </thead>
          <tbody>
            <tr data-id="p1" data-price="14989" data-power="12" data-dist="10000" data-src="solar,multi" data-set="unit">
              <th scope="row"><span class="mono t-id">#1</span><span class="t-name">ahomeone 電気柵 エナジャイザー<br><span class="t-model">LJCYW228335</span></span></th>
              <td><span class="mono">14,989円</span></td>
              <td>ソーラー一体型<br><span class="t-sub">7.5Wパネル＋12V 6Ah内蔵</span></td>
              <td><span class="mono">12kV ／ 1.2J</span></td>
              <td><span class="mono">最大10km</span></td>
              <td>本体のみ</td>
            </tr>
            <tr data-id="p2" data-price="8787" data-power="12" data-dist="12000" data-src="multi,solar,ac" data-set="unit">
              <th scope="row"><span class="mono t-id">#2</span><span class="t-name">ahomeone 電気柵 自作キット</span></th>
              <td><span class="mono">8,787円</span></td>
              <td>3電源<br><span class="t-sub">AC110V／12Vバッテリー／ソーラー</span></td>
              <td><span class="mono">12kV ／ 1.5〜3J</span></td>
              <td><span class="mono">約12km</span></td>
              <td>本体のみ</td>
            </tr>
            <tr data-id="p3" data-price="8988" data-power="13" data-dist="15000" data-src="multi,solar,ac" data-set="unit">
              <th scope="row"><span class="mono t-id">#3</span><span class="t-name">ahomeone 電気柵エナジャイザー</span></th>
              <td><span class="mono">8,988円</span></td>
              <td>3電源<br><span class="t-sub">AC110V／12Vバッテリー／ソーラー</span></td>
              <td><span class="mono">7kV〜13kV 可変</span></td>
              <td><span class="mono">最大15km</span></td>
              <td>本体のみ</td>
            </tr>
            <tr data-id="p4" data-price="8612" data-power="0" data-dist="12000" data-src="ac" data-set="unit">
              <th scope="row"><span class="mono t-id">#4</span><span class="t-name">ahomeone 電気柵用電源</span></th>
              <td><span class="mono">8,612円</span></td>
              <td>AC専用<br><span class="t-sub">110V。12Vバッテリーは別売</span></td>
              <td><span class="t-sub">出力の記載なし</span></td>
              <td><span class="mono">約12km</span></td>
              <td>本体のみ</td>
            </tr>
            <tr data-id="p5" data-price="32800" data-power="0" data-dist="3000" data-src="battery,solar" data-set="kit">
              <th scope="row"><span class="mono t-id">#5</span><span class="t-name">ニシデン アニマルバスター NSD-5<br><span class="t-model">2段張り 50mセット</span></span></th>
              <td><span class="mono">32,800円</span></td>
              <td>乾電池式<br><span class="t-sub">単三×8本（別売）／ソーラー化は後付け</span></td>
              <td><span class="mono">ランプは約3,500V以上で点灯</span></td>
              <td><span class="mono">最大3,000m</span></td>
              <td>本体＋支柱＋柵線</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="notes">
        <p>数字は各商品ページの表記にもとづきます。表の数字は「そう書かれている」という意味で、畑でそのとおりになる保証ではありません。#1〜#4は本体のみで、支柱・柵線・アース棒・検電器は含まれていません。</p>
        <p>価格・仕様は執筆時点のものです。変更されることがあるので、購入前に各商品ページでご確認ください。</p>
      </div>
    </div>
  </section>

  <!-- ============ 06 MODELS ============ -->
  <section class="sec" id="models">
    <div class="sec__rail"><span class="node" aria-hidden="true"></span><span class="sec__tag">機種別</span></div>
    <div class="sec__body">
      <h2 class="h2">1機種ずつ、向き・不向き</h2>
      <p class="lead-para">良いところだけ書いても選べないので、合わない場面も同じ分量で書きます。</p>

      <article class="card" data-id="p1">
        <header class="card__head">
          <p class="card__id mono">#1</p>
          <h3 class="card__name">ahomeone 電気柵 エナジャイザー <span class="card__model">LJCYW228335</span></h3>
          <p class="card__price"><span class="mono">14,989円</span></p>
        </header>
        <p class="card__spec mono">7.5Wソーラー ＋ 12V 6Ah 内蔵 ／ 12kV・1.2J ／ 最大10km ／ 本体のみ</p>
        <div class="card__split">
          <div class="fit fit--yes">
            <p class="fit__label">向いている人</p>
            <ul>
              <li>コンセントのない離れた畑</li>
              <li>通うのが月に数回で、日当たりの良い場所</li>
              <li>配線作業をしたくない</li>
            </ul>
          </div>
          <div class="fit fit--no">
            <p class="fit__label">向いていない人</p>
            <ul>
              <li>山の陰、木の下など日当たりが悪い</li>
              <li>毎日は見に行けず、日当たりも悪い</li>
              <li>段数を増やして広く囲いたい</li>
            </ul>
          </div>
        </div>
        <p class="card__note">ソーラーとバッテリーが本体に入っているので、置くだけで動きます。この手軽さは大きい。ただ、この中では出力エネルギーが控えめです。そしてソーラー内蔵タイプに共通する落とし穴が、晴れた昼は電圧が立っているのに夜に落ちている、という状態。原因はバッテリーの劣化であることが多く、12Vの鉛なら満充電で13V以上、12.3V以上に充電できないものは傷んでいるとされています。</p>
      </article>

      <article class="card" data-id="p2">
        <header class="card__head">
          <p class="card__id mono">#2</p>
          <h3 class="card__name">ahomeone 電気柵 自作キット</h3>
          <p class="card__price"><span class="mono">8,787円</span></p>
        </header>
        <p class="card__spec mono">AC110V ／ 12Vバッテリー ／ ソーラー ／ 12kV・1.5〜3J ／ 約12km ／ 本体のみ</p>
        <div class="card__split">
          <div class="fit fit--yes">
            <p class="fit__label">向いている人</p>
            <ul>
              <li>すでに12Vバッテリーやパネルを持っている</li>
              <li>畑が広めで、段数を増やす予定がある</li>
              <li>ACが引けるので電源に困らない</li>
            </ul>
          </div>
          <div class="fit fit--no">
            <p class="fit__label">向いていない人</p>
            <ul>
              <li>箱を開けてすぐ張りたい</li>
              <li>電源を用意する気がない</li>
              <li>出力の数字を読み解く気力がない</li>
            </ul>
          </div>
        </div>
        <p class="card__note">電源を3通りから選べて、出力の幅もあります。この余裕は、段数を増やすときに効いてきます。名前のとおり、電源は自分で用意する前提の商品です。</p>
      </article>

      <article class="card" data-id="p3">
        <header class="card__head">
          <p class="card__id mono">#3</p>
          <h3 class="card__name">ahomeone 電気柵エナジャイザー</h3>
          <p class="card__price"><span class="mono">8,988円</span></p>
        </header>
        <p class="card__spec mono">AC110V ／ 12Vバッテリー ／ ソーラー ／ 7kV〜13kV 可変 ／ 最大15km ／ 本体のみ</p>
        <div class="card__split">
          <div class="fit fit--yes">
            <p class="fit__label">向いている人</p>
            <ul>
              <li>まず1〜2段で始めたい</li>
              <li>出力を絞って運用したい</li>
              <li>獣の反応を見ながら調整したい</li>
            </ul>
          </div>
          <div class="fit fit--no">
            <p class="fit__label">向いていない人</p>
            <ul>
              <li>1台で広い畑を最初から囲いたい</li>
              <li>「最大15km」という表記を実力と受け取った</li>
            </ul>
          </div>
        </div>
        <p class="card__note">出力を7kVから13kVまで絞れるのが特徴です。総延長が短い家庭菜園で、パワーを抑えて使いたい場面に合います。カタログの最大距離に引っ張られると期待が外れます。</p>
      </article>

      <article class="card" data-id="p4">
        <header class="card__head">
          <p class="card__id mono">#4</p>
          <h3 class="card__name">ahomeone 電気柵用電源</h3>
          <p class="card__price"><span class="mono">8,612円</span></p>
        </header>
        <p class="card__spec mono">110V AC専用 ／ 12Vバッテリーは別売 ／ 出力の記載なし ／ 約12km ／ 本体のみ</p>
        <div class="card__split">
          <div class="fit fit--yes">
            <p class="fit__label">向いている人</p>
            <ul>
              <li>納屋や母屋の壁にコンセントがある</li>
              <li>そこから数十mの畑を守りたい</li>
              <li>電池やソーラーの心配から解放されたい</li>
            </ul>
          </div>
          <div class="fit fit--no">
            <p class="fit__label">向いていない人</p>
            <ul>
              <li>電源のない畑（現地で詰みます）</li>
              <li>延長ケーブルの防水処理をしたくない</li>
              <li>出力を数値で比べたい</li>
            </ul>
          </div>
        </div>
        <p class="card__note">ACが引けるなら、これで足りる場面があります。逆に、電源のない畑には持っていけません。この条件だけは読み違えないでください。</p>
      </article>

      <article class="card card--outside" data-id="p5">
        <header class="card__head">
          <p class="card__id mono">#5 ／帯外</p>
          <h3 class="card__name">ニシデン アニマルバスター NSD-5 <span class="card__model">2段張り 50mセット</span></h3>
          <p class="card__price"><span class="mono">32,800円</span></p>
        </header>
        <p class="card__spec mono">単三アルカリ乾電池×8本（別売）／ソーラー化は後付け ／ 出力ランプは約3,500V以上で点灯、出力周期 約1.0〜1.2秒 ／ 最大3,000m ／ 本体＋支柱＋柵線</p>
        <div class="card__split">
          <div class="fit fit--yes">
            <p class="fit__label">向いている人</p>
            <ul>
              <li>初めてで、失敗したくない</li>
              <li>通電しているかを現場で目で確認したい</li>
              <li>予算を最初にまとめて確定させたい</li>
            </ul>
          </div>
          <div class="fit fit--no">
            <p class="fit__label">向いていない人</p>
            <ul>
              <li>初期費用を抑えたい</li>
              <li>段数をあとから増やす前提がない（2段のセット）</li>
              <li>乾電池の交換を想像できていない</li>
            </ul>
          </div>
        </div>
        <p class="card__note">価格帯から外れていますが、判断の基準として入れました。違うのは、支柱と柵線が最初から入っていること。そして通電しているかがランプと音で分かる設計であることです。ソーラー化も後から足せます。本体に1万円を投じるか、3万円台で一式揃えるか。ここが実質いちばんの分岐点だと思っています。</p>
      </article>
    </div>
  </section>

  <!-- ============ 07 VOICES ============ -->
  <section class="sec" id="voices">
    <div class="sec__rail"><span class="node" aria-hidden="true"></span><span class="sec__tag">不満</span></div>
    <div class="sec__body">
      <h2 class="h2">レビューで多かった不満と、その対処</h2>
      <p class="lead-para">公開されている購入者の声とメーカー・自治体の技術資料を突き合わせると、出てくる不満は「商品のせい」より「使い方のつまずき」に寄っていました。多い順に並べます。</p>

      <div class="acc">
        <details class="acc__item" open>
          <summary><span class="acc__q">電圧が上がらない</span><span class="acc__meta mono">最多</span></summary>
          <div class="acc__body">
            <p>いちばん多いのがこれです。原因は本体の故障より、アース不足と乾燥した土であることが多いとされます。アース棒は本体がすべて隠れるまで打ち込み、石が多く乾いた場所では設置位置を見直します。</p>
          </div>
        </details>

        <details class="acc__item">
          <summary><span class="acc__q">草で漏電する</span></summary>
          <div class="acc__body">
            <p>草や落ち葉が線に触れるだけで電気が逃げます。鉄が触れると損失はさらに大きい。草刈りの導線を決めておく、草が触れない高さに管理する。地味ですが、ここが電気柵の本体です。除草のことを考えずに支柱を立てると、毎年の作業が増えます。</p>
          </div>
        </details>

        <details class="acc__item">
          <summary><span class="acc__q">夜に効いていない気がする</span><span class="acc__meta mono">ソーラー式に多い</span></summary>
          <div class="acc__body">
            <p>日中の電圧は正常に見えるのに、夜だけ落ちる。ソーラー充電タイプでは、これがバッテリー劣化のサインであることがあります。バッテリーの寿命は3〜5年程度が目安で、充電不足が続くと2年程度で劣化が進むこともあるとされています。3年以上使っているなら、テスターで電圧を見てください。</p>
          </div>
        </details>

        <details class="acc__item">
          <summary><span class="acc__q">電池切れに気づかなかった</span></summary>
          <div class="acc__body">
            <p>乾電池式の弱点です。切れるタイミングが分かりにくく、気づいたときには食害が広がっている、という流れになります。月に一度の点検日を先にカレンダーへ書いてしまうのが現実的です。</p>
          </div>
        </details>

        <details class="acc__item">
          <summary><span class="acc__q">本体だけ買ったら、あとから出費が増えた</span></summary>
          <div class="acc__body">
            <p>支柱と柵線の見積もりを先に出す。これに尽きます。本体8,000円で始めたつもりが、結果的にセット品より高くついた、という声は少なくありません。</p>
          </div>
        </details>

        <details class="acc__item">
          <summary><span class="acc__q">入られた</span></summary>
          <div class="acc__body">
            <p>段数と高さのミス、地面との隙間、斜面に近すぎる、そして一度入った個体は強引にでも入る。柵の外に獣の逃げ場がない設置も、柵を壊される原因になります。ここは本体の性能では解決しません。</p>
          </div>
        </details>
      </div>
    </div>
  </section>

  <!-- ============ 08 FIT ============ -->
  <section class="sec" id="fit">
    <div class="sec__rail"><span class="node" aria-hidden="true"></span><span class="sec__tag">状況別</span></div>
    <div class="sec__body">
      <h2 class="h2">状況別のおすすめ</h2>
      <p class="lead-para">条件から選ぶときの早見です。金額は本体のみの価格で、支柱と柵線は別とお考えください。</p>

      <ul class="fitlist">
        <li class="fitlist__row">
          <p class="fitlist__cond">コンセントがあり、畑は狭い</p>
          <p class="fitlist__pick"><span class="mono">#4</span> AC専用 <span class="mono">8,612円</span></p>
          <p class="fitlist__why">電源の心配が消えるのが最大の利点。延長ケーブルの防水だけ手当てを。</p>
        </li>
        <li class="fitlist__row">
          <p class="fitlist__cond">コンセントはないが、日当たりは良い</p>
          <p class="fitlist__pick"><span class="mono">#1</span> ソーラー一体型 <span class="mono">14,989円</span></p>
          <p class="fitlist__why">配線も充電も不要。ただし日当たりが前提条件になります。</p>
        </li>
        <li class="fitlist__row">
          <p class="fitlist__cond">畑が広め／段数を増やす予定がある</p>
          <p class="fitlist__pick"><span class="mono">#2</span> 自作キット <span class="mono">8,787円</span></p>
          <p class="fitlist__why">出力の幅があり、AC・バッテリー・ソーラーを選べます。電源は自分で用意。</p>
        </li>
        <li class="fitlist__row">
          <p class="fitlist__cond">まず1〜2段で試したい</p>
          <p class="fitlist__pick"><span class="mono">#3</span> 可変タイプ <span class="mono">8,988円</span></p>
          <p class="fitlist__why">出力を絞れるので、小規模の畑で使いやすい。</p>
        </li>
        <li class="fitlist__row">
          <p class="fitlist__cond">初めてで失敗したくない。予算が許す</p>
          <p class="fitlist__pick"><span class="mono">#5</span> 国産セット <span class="mono">32,800円</span></p>
          <p class="fitlist__why">支柱と柵線が最初から揃い、通電状態がランプで分かります。</p>
        </li>
      </ul>
    </div>
  </section>

  <!-- ============ 09 AFTER ============ -->
  <section class="sec" id="after">
    <div class="sec__rail"><span class="node" aria-hidden="true"></span><span class="sec__tag">設置後</span></div>
    <div class="sec__body">
      <h2 class="h2">買ったあと、最初にやること</h2>
      <p class="lead-para">届いた日と、その翌日の作業が、この先1年の楽さを決めます。チェックを付けながら進めてください（この端末のブラウザにだけ保存されます）。</p>

      <div class="check">
        <div class="check__bar" aria-hidden="true"><span class="check__fill" id="checkFill"></span></div>
        <p class="check__count"><span class="mono" id="checkCount">0 / 7</span> 完了</p>
        <ul class="check__list" id="checkList">
          <li><label><input type="checkbox" data-key="k1"><span>アース棒を、本体が全部隠れるまで打ち込む</span></label></li>
          <li><label><input type="checkbox" data-key="k2"><span>石が多く乾いた土なら、アースの設置場所を変えてみる</span></label></li>
          <li><label><input type="checkbox" data-key="k3"><span>張り終えた日に通電して、獣に一度体験させる</span></label></li>
          <li><label><input type="checkbox" data-key="k4"><span>検電器で末端の電圧を測る（日中）</span></label></li>
          <li><label><input type="checkbox" data-key="k5"><span>できれば夜にも測る。ソーラー式は特に</span></label></li>
          <li><label><input type="checkbox" data-key="k6"><span>人の目に触れる場所に危険表示板を付ける</span></label></li>
          <li><label><input type="checkbox" data-key="k7"><span>草刈りの日にちを決めて、カレンダーに書く</span></label></li>
        </ul>
      </div>

      <div class="prose">
        <p>電圧の目安として、末端で4,000V以上は確保したい、5,000Vを下回る状態が続くと侵入される可能性が上がる、というのが現場で共有されている数字です。本体単体の点検では6,000V以上が正常の目安として示されることもあります。</p>
        <p>本体選びで差がつくのは、出力の数字そのものより、その電源方式を自分が維持できるかどうかです。高い本体を買って点検がおろそかになれば、安い本体と同じか、それ以下になります。逆に、自分の通える頻度と日当たりに合った1台を選べば、1万円以下でも仕事をしてくれます。</p>
      </div>
    </div>
  </section>
</main>

<footer class="foot">
  <div class="foot__inner">
    <p class="foot__lead">この記事について</p>
    <ul class="foot__list">
      <li>価格・仕様は執筆時点（2026年10月）の各商品ページの表記にもとづきます。変更される可能性があるため、購入前に必ず各商品ページでご確認ください。</li>
      <li>数字は公表値を並べたもので、畑での結果を保証するものではありません。設置条件・獣種・地形によって変わります。</li>
      <li>電気柵の設置にあたっては、危険表示板の設置など安全基準・法令の確認と、地域の普及指導機関・自治体の指導内容の確認をおすすめします。</li>
      <li>特定の商品の購入を勧めるものではありません。条件に合うかを判断する材料としてお使いください。</li>
    </ul>
    <p class="foot__end"><a href="#hero">ページの先頭へ</a></p>
  </div>
</footer>

<button class="totop" type="button" id="toTop" aria-label="ページの先頭へ戻る" hidden>
  <span class="totop__arrow" aria-hidden="true"></span>
</button>

<script defer>
/* =========================================================
   電気柵 本体の選び方 — main.js
   依存ライブラリなし。すべて DOMContentLoaded 後に実行。
   ========================================================= */
(function () {
  'use strict';

  var root = document.documentElement;
  root.classList.add('js');

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $  = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ---------- 1. テーマ ---------- */
  var THEME_KEY = 'fence-compare:theme';
  var themeBtn = $('.theme-btn');

  function applyTheme(mode) {
    root.setAttribute('data-theme', mode);
    if (themeBtn) {
      themeBtn.setAttribute('aria-pressed', mode === 'dark' ? 'true' : 'false');
      themeBtn.setAttribute('aria-label', mode === 'dark' ? '明るい表示に切り替える' : '暗い表示に切り替える');
    }
    var meta = $('meta[name="theme-color"]');
    if (meta) meta.setAttribute('content', mode === 'dark' ? '#0e1720' : '#0e1720');
  }

  function storedTheme() {
    try { return localStorage.getItem(THEME_KEY); } catch (e) { return null; }
  }

  applyTheme(storedTheme() || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'));

  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      applyTheme(next);
      try { localStorage.setItem(THEME_KEY, next); } catch (e) {}
    });
  }

  /* ---------- 2. 目次パネル ---------- */
  var tocBtn = $('.toc-btn');
  var toc = $('#toc');

  function setToc(open) {
    if (!tocBtn || !toc) return;
    toc.hidden = !open;
    tocBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  if (tocBtn) {
    tocBtn.addEventListener('click', function () { setToc(toc.hidden); });
  }
  if (toc) {
    toc.addEventListener('click', function (e) { if (e.target.closest('a')) setToc(false); });
  }
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') setToc(false);
  });
  document.addEventListener('click', function (e) {
    if (!toc || toc.hidden) return;
    if (e.target.closest('#toc') || e.target.closest('.toc-btn')) return;
    setToc(false);
  });

  /* ---------- 3. スクロール進捗 / トップへ戻る ---------- */
  var bar = $('#progressBar');
  var railFill = $('#railFill');
  var toTop = $('#toTop');
  var ticking = false;

  function onScroll() {
    var h = document.documentElement;
    var max = h.scrollHeight - h.clientHeight;
    var y = window.scrollY || h.scrollTop;
    var ratio = max > 0 ? Math.min(1, Math.max(0, y / max)) : 0;

    if (bar) bar.style.width = (ratio * 100).toFixed(2) + '%';
    if (railFill) railFill.style.height = (ratio * 100).toFixed(2) + '%';
    if (toTop) toTop.hidden = y < 600;
    ticking = false;
  }

  window.addEventListener('scroll', function () {
    if (!ticking) { ticking = true; window.requestAnimationFrame(onScroll); }
  }, { passive: true });
  window.addEventListener('resize', onScroll, { passive: true });
  onScroll();

  if (toTop) {
    toTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
    });
  }

  /* ---------- 4. 節点（碍子）の点灯 ----------
     本文の表示・非表示には一切関与しない。内容が消える余地を作らない。 */
  if (!reduceMotion && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        en.target.classList.add('is-in');
        io.unobserve(en.target);
      });
    }, { rootMargin: '-6% 0px -6% 0px', threshold: 0.02 });

    $$('.sec').forEach(function (el) { io.observe(el); });
  }

  /* ---------- 5. ヒーローの読み出し値（一度だけ動かす） ---------- */
  (function countUp() {
    var els = $$('[data-count]');
    els.forEach(function (el) {
      var target = parseFloat(el.getAttribute('data-count'));
      var suffix = el.getAttribute('data-suffix') || '';
      var dec = parseInt(el.getAttribute('data-decimals') || '0', 10);
      if (isNaN(target)) return;
      function fmt(v) { return v.toFixed(dec) + suffix; }
      if (reduceMotion) { el.textContent = fmt(target); return; }

      var start = null, dur = 900;
      function step(ts) {
        if (start === null) start = ts;
        var p = Math.min(1, (ts - start) / dur);
        var eased = 1 - Math.pow(1 - p, 3);
        el.textContent = fmt(target * eased);
        if (p < 1) window.requestAnimationFrame(step);
        else el.textContent = fmt(target);
      }
      el.textContent = fmt(0);
      window.requestAnimationFrame(step);
    });
  })();

  /* ---------- 6. 総延長の判定ツール ---------- */
  var TOOLS = {
    perimeter: $('#perimeter'),
    perimeterOut: $('#perimeterOut'),
    rows: $('#rows'),
    rowsOut: $('#rowsOut'),
    totalOut: $('#totalOut'),
    formulaOut: $('#formulaOut'),
    chips: $('#chips'),
    note: $('#toolNote'),
    beastNote: $('#beastNote')
  };

  var PRODUCTS = [
    { id: '#1', name: 'ahomeone ソーラー一体型', dist: 10000, distLabel: '最大10km', src: ['solar'] },
    { id: '#2', name: 'ahomeone 自作キット',      dist: 12000, distLabel: '約12km',  src: ['ac', 'battery', 'solar'] },
    { id: '#3', name: 'ahomeone 可変タイプ',      dist: 15000, distLabel: '最大15km', src: ['ac', 'battery', 'solar'] },
    { id: '#4', name: 'ahomeone AC専用',          dist: 12000, distLabel: '約12km',  src: ['ac'] },
    { id: '#5', name: 'ニシデン NSD-5 セット',    dist: 3000,  distLabel: '最大3,000m', src: ['battery'] }
  ];

  var BEASTS = {
    boar:    { rows: 2, note: 'イノシシは、最下段を地上20cm、その上の段を20cm間隔にした2段が基本とされています。' },
    deer:    { rows: 4, note: 'シカは、最下段を地上20cm、そこから30cm・30cm・40cm間隔にした4段が基本とされています。' },
    mid:     { rows: 4, note: 'アライグマなどの中型は、最下段を地上5cm、それ以降を10cm間隔にした4段が基本とされています。' },
    monkey:  { rows: 0, note: 'サルの段数は資料によって幅があり、8段張りのセットが販売されている例もあります。段数は地域の普及指導機関に確認してください。' },
    unknown: { rows: 0, note: '足跡と食害の形から、獣種を先に絞り込んでください。段数が決まらないと本体の選定に入れません。' }
  };

  var requiredRows = 2;

  function renderTool() {
    if (!TOOLS.perimeter || !TOOLS.rows) return;

    var per = parseInt(TOOLS.perimeter.value, 10);
    var rows = parseInt(TOOLS.rows.value, 10);
    var total = per * rows;

    TOOLS.perimeterOut.textContent = per + ' m';
    TOOLS.rowsOut.textContent = rows + ' 段';
    TOOLS.totalOut.textContent = total.toLocaleString('ja-JP');
    TOOLS.formulaOut.textContent = per + 'm × ' + rows + '段';

    var hits = PRODUCTS.filter(function (p) { return p.dist >= total; });
    TOOLS.chips.innerHTML = '';

    if (!hits.length) {
      var li = document.createElement('li');
      li.className = 'chip chip--none';
      li.textContent = '公表値でカバーできる機種がありません。周囲長か段数を見直すか、より上位の機種を検討してください。';
      TOOLS.chips.appendChild(li);
    } else {
      hits.forEach(function (p) {
        var li = document.createElement('li');
        li.className = 'chip';
        li.innerHTML = '<span class="mono">' + p.id + '</span>' + p.name +
                       ' <span class="mono">' + p.distLabel + '</span>';
        TOOLS.chips.appendChild(li);
      });
    }

    var msg = '総延長に対して公表値がギリギリの機種は、草の接触による漏電で電圧が落ちやすくなります。1ランク上を選ぶと管理が楽になります。';
    if (requiredRows && rows < requiredRows) {
      msg = '選んだ相手に対しては' + requiredRows + '段が基本とされています。段数を下げると、鼻先に線が当たらず素通りされる可能性があります。';
    } else if (total > 3000) {
      msg = '#5（ニシデン セット）の公表値3,000mを超えています。セット品を使う場合は本体の上位機種にするか、まず範囲を区切って設置することを検討してください。';
    }
    TOOLS.note.textContent = msg;
  }

  if (TOOLS.perimeter && TOOLS.rows) {
    TOOLS.perimeter.addEventListener('input', renderTool);
    TOOLS.rows.addEventListener('input', renderTool);

    $$('.seg__btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        $$('.seg__btn').forEach(function (b) {
          b.classList.remove('is-on');
          b.setAttribute('aria-checked', 'false');
        });
        btn.classList.add('is-on');
        btn.setAttribute('aria-checked', 'true');

        var info = BEASTS[btn.getAttribute('data-beast')];
        var preset = parseInt(btn.getAttribute('data-rows'), 10);

        if (info) {
          TOOLS.beastNote.textContent = info.note;
          TOOLS.beastNote.classList.remove('is-alert');
          requiredRows = info.rows;
        }
        if (preset) TOOLS.rows.value = preset;
        renderTool();
      });
    });

    renderTool();
  }

  /* ---------- 7. 比較表の絞り込み / 並べ替え ---------- */
  var table = $('#compareTable');

  if (table) {
    var tbody = table.tBodies[0];
    var allRows = $$('tr', tbody);

    function applyFilter(key) {
      allRows.forEach(function (tr) {
        var src = (tr.getAttribute('data-src') || '').split(',');
        var isKit = tr.getAttribute('data-set') === 'kit';
        var show = key === 'all' ||
                   (key === 'kit' ? isKit : src.indexOf(key) > -1);
        tr.classList.toggle('is-out', !show);
      });
    }

    function applySort(key) {
      var sorted = allRows.slice().sort(function (a, b) {
        var av = parseFloat(a.getAttribute('data-' + key)) || 0;
        var bv = parseFloat(b.getAttribute('data-' + key)) || 0;
        if (key === 'price') return av - bv;
        return bv - av;
      });
      sorted.forEach(function (tr) { tbody.appendChild(tr); });
    }

    $$('.chip-btn[data-filter]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        $$('.chip-btn[data-filter]').forEach(function (b) { b.classList.remove('is-on'); });
        btn.classList.add('is-on');
        applyFilter(btn.getAttribute('data-filter'));
      });
    });

    $$('.chip-btn[data-sort]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var already = btn.classList.contains('is-on');
        $$('.chip-btn[data-sort]').forEach(function (b) { b.classList.remove('is-on'); });
        if (already) { applySort('orig'); return; }
        btn.classList.add('is-on');
        applySort(btn.getAttribute('data-sort'));
      });
    });

    // 「元の順」に戻すための初期順を記録
    allRows.forEach(function (tr, i) { tr.setAttribute('data-orig', String(i)); });
  }

  /* ---------- 8. 設置チェックリスト ---------- */
  var checkList = $('#checkList');
  var CHECK_KEY = 'fence-compare:checks';

  if (checkList) {
    var boxes = $$('input[type="checkbox"]', checkList);
    var fill = $('#checkFill');
    var count = $('#checkCount');
    var saved = {};

    try { saved = JSON.parse(localStorage.getItem(CHECK_KEY) || '{}') || {}; } catch (e) { saved = {}; }

    boxes.forEach(function (box) {
      var key = box.getAttribute('data-key');
      if (saved[key]) box.checked = true;
      box.addEventListener('change', function () {
        saved[key] = box.checked;
        try { localStorage.setItem(CHECK_KEY, JSON.stringify(saved)); } catch (e) {}
        updateChecks();
      });
    });

    function updateChecks() {
      var done = boxes.filter(function (b) { return b.checked; }).length;
      if (fill) fill.style.width = (done / boxes.length * 100).toFixed(0) + '%';
      if (count) count.textContent = done + ' / ' + boxes.length;
    }
    updateChecks();
  }

  /* ---------- 9. 目次の現在地表示 ---------- */
  if ('IntersectionObserver' in window) {
    var links = $$('#toc a');
    var map = {};
    links.forEach(function (a) {
      var id = a.getAttribute('href');
      if (id && id.charAt(0) === '#') map[id.slice(1)] = a;
    });

    var secObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        var a = map[en.target.id];
        if (!a) return;
        if (en.isIntersecting) {
          links.forEach(function (l) { l.removeAttribute('aria-current'); });
          a.setAttribute('aria-current', 'true');
          a.style.color = '';
        } else if (a.getAttribute('aria-current') === 'true') {
          a.removeAttribute('aria-current');
        }
      });
    }, { rootMargin: '-20% 0px -70% 0px' });

    Object.keys(map).forEach(function (id) {
      var el = document.getElementById(id);
      if (el) secObserver.observe(el);
    });
  }
})();

</script>
<script type="module" src="https://static.cloudflareinsights.com/beacon.min.js/v4bc70e2c01a94c73b74392e4234840661791215815920" integrity="sha512-L0ha0OXavK/8okipN9F8BtP84dg9DUhPERbBXzwI6dgTA55d2+yweo3pn5CSFYs45/r8md2+xvUPtTdvTNRfjA==" data-cf-beacon='{"version":"2024.11.0","token":"4edd5f8ec12a48cfa682ab8261b80a79","spa":2}' crossorigin="anonymous"></script>
</body>
</html>
    """
