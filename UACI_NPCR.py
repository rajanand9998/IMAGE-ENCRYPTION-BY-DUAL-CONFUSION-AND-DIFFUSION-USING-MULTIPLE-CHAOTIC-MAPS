from PIL import Image
import math
import numpy as np

#UACI (Unified Average Changing Intensity)
def uaci(height,width):
    image1 = Image.open(r"C:\Users\Vardhu\Desktop\Mini Project\Images\Cameraman original.jpeg")
    image2 = Image.open(r"C:\Users\Vardhu\Desktop\Mini Project\encrypted image.jpeg")
    pixel1=image1.load()
    pixel2=image2.load()
    width,height=image1.size
    value=0.0
    for y in range(0,height):
        for x in range(0,width):
            #value+=(abs(int(image1[x,y])-int(image2[x,y])))
            value=(abs(pixel1[x,y][0]-pixel2[x,y][0])/255)+value
    
    value=(value/(width*height))*100
    #value=value*100/(width*height*511)
    return value


#NPCR (Number of Pixel Changed Rate)
#This method compares two image.If the pixel value is same then 0 is stored in the matrix else one is stored
def rateofchange(height,width,pixel1,pixel2,matrix,i):
    for y in range(0,height):
        for x in range(0,width):
            if pixel1[x,y][i] == pixel2[x,y][i]:
                matrix[x,y]=0
            else:
                matrix[x,y]=1
    return matrix

#sum of the values of 1 stored in matrix is calculated
def sumofpixel(height,width,pixel1,pixel2,ematrix,i):
    matrix=rateofchange(height,width,pixel1,pixel2,ematrix,i)
    psum=0
    for y in range(0,height):
        for x in range(0,width):
            psum=matrix[x,y]+psum
    return psum

#Finally the above two module is called to calculate the values
def npcrv(height,width):
    c1 = Image.open(r"C:\Users\Vardhu\Desktop\Mini Project\Images\Cameraman original.jpg")
    c2 = Image.open(r"C:\Users\Vardhu\Desktop\Mini Project\decrypted image.jpeg")
    pixel1 = c1.load()
    pixel2 = c2.load()
    ematrix = np.empty([width, height])
    per=100-(((sumofpixel(height,width,pixel1,pixel2,ematrix,0)/(height*width))*100)+((sumofpixel(height,width,pixel1,pixel2,ematrix,1)/(height*width))*100)+((sumofpixel(height,width,pixel1,pixel2,ematrix,2)/(height*width))*100))/30
    #per = ((sumofpixel))
    return per