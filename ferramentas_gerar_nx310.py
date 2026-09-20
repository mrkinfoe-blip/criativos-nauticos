from PIL import Image, ImageDraw, ImageFont
import os

AZUL  = (0x32, 0x86, 0xc7)
PRETO = (0x1d, 0x1d, 0x1b)
BRANCO= (255, 255, 255)
S = 1080
FB = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

def quadrado(src, bias=0.5):
    im = Image.open(src).convert("RGB")
    w, h = im.size
    if w >= h:
        lado = h
        x = int((w - lado) * 0.5); y = 0
    else:
        lado = w
        x = 0
        y = int((h - lado) * bias)
    im = im.crop((x, y, x + lado, y + lado)).resize((S, S), Image.LANCZOS)
    return im

def card(src, saida, bias=0.5, titulo=None):
    im = quadrado(src, bias)
    d = ImageDraw.Draw(im, "RGBA")

    painel_h = 132
    # escurecimento suave acima do painel para o texto grande respirar
    if titulo:
        for i in range(260):
            a = int(150 * (i / 260) ** 1.6)
            d.line([(0, S - painel_h - 260 + i), (S, S - painel_h - 260 + i)], fill=(0, 0, 0, a))

    if titulo:
        f = ImageFont.truetype(FB, 62)
        d.text((56, S - painel_h - 96), titulo, font=f, fill=BRANCO)

    d.rectangle([0, S - painel_h, S, S], fill=PRETO)
    d.rectangle([0, S - painel_h - 6, S, S - painel_h], fill=AZUL)
    d.text((56, S - painel_h + 30), "GUSTAVO MENEZES", font=ImageFont.truetype(FB, 34), fill=BRANCO)
    d.text((56, S - painel_h + 74), "Consultoria Náutica", font=ImageFont.truetype(FR, 26), fill=(190, 190, 190))

    im.save(saida, "JPEG", quality=92, optimize=True)
    return saida

O = "nx-novos/nx310-impact/originais"
D = "nx-novos/nx310-impact"
plano = [
    (f"{O}/01-externa-proa.jpg", f"{D}/card-1.jpg", 0.58, "NX 310 IMPACT"),
    (f"{O}/02-aerea.jpg",        f"{D}/card-2.jpg", 0.50, None),
    (f"{O}/04-cockpit.jpg",      f"{D}/card-3.jpg", 0.50, None),
    (f"{O}/06-cabine.jpg",       f"{D}/card-4.jpg", 0.50, None),
    (f"{O}/08-console.jpg",      f"{D}/card-5.jpg", 0.52, None),
    (f"{O}/03-duas-unidades.jpg",f"{D}/single-duas.jpg", 0.50, "NX 310 IMPACT"),
]
for src, out, bias, tit in plano:
    print(card(src, out, bias, tit))
