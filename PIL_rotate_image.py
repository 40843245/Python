#import module
from PIL import Image
#path of img.
img_path='NFU_Logo.png'
#img_path=r'C:\Users\jayw7\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Anaconda3 (32-bit)'
im=Image.open(img_path)
#print the info about the image
print(im.format,im.size,im.mode)
#show it
im.show()
print("the img is shown successfully.")
rotated_im=im.rotate(180)
rotated_im.show()