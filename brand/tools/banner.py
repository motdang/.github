import sys
ANT = '''<g fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="20">
<path d="M340 194 C314 170 298 148 294 116 C292 96 306 84 320 92 C330 98 326 112 314 110" stroke-width="16"/>
<path d="M380 194 C406 170 422 148 426 116 C428 96 414 84 400 92 C390 98 394 112 406 110" stroke-width="16"/>
<circle cx="360" cy="222" r="34"/>
<path d="M346 252 C338 262 338 270 348 274" stroke-width="14"/>
<path d="M374 252 C382 262 382 270 372 274" stroke-width="14"/>
<ellipse cx="360" cy="292" rx="26" ry="34"/><circle cx="360" cy="340" r="10"/>
<path d="M360 362 C398 362 418 394 418 426 C418 468 392 496 360 496 C328 496 302 468 302 426 C302 394 322 362 360 362 Z"/>
<path d="M360 390 C384 398 396 418 392 442 C389 460 372 466 364 454 C358 444 368 434 376 440" stroke-width="14"/>
<path d="M338 270 C304 258 276 240 258 210 C250 196 236 200 240 214 C243 225 256 222 254 212" stroke-width="16"/>
<path d="M382 270 C416 258 444 240 462 210 C470 196 484 200 480 214 C477 225 464 222 466 212" stroke-width="16"/>
<path d="M334 292 C292 292 258 304 234 334 C224 346 210 340 214 326 C217 316 230 316 232 326" stroke-width="16"/>
<path d="M386 292 C428 292 462 304 486 334 C496 346 510 340 506 326 C503 316 490 316 488 326" stroke-width="16"/>
<path d="M340 314 C302 334 280 366 272 406 C269 420 254 420 254 406 C254 396 266 392 272 400" stroke-width="16"/>
<path d="M380 314 C418 334 440 366 448 406 C451 420 466 420 466 406 C466 396 454 392 448 400" stroke-width="16"/>
</g>'''
def page(dark):
    bg, ink, red, sub, chip, trail = (("#16182a","#fff8ec","#ff6b5c","#c9c4d6","#d7261e","#3a3d55") if dark
                                      else ("#fff8ec","#1d2033","#d7261e","#5b5870","#d7261e","#e9d9c4"))
    # marching ants along the bottom, the third carries a gold crumb
    ants = ""
    for i, x in enumerate(range(600, 1260, 120)):
        y = 338 + (6 if i % 2 else 0)
        crumb = f'<circle cx="360" cy="70" r="46" fill="#f5c400" stroke="none"/>' if i == 2 else ""
        ants += f'<g transform="translate({x} {y}) rotate(90) scale(.14) translate(-360 -290)" stroke="{red}">{ANT}{crumb}</g>'
    return f'''<!doctype html><meta charset="utf-8"><style>
@font-face{{font-family:Mali;font-weight:700;src:url(../fonts/mali-700-thai.woff2);unicode-range:U+0E00-0E7F}}
@font-face{{font-family:Mali;font-weight:700;src:url(../fonts/mali-700-latin.woff2);unicode-range:U+0000-024F,U+2000-206F}}
@font-face{{font-family:Prompt;font-weight:400;src:url(../fonts/prompt-400-thai.woff2);unicode-range:U+0E00-0E7F}}
@font-face{{font-family:Prompt;font-weight:400;src:url(../fonts/prompt-400-latin.woff2);unicode-range:U+0000-024F,U+2000-206F}}
@font-face{{font-family:Prompt;font-weight:600;src:url(../fonts/prompt-600-thai.woff2);unicode-range:U+0E00-0E7F}}
@font-face{{font-family:Prompt;font-weight:600;src:url(../fonts/prompt-600-latin.woff2);unicode-range:U+0000-024F,U+2000-206F}}
html,body{{margin:0;background:{bg}}} body{{width:1280px;height:400px;position:relative;overflow:hidden}}
.stripe{{position:absolute;inset:0 0 auto 0;height:10px;background:#f5c400}}
.tile{{position:absolute;left:72px;top:72px;width:236px;height:236px;border-radius:56px;background:{chip};transform:rotate(-4deg);box-shadow:0 10px 0 {trail}}}
.tile svg{{width:236px;height:236px}}
.t{{position:absolute;left:372px;top:58px;font:700 112px/1 Mali;color:{red};letter-spacing:-1px}}
.t span{{color:{ink};font-size:84px;margin-left:18px}}
.s{{position:absolute;left:378px;top:196px;font:400 30px/1.35 Prompt;color:{sub}}}
.s b{{font-weight:600;color:{ink}}}
.trail{{position:absolute;left:0;top:0}}
</style><body><div class="stripe"></div>
<div class="tile"><svg viewBox="132 65 457 457" stroke="#fff8ec">{ANT}</svg></div>
<div class="t">มดแดง<span>Mot Dang</span></div>
<div class="s"><b>รู้ทุกซอย เหมือนมดแดง</b><br>City guide · Chiang Mai &amp; Chiang Rai · motdang.net</div>
<svg class="trail" width="1280" height="400"><path d="M520 340 C700 320 900 362 1280 336" stroke="{trail}" stroke-width="3" stroke-dasharray="2 12" stroke-linecap="round" fill="none"/>{ants}</svg>
</body>'''
for dark in (0, 1):
    open(f"banner-{'dark' if dark else 'light'}.html", "w").write(page(dark))
