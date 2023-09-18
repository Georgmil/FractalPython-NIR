from PIL import Image
  
# gde risuem
xstart = -2.0
xend = 1.0
ystart = -1.5
yend = 1.5
  
# maximalnoe kolichestvo prohodov
maxkol = 255 
  
# razmer fotografii
imgx = 500
imgy = 500
image = Image.new("RGB", (imgx, imgy))
  
for y in range(imgy):
    zy = y * (yend - ystart) / (imgy - 1)  + ystart
    for x in range(imgx):
        zx = x * (xend - xstart) / (imgx - 1)  + xstart
        z = zx + zy * 1j #complex
        c = z
        for i in range(maxkol):
            if abs(z) > 2.0: 
                break
            z = z * z + c
        image.putpixel((x, y), (i % 4 * 10, i % 8 * 32, i % 16 * 16)) # tsvet v kordinate x,y, tsvet v rgb
  
image.show()