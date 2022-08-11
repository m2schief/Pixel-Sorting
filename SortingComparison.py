import random
from PIL import Image, ImageCms
from Arrays import *
random.seed(139381512)


#create LAB transform
srgb_p = ImageCms.createProfile('sRGB')
lab_p = ImageCms.createProfile('LAB')
rgb2lab = ImageCms.buildTransformFromOpenProfiles(srgb_p, lab_p, 'RGB', 'LAB')


#Open Image
im = Image.open(fp="lorikeet1000.jpg")
width, height = im.size
imData = list(ImageCms.applyTransform(im, rgb2lab).getdata())


#Create image of random pixels
rData = [(random.randrange(256), random.randrange(256), random.randrange(256))
          for i in range(width * height)]
rIm = Image.new('RGB', (width, height))
rIm.putdata(rData)
rData = list(ImageCms.applyTransform(rIm, rgb2lab).getdata())


#random pixels sorted different ways
rDataSimple = ThreeArray(rData, width, height, 1)
rDataSimple.cuboidDimensions()
rDataSimple.sorted()
rDataSimple = rDataSimple.getData()

rDataDiag = ThreeArray(rData, width, height, 1)
rDataDiag.cuboidDimensions()
rDataDiag.sorted(f1= lambda x: x[2], f2=lambda x: x[0] + x[1], f3=lambda x: x[0] - x[1], simpleSort=False)
rDataDiag = rDataDiag.getData()

print(dataDistance(rDataSimple, rDataDiag, len(rData))) #90985


#Image Data and Comparison
imDataSimple = ThreeArray(imData, width, height, 1)
imDataSimple.cuboidDimensions()
imDataSimple.sorted()
imDataSimple = imDataSimple.getData()
print(dataDistance(rDataSimple, imDataSimple, len(imData))) #89553

imDataDiag = ThreeArray(imData, width, height, 1)
imDataDiag.cuboidDimensions()
imDataDiag.sorted(f1= lambda x: x[2], f2=lambda x: x[0] + x[1], f3=lambda x: x[0] - x[1], simpleSort=False)
imDataDiag = imDataDiag.getData()
print(dataDistance(rDataDiag, imDataDiag, len(imData))) #87824