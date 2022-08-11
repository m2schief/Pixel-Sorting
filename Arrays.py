import random
random.seed(139381512)


class TwoArray:
    '''
    A class storing numerical data to be interpreted in two dimensions
    
    Methods
    --
    getData():
        Returns the list of values.

    sorted(f1 = lambda x: x[0]+x[1], f2 = lambda x: x[1] - x[0]):
        Sorts data along the diagonals of the rectangle by the two
        given (optional) functions. Default sorts upper left to
        bottom right by the sum of the x and y values, and upper
        right to bottom left by difference between x and y.
    
    simpleSort(f1 = lambda x: x[1], f2 = lambda x: x[0]):
        Sorts data along the sides of the rectangles by the two given
        (optional) functions. Default sorts into rows by y values,
        then sorts rows by x values.
    
    squarewardDimensions():
        Sets dimensions to largest values that multiply to existing length.
        Improves sorting methods.
    '''

    def __init__(self, data, width, height):
        '''
        Constructs necessary attributes for the TwoArray object.

        Parameters
        --
        data: listof Tuple
            data to be stored in array. Must have length of width*height
        width: Int
            Size of rows of TwoArray
        height: Int
            Number of rows of TwoArray
        '''

        self.data = data
        self.w = width
        self.h = height
    
    def __str__(self):
        '''
        String representation of TwoArray. Prints new lines after each row.
        '''
        out = ""
        for y in range(self.h):
            for x in range(self.w):
                out += str(self.data[y * self.w + x])
            out += "\n"
        return out
    
    def getData(self):
        '''
        Retrieves the data attribute.
        '''
        return self.data
    
    def __groupData(self, sFunc = lambda x: x[1] - x[0]):
        '''
        Groups the data by the diagonals of the TwoArray for use exclusively
        in the diagonal sort method.

        Parameters
        --
        sFunc: Tuple function
            Function used to sort the diagonals. Default sorts based on the
            difference of the first and second tuple values.
        '''
        currentStart = 0
        newData = []
        for i in range(1, self.w + self.h):
            if (i > max(self.w, self.h)):
                i = -i + self.w + self.h
            elif (i > min(self.w, self.h)):
                i = min(self.w, self.h)
            
            splice = self.data[currentStart:currentStart+i]
            splice.sort(key=sFunc)
            newData.append(splice)
            currentStart += i
        self.data = newData

    def sorted(self, f1 = lambda x: x[0]+x[1], f2 = lambda x: x[1] - x[0]):
        '''
        Sorts the data by the diagonals.

        Parameters
        --
        f1: Tuple function
        Higher priority function. Data with lower results will end up closer
        to the top left of the graph. Default total of the first and second
        tuple values.

        f2: Tuple function
        Lower priority function. Meant to be related to f1. Results with lower
        results will end up closer to the top right of the graph. Default
        difference between first and second tuple values.
        '''
        self.data.sort(key= f1)
        
        self.__groupData(f2)
        newData = [0] * self.w * self.h

        for i in range(self.w + self.h - 1):
            diagLen = len(self.data[i])
            for j in range(diagLen):
                loc = i + j*(self.w-1)
                if i >= self.w:
                    loc += (self.w-1)*(i - self.w + 1)
                newData[loc] = self.data[i][j]
        
        self.data = newData

    def simpleSort(self, f1 = lambda x: x[1], f2 = lambda x: x[0]):
        '''
        'traditional' two-dimensional sort. First sorts all data by f1, then
        sorts the rows of the data by f2.

        f1: Tuple function
            Much higher priority function. Data with lower results will end
            up higher in the array. Default is the second value of the tuple.
        
        f2: Tuple function
            Much lower priority function. Data with lower results will end up
            further left in the array. Default is the first value of the tuple.
        '''
        self.data.sort(key = f1)
        newData = []
        for i in range(self.h):
            splice = self.data[i*self.w : i*self.w + self.w]
            splice.sort(key = f2)
            newData.append(splice)
        newData = [item for row in newData for item in row] #flatten
        
        self.data = newData
    
    def squarewardDimensions(self):
        '''
        Changes width and height of the TwoArray to be as close together while
        maintaining the same size. Benefits the sorting methods. If unequal,
        the lower value becomes the width.
        '''
        dimensions = IntoSquare(self.w * self.h)
        self.w = dimensions[0]
        self.h = dimensions[1]




class ThreeArray:
    '''
    A class storing numerical data to be interpreted in three dimensions
    
    Methods
    --
    getData():
        Returns the list of values.
    
    sorted(f1 = lambda x: x[2], f2 = lambda x: x[1], f3 = lambda x: x[0],
           simpleSort = True):
        Sorts data by three functions. Default sorts by third value of the
        tuple, followed by the second, then first values.
    
    cuboidDimensions():
        Sets dimensions to largest values that multiply to existing length.
        Improves sorting methods.
    '''

    def __init__(self, data, width, height, depth):
        '''
        Constructs necessary attributes for the ThreeArray object.

        Parameters
        --
        data: listof Tuple
            data to be stored in array. Must have length of width*height*depth
        width: Int
            Size of rows per face
        height: Int
            Number of rows per face
        depth: Int
            Number of faces
        '''

        self.data = data
        self.w = width
        self.h = height
        self.d = depth

        self.sa = width * height
    
    def __str__(self):
        '''
        String representation of ThreeArray. Prints each face separated by a
        new line.
        '''
        out = ""
        for z in range(self.d):
            for y in range(self.h):
                for x in range(self.w):
                    out += str(self.data[x + y * self.w + z * self.sa])
                out += "\n"
            out += "\n"
        return out
    
    def getData(self):
        '''
        Returns ThreeArray data unformatted.
        '''
        return self.data
    
    def sorted(self, f1 = lambda x: x[2], f2 = lambda x: x[1], f3 = lambda x: x[0], simpleSort = True):
        '''
        Sorts ThreeArray data by three different functions. Sorts in order
        of functions given (f1, followed by f2 then f3).

        Parameters
        --
        f1 (tuple function):
        Highest priority function. Sorts data into different faces based on
        the values returned by this function. Default is third tuple value.

        f2 (tuple function):
        Higher priority function. Sorts data into rows of the faces based on the
        values returned by this function. Default is the second tuple value.
        Gets even higher importance over f3 when simpleSort is set to True.

        f3 (tuple function):
        Lowest priority function. Sorts data within their rows based on the
        values returned by this function. Default is the first tuple value.

        simpleSort (bool):
        Determines if the values within the faces are sorted by the TwoArray
        simpleSort function as opposed to the more complicated sorted function.
        If set to false: f2 and f3 sort into diagonals instead of rows (see
        TwoArray sorted documentation). Default set to True.
        '''
        self.data.sort(key = f1)
        newData = []

        for i in range(self.d):
            splice = self.data[i*self.sa : i*self.sa + self.sa]
            splice = TwoArray(splice, self.w, self.h)
            
            if simpleSort:
                splice.simpleSort(f2, f3)
            else:
                splice.sorted(f2, f3)
            
            newData.append(splice.getData())
        newData = [item for slice in newData for item in slice] #flatten
        
        self.data = newData
    
    def cuboidDimensions(self):
        '''
        Sets width, height, and depth of array to be as close together as
        possible while still multiplying to the defined length.
        '''
        dimensions = TripletFactors(self.w * self.h * self.d)
        self.d = dimensions[0]
        self.h = dimensions[1]
        self.w = dimensions[2]
        self.sa = self.w * self.h


def IntoSquare(n):
    '''
    Returns a tuple of integers close in value that multiply to the given
    integer.

        Parameters:
            n (int): A positive integer
        
        Returns:
            (int, int): Tuple of integers who's product is n
    '''
    curr = int(n**(1/2))
    while (n % curr != 0): #worst case curr = n
        curr += 1
    return (curr, n // curr)


def TripletFactors(n):
    '''
    Returns a list of three integers close in value that multiply to the given
    integer.

        Parameters:
            n (int): A positive integer
        
        Returns:
            [int, int, int]: A list of integers who's product is n
    '''
    L = prime_factors(n)
    L.reverse()
    r = n ** (1/3)
    f = [1, 1, 1]

    for i in L:
        mult_done = False
        curr_ind = 0
        while (mult_done == False):
            if f[curr_ind] * i < r:
                f[curr_ind] *= i
                mult_done = True
            else:
                curr_ind += 1;
            
            if curr_ind == 3:
                index_min = min(range(len(f)), key=f.__getitem__)
                f[index_min] *= i
                mult_done = True
    return f

def prime_factors(n):
    '''
    Returns a list of prime factors of a given integer.

        Parameters:
            n (int): A positive integer
        
        Returns:
            listof(Int): The prime factors of n
    '''
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def dataDistance(data1, data2, size):
    '''
    Returns the 'distance' between two datasets of tuples of integers.

        Parameters:
            data1 (listof(tuplesof(Int))): First dataset

            data2 (listof(tuplesof(Int))): Second dataset

            size (int): The length of the datasets (as both should be the same)
        
        Returns:
            Float: Measure of distance between the values of the dataset using
            the square distance of the values
    '''
    totalDiff = 0
    for i in range(size):
        for j in range(len(data1[i])):
            totalDiff += (data1[i][j] - data2[i][j])**2
    return totalDiff**(1/2)

if __name__ == "__main__":
    testArray = [(random.randrange(256), random.randrange(256), random.randrange(256)) for i in range(30)]
    testArray = ThreeArray(testArray, 30, 1, 1)
    testArray.cuboidDimensions()
    testArray.sorted()
    print(testArray)