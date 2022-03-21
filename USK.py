from PIL import Image

# Opening the primary image (used in background)
img1 = Image.open("1.jpg")
width0, height = img1.size
# Opening the secondary image (overlay image)
img2 = Image.open("6.png")
width1, height1 = img2.size

# Pasting img2 image on top of img1
# starting at coordinates (0, 0)
img1.paste(img2,(0, height - height1))


# Displaying the image
img1.show()
