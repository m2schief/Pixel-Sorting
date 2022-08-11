The following is a simple python project done primarily to demonstrate a degree of coding knowledge and problem-solving.

# Pixel-Sorting

### TwoArray

The TwoArray class is found in the Arrays.py file. It takes a list of tuples of length two, a width, and a height.  
The provided methods are related to the interpretation of the data as a two-dimensional array. The TwoArray can be outputed to demonstrate this:

The sorting methods for the array are based off the interpretation that the first value of the tuple corresponds to the x-axis, and the second value corresponds to the y-axis. Here is the above array sorted (same output for both methods):

###### Simple Sort

The first sorting method is done in the simplest way. The array is first sorted solely by y-values, and then subsequently sorts the rows by x-values.


##### Diagonal Sort

You'll notice that the lowest sum of values isn't always found in the top-left corner, as would be expected. This motivates the following sorting method, titled simply "sort" in the code. The array is first sorted solely by the total value of x and y, putting the lowest sum in the top left and the highest sum in the bottom right. The values are then separated based on which diagonal they would appear on, based on their xy sum. These diagonals are then sorted by 
