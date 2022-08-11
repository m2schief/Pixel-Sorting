import random
from PIL import Image, ImageCms
from Arrays import *
random.seed(139381512)

#create LAB transform
srgb_p = ImageCms.createProfile('sRGB')
lab_p = ImageCms.createProfile('LAB')
rgb2lab = ImageCms.buildTransformFromOpenProfiles(srgb_p, lab_p, 'RGB', 'LAB')
lab2rgb = ImageCms.buildTransformFromOpenProfiles(lab_p, srgb_p, 'LAB', 'RGB')

def PixelsToImage(imTake, imTo):
    '''
    Produces an image using the pixels in imTake that resembles the image imTo

        Parameters:
            imTake (image): image comprising of the pixels you want to use
            (must be of same size as imTo)

            imTo (image): image you want to replicate (must be of same size
            as imTake)
        
        Returns:
            image: image resembling imTo comprised solely of the pixels in
            imTake
    '''

    width, height = imTake.size
    size = width * height
    retIm = Image.new('RGB', (width, height))

    takeData = list(ImageCms.applyTransform(imTake, rgb2lab).getdata())
    toData = list(ImageCms.applyTransform(imTo, rgb2lab).getdata())

    #store original locations of imTo pixels before sorting
    for row in range(height):
        for col in range(width):
            toData[row*width + col] = [toData[row*width + col], (col, row)]
    
    #sort and retrieve both image data
    takeDatArray = ThreeArray(takeData, width, height, 1)
    takeDatArray.cuboidDimensions()
    takeDatArray.sorted(f1=lambda x: x[0], f2=lambda x: x[1]+x[2], 
    f3=lambda x: x[1] - x[2], simpleSort=False)
    takeData = takeDatArray.getData()

    toDatArray = ThreeArray(toData, width, height, 1)
    toDatArray.cuboidDimensions()
    toDatArray.sorted(f1=lambda x: x[0][0], f2=lambda x: x[0][1]+x[0][2], 
    f3=lambda x: x[0][1] - x[0][2], simpleSort=False)
    toData = toDatArray.getData()

    #place imTake pixels into corresponding imTo positions
    retData = [0] * size
    for pixel in range(size):
        retData[toData[pixel][1][1]*width + toData[pixel][1][0]] = takeData[pixel]
    retIm.putdata(retData)

    retIm.putdata(list(ImageCms.applyTransform(retIm, lab2rgb).getdata()))
    #reverse transformation back to RGB to be displayed properly

    return retIm

def RandomToImage(im):
    '''
    Produces an image comprised of randomly generated pixels arranged to
    resemble the given image

        Parameters:
            im (image): image to be recreated by random pixels
        
        Returns:
            image: image of same dimensions as supplied, comprised solely of
            generated pixels
    '''
    rIm = Image.new('RGB', im.size)
    rIm.putdata([(random.randrange(256), random.randrange(256), random.randrange(256))
     for i in range (im.size[0] * im.size[1])])

    return PixelsToImage(rIm, im)

if __name__ == "__main__":

    lorikeet = Image.open("lorikeet1000.jpg")
    landscapeGrey = Image.open("landscape1000.jpg")
    landscapeGreen = Image.open("landscape2.jpg")
    edinburgh = Image.open("edinburgh.jpg")
    color_spiral = Image.open("color_spiral.jpg")
    flowers = Image.open("flowers1000.jpg")

    rLorikeet = RandomToImage(lorikeet)
    rLorikeet = rLorikeet.save("Lorikeet_From_Random.jpg")

    rFlowers = RandomToImage(flowers)
    rFlowers = rFlowers.save("Flowers_From_Random.jpg")

    rEdinburgh = RandomToImage(edinburgh)
    rEdinburgh = rEdinburgh.save("Edinburgh_From_Random.jpg")

    landscape_combined = PixelsToImage(landscapeGreen, landscapeGrey)
    landscape_combined = landscape_combined.save("landscape1000_from_2.jpg")

    cSpiral_lorikeet = PixelsToImage(lorikeet, color_spiral)
    cSpiral_lorikeet = cSpiral_lorikeet.save("Color_Spiral_from_Lorikeet.jpg")

