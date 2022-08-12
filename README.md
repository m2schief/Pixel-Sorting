The following is a simple python project done primarily to demonstrate a degree of coding knowledge and problem-solving.

# Pixel-Sorting

### TwoArray

The TwoArray class is found in the Arrays.py file. It takes a list of tuples of length two, a width, and a height.  
The provided methods are related to the interpretation of the data as a two-dimensional array. The TwoArray can be outputed to demonstrate this:  
![TwoArray Data](/README_Images/TwoArray_PreSort.png)

The sorting methods for the array are based off the interpretation that the first value of the tuple corresponds to the x-axis, and the second value corresponds to the y-axis. Here is the above array sorted (same output for both methods):  
![TwoArray Data Sorted](/README_Images/TwoArray_PostSort.png)

###### Simple Sort

The first sorting method is done in the simplest way. The array is first sorted solely by y-values, and then subsequently sorts the rows by x-values.  
![Randomly Generated TwoArray Data](/README_Images/TwoArray_Demo0.png)  
-  
![Above Data Sorted Into Rows](/README_Images/TwoArray_Demo1.png)  
-  
![Above Data with Rows Sorted](/README_Images/TwoArray_Demo2.png)


##### Diagonal Sort

You'll notice that the lowest sum of values isn't always found in the top-left corner, as would be expected. This motivates the following sorting method, titled simply "sort" in the code. The array is first sorted solely by the total value of x and y, putting the lowest sum in the top left and the highest sum in the bottom right. The values are then separated based on which diagonal they would appear on, based on their xy sum. These diagonals are then sorted by the difference between the y and x values, to determine how far along the diagonal they should go. Here is the same array as above sorted using this method:  
![Above Data Sorted through a Different Method](/README_Images/TwoArray_DemoDiag.png)

##### Squareward Dimensions

Finding a width and height closer in value benefit the sorting methods by reducing the relative importance of the first sorting function used. The same idea applies to the third-dimension and the method 'Cuboid Dimensions'.

### ThreeArray

The ThreeArray class is found in the Arrays.py file. It takes a list of tuples of length three, a width, a height, and a depth.  
The ThreeArray is the natural extension of the TwoArray, treating the data as a 3d object:  

Again, here is a sorting demonstration:  
![ThreeArray Data](/README_Images/ThreeArray_PreSort.png)  
-  
![ThreeArray Data Sorted](/README_Images/ThreeArray_PostSort.png)

##### Three-Dimensional Sorting

Sorting such an array is done much the same as before. For the diagonal sort, the process is only done with the final two values of the tuple. This keeps some of the flaws of the 'simple sort', as the first value of the tuple thus has priority in the overall placement. This can be a future improvement, though would involve a more complicated equation for not much of a difference.

### Comparison of Sorting Methods

Determining the better sorting method was done by sorting the pixels of an image, sorting an equal-sized list of random pixels, and summing the distance between each image pixel and its corresponding random pixel. When done with the Lorikeet image, the SimpleSort method had a distance of 137324, while the Diagonal Sort method had a distance of 134542. Consistently, with other images as well, sorting along the diagonals gave better results.

### Application and Use with Images

These methods allow for the sorting of items based on multiple values, as opposed to simply one. In particular, this gives useful comparisons between groups of items when they are sorted, as is shown in the above section on comparing sorting methods.  
It also allows us to create a mapping of pixels from one image to another.  
The following results use LAB pixel values as opposed to RGB, as this creates less of a difference in importance between the values in the tuple (for example, the blue component of an RGB pixel has a much larger effect on the overall pixel than the green component, as blue is a darker, more prominant colour).  
Once the image pixels and random pixels are sorted based on each of the LAB components, we can place each random pixel into the original location of its corresponding image pixel. We get the following results, with the original image next to the image comprised entirely of random pixels. 
![Image of a Lorikeet](/lorikeet1000.jpg)  
![Lorikeet Image Created from Randomly Generated Pixels](/Lorikeet_From_Random.bmp)

We can do the same with non-random images. Taking the pixels from one image and placing them in a configuration resembling another image. Example below.
![Image of a lush Landscape](/landscape2.jpg)  
![Image of a low saturation Landscape](/landscape1000.jpg)  
![Above Landscape made out Pixels from Lush Landscape](/landscape1000_from_2.bmp)