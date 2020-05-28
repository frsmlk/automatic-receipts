from PIL import Image,ImageDraw,ImageFont

image_wdp = Image.open('/assets/wdp.png')
image_cpp = Image.open('/assets/cpp.png')
font_league_spartan = ImageFont.truetype('/fonts/LeagueSpartan-Bold.otf', 40 )
font_kollekif = ImageFont.truetype('/fonts/Kollektif.ttf', 29)
font_kollekif_bold = ImageFont.truetype('/fontsKollektif-Bold.ttf', 29)
font_arimo = ImageFont.truetype('/fonts/Arimo-Italic.ttf', 26)


draw = ImageDraw.Draw(image)
draw.text(xy=(191,545), text="FARIS MALIK",fill=(83,143,147), font=font_league_spartan)
draw.text(xy=(195,829), text=str(4), fill=(111,111,110),font=font_kollekif)
draw.text(xy=(1085,829), text="RM 400", fill=(111,111,110),font=font_kollekif)
draw.text(xy=(1085,1131.5), text="RM 400", fill=(111,111,110),font=font_kollekif_bold)
draw.text(xy=(730,1295), text="FARIS", fill=(111,111,110),font=font_arimo)


image.show()