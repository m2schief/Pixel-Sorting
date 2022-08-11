import random
from PIL import Image, ImageCms
from Arrays import *
random.seed(139381512)


#Open Image
im = Image.open(fp="lorikeet1000.jpg")
width, height = im.size
imData = list(im.getdata())


#Create data array of random pixels
rData = [(random.randrange(256), random.randrange(256), random.randrange(256))
          for i in range(width * height)]


#random pixels sorted different ways
rDataSimple = ThreeArray(rData, width, height, 1)
rDataSimple.cuboidDimensions()
rDataSimple.sorted()
rDataSimple = rDataSimple.getData()

rDataDiag = ThreeArray(rData, width, height, 1)
rDataDiag.cuboidDimensions()
rDataDiag.sorted(f1= lambda x: x[2], f2=lambda x: x[0] + x[1], f3=lambda x: x[1] - x[0], simpleSort=False)
rDataDiag = rDataDiag.getData()

print(dataDistance(rDataSimple, rDataDiag, len(rData))) #15986


#Image Data and Comparison
imDataSimple = ThreeArray(imData, width, height, 1)
imDataSimple.cuboidDimensions()
imDataSimple.sorted()
imDataSimple = imDataSimple.getData()
print(dataDistance(rDataSimple, imDataSimple, len(imData))) #137324

imDataDiag = ThreeArray(imData, width, height, 1)
imDataDiag.cuboidDimensions()
imDataDiag.sorted(f1= lambda x: x[2], f2=lambda x: x[0] + x[1], f3=lambda x: x[1] - x[0], simpleSort=False)
imDataDiag = imDataDiag.getData()
print(dataDistance(rDataDiag, imDataDiag, len(imData))) #134526