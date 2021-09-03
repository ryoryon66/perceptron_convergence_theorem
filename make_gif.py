from PIL import Image
import os

remove_images = False

images = []

for i in range(1,100):
    if not os.path.exists("classification"+str(i)+'.png'):
        break
    file_name ="classification"+str(i)+'.png'
    im = Image.open(file_name)
    images.append(im)

images[0].save('classification.gif', save_all=True, append_images=images[1:], loop=0, duration=250)
#print(os.path)

if remove_images is False:
    exit()

for i in range(100):
    if (os.path.exists("classification"+str(i)+".png")):
        print("deleted")
        os.remove("classification"+str(i)+".png")
print("created the gif")