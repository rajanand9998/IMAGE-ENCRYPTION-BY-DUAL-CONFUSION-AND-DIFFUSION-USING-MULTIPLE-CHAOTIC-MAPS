import cv2 as cv
import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np
import Chaotic_map as cm
import UACI_NPCR as un
from PIL import Image

# Accepting Image using it's path
#path = str(input('Enter path of the image\n'))
image = img.imread(r"C:\Users\Vardhu\Desktop\Mini Project\Images\Cameraman original.jpg")
#print(image.size)
# Displaying original image
plt.imshow(image)
plt.show()
# Storing the size of image in variables
height = image.shape[0]
width = image.shape[1]
print("Height:",height,"  Width:",width)
# Using lorenz_key function to generate 3 lists of keys
xkey, ykey, zkey = cm.lorenz_key(0.01, 0.02, 0.03, height*width)

# Initializing empty index lists to store index of pixels
xindex = []
yindex = []
# Initializing an empty image to store the encrypted image
encryptedImage = np.zeros(shape=[height, width, 3], dtype=np.uint8)
l = 0

# Populating xindex and yindex
for i in range(width):
    xindex.append(i)
for i in range(height):
    yindex.append(i)

# Re-arranging xindex and xkey to increase randomness
for i in range(width):
    for j in range(width):
        if xkey[i] > xkey[j]:
            xkey[i], xkey[j] = xkey[j], xkey[i]
            xindex[i], xindex[j] = xindex[j], xindex[i]
# Re-arranging yindex and ykey to increase randomness
for i in range(height):
    for j in range(height):
        if ykey[i] > ykey[j]:
            ykey[i], ykey[j] = ykey[j], ykey[i]
            yindex[i], yindex[j] = yindex[j], yindex[i]
# Shuffling original image's pixels and storing them in an empty image
for i in range(height):
    k = 0
    for j in range(width):
        encryptedImage[i][j] = image[yindex[k]][xindex[k]] 
        k += 1
# Displaying the shuffled image
plt.imshow(encryptedImage)
plt.show()

# Calling logistic_key and providing r value such that the keys are pseudo-random
# and generating a key for every pixel of the image
generatedKey = cm.logistic_key(0.01, 3.95, height*width) 
z = 0
# Substituting all the pixels in original image using XOR
for i in range(height):
    for j in range(width):
        encryptedImage[i, j] = encryptedImage[i, j].astype(int) ^ generatedKey[z]
        z += 1
# Displaying the intermediate encrypted image
plt.imshow(encryptedImage)
plt.show()
# Using lorenz_key function to generate 3 lists of keys
xkey1, ykey1, zkey1 = cm.lorenz_key(0.03, 0.02, 0.01, height*width)
# Initializing empty index lists to store index of pixels
xindex1 = []
yindex1 = []
# Initializing an empty image to store the encrypted image
encryptedImage2 = np.zeros(shape=[height, width, 3], dtype=np.uint8)
l = 0
# Populating xindex and yindex
for i in range(width):
    xindex1.append(i)
for i in range(height):
    yindex1.append(i)

# Re-arranging xindex and xkey to increase randomness
for i in range(width):
    for j in range(width):
        if xkey1[i] > xkey1[j]:
            xkey1[i], xkey1[j] = xkey1[j], xkey1[i]
            xindex1[i], xindex1[j] = xindex1[j], xindex1[i]
# Re-arranging yindex and ykey to increase randomness
for i in range(height):
    for j in range(height):
        if ykey1[i] > ykey1[j]:
            ykey1[i], ykey1[j] = ykey1[j], ykey1[i]
            yindex1[i], yindex1[j] = yindex1[j], yindex1[i]

# Shuffling encrypted image's pixels and storing them in another empty image
for i in range(height):
    k = 0
    for j in range(width):
        encryptedImage2[i][j] = encryptedImage[yindex1[k]][xindex1[k]] 
        k += 1
# Displaying the newly shuffled image
plt.imshow(encryptedImage2)
plt.show()

# Calling tent_key and providing r value such that the keys are pseudo-random
# and generating a key for every pixel of the image
generatedKey1 = cm.tent_key(0.01, 1.9, height*width) 
z = 0
# Substituting all the pixels in encrypted image using XOR
for i in range(height):
    for j in range(width):
        encryptedImage2[i, j] = encryptedImage2[i, j].astype(int) ^ generatedKey1[z]
        z += 1
# Displaying the final encrypted image
plt.imshow(encryptedImage2)
plt.show()
im = Image.fromarray(encryptedImage2)
im.save("encrypted image.jpeg")

# Start of decryption process
# Reversing the xor operation done using tent map
z=0
for i in range(height):
    for j in range(width):
        encryptedImage2[i, j] = encryptedImage2[i, j].astype(int) ^ generatedKey1[z]
        z += 1
# Displaying the intermediate decrypted image
plt.imshow(encryptedImage2)
plt.show()

# Reversal of second lorenze shuffling
for i in range(height):
    k = 0
    for j in range(width):
        encryptedImage[yindex1[k]][xindex1[k]] = encryptedImage2[i][j] 
        k += 1
# Displaying the reshuffled intermediate decrypted image
plt.imshow(encryptedImage)
plt.show()

z = 0
# Reversal of first xor operation done using logistic map
for i in range(height):
    for j in range(width):
        encryptedImage[i, j] = encryptedImage[i, j].astype(int) ^ generatedKey[z]
        z += 1
# Displaying the intermediate decrypted image
plt.imshow(encryptedImage)
plt.show()

# Reversing the initial shuffling done using lorenze attractor
imagel = np.zeros(shape=[height, width, 3], dtype=np.uint8)
for i in range(height):
    k = 0
    for j in range(width):
        imagel[yindex[k]][xindex[k]] = encryptedImage[i][j]
        k += 1
# Displaying final decrypted image
plt.imshow(image)
plt.show()
im = Image.fromarray(image)
im.save("decrypted image.jpeg")
#Showing Histograms of original intermediate and final image
hist=cv.calcHist([image], [0], None, [512], [0,512])
plt.plot(hist)
plt.show()

hist1=cv.calcHist([encryptedImage], [0], None, [512], [0,512])
plt.plot(hist1)
plt.show()

hist2=cv.calcHist([encryptedImage2], [0], None, [512], [0,512])
plt.plot(hist2)
plt.show()

#Showing UACI and NPCR values
UACI=un.uaci(height,width)
NPCR=un.npcrv(height,width)
print("UACI:",UACI," \nNPCR:",NPCR)