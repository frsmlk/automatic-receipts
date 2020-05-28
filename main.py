from PIL import Image,ImageDraw,ImageFont
import csv
import math
from datetime import datetime

font_league_spartan = ImageFont.truetype('fonts/LeagueSpartan-Bold.otf', 40 )
font_kollekif = ImageFont.truetype('fonts/Kollektif.ttf', 29)
font_kollekif_bold = ImageFont.truetype('fonts/Kollektif-Bold.ttf', 29)
font_arimo = ImageFont.truetype('fonts/Arimo-Italic.ttf', 25)


d = open('stripe.csv')
d_read = csv.reader(d)
next(d_read,None)
data = list(d_read)

# for i in data:
    # datetime_str = i[7].split(" ")[:-1]
    # datetime_str = ' '.join(datetime_str)
    # datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
    # print(datetime_object.strftime('%d %m %Y'))


# image_wdp = Image.open('assets/wdp.png')
# draw= ImageDraw.Draw(image_wdp)
# draw.text(xy=(990,380),text=f"02 02 2020 - {'1'.zfill(3)}", fill=(135,135,133),font=font_kollekif)
# image_wdp.show()


#             image_wdp = Image.open('assets/wdp.png')

# draw = ImageDraw.Draw(image_wdp)
# draw.text(xy=(191,545), text=(f"{i[1].upper()}"),fill=(83,143,147), font=font_league_spartan)
# draw.text(xy=(195,829), text=(f"{rounded/10}" ),fill=(111,111,110),font=font_kollekif)
# draw.text(xy=(1085,829), text=(f"RM {rounded}"),fill=(111,111,110),font=font_kollekif)
# draw.text(xy=(1085,1131.5), text=(f"RM {rounded}" ),fill=(111,111,110),font=font_kollekif_bold)
# draw.text(xy=(730,1296), text=(f"CONTRIBUTOR"), fill=(111,111,110),font=font_arimo)
# image_wdp.save(f"receipts/receipt_{i[1].upper().split(' ')[0]}.png")

def roundup(x):
    return int(math.ceil(float(x) / 10.0)) * 10

def receipts(array):

    count = 0


    for i in array:

        count += 1

        
       
        rounded = int(roundup(i[6]))

        if i[9] == "Weekly Delivery" or i[9] == "":

            datetime_str = i[7].split(" ")[:-1]
            datetime_str = ' '.join(datetime_str)
            datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
            date = datetime_object.strftime('%d %m %Y')
            
            image_wdp = Image.open('assets/wdp.png')

            draw = ImageDraw.Draw(image_wdp)
            draw.text(xy=(191,545), text=(f"{i[1].upper()}"),fill=(83,143,147), font=font_league_spartan)
            draw.text(xy=(195,829), text=(f"{int(rounded/10)}" ),fill=(111,111,110),font=font_kollekif)
            draw.text(xy=(1085,829), text=(f"RM {rounded}"),fill=(111,111,110),font=font_kollekif)
            draw.text(xy=(1085,1131.5), text=(f"RM {rounded}" ),fill=(111,111,110),font=font_kollekif_bold)
            draw.text(xy=(730,1296), text=(f"CONTRIBUTOR"), fill=(111,111,110),font=font_arimo)
            draw.text(xy=(990,380),text=f"{date} - {str(count).zfill(3)}", fill=(135,135,133),font=font_kollekif)
            image_wdp.save(f"receipts/receipt_{i[1].upper().split(' ')[0]}.png")

        if i[9] == "Care Package":

            datetime_str = i[7].split(" ")[:-1]
            datetime_str = ' '.join(datetime_str)
            datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
            date = datetime_object.strftime('%d %m %Y')

            image_cpp = Image.open('assets/cpp.png')

            draw = ImageDraw.Draw(image_cpp)
            draw.text(xy=(191,545), text=(f"{i[1].upper()}"),fill=(83,143,147), font=font_league_spartan)
            draw.text(xy=(195,829), text=(f"{round((rounded/150),1)}" ),fill=(111,111,110),font=font_kollekif)
            draw.text(xy=(1085,829), text=(f"RM {rounded}" ),fill=(111,111,110),font=font_kollekif)
            draw.text(xy=(1085,1131.5), text=(f"RM {rounded}" ),fill=(111,111,110),font=font_kollekif_bold)
            draw.text(xy=(730,1296), text=(f"CONTRIBUTOR"), fill=(111,111,110),font=font_arimo)
            draw.text(xy=(990,380),text=f"{date} - {str(count).zfill(3)}", fill=(135,135,133),font=font_kollekif)
            image_cpp.save(f"receipts/receipt_{i[1].upper().split(' ')[0]}.png")



    return

receipts(data)


# draw = ImageDraw.Draw(image_wdp)
# draw.text(xy=(191,545), text="FARIS MALIK",fill=(83,143,147), font=font_league_spartan)
# draw.text(xy=(195,829), text=str(4), fill=(111,111,110),font=font_kollekif)
# draw.text(xy=(1085,829), text="RM 400", fill=(111,111,110),font=font_kollekif)
# draw.text(xy=(1085,1131.5), text="RM 400", fill=(111,111,110),font=font_kollekif_bold)
# draw.text(xy=(730,1296), text="FARIS,", fill=(111,111,110),font=font_arimo)


# image_wdp.show()