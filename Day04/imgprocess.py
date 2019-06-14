from PIL import Image
import os

## Displays the rotated image
img_rotate = img.transpose(Image.ROTATE_90)
img_rotate.show()  

# Crop (Center) (size = 160(W), 204(H))
crop_im = img.crop(box=(160,240))
img.show()

#Thumbnail – Generate the thumbnail of the given image (size = 75, 75)
img.thumbnail((150, 100))
img.show()