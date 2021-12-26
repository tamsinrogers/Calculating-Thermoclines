# Tamsin Rogers
# September 18, 2019
# CS 152 
# Project 3: Calculating Thermoclines
# Parts 1&2 - write a library of useful statistical functions
# Run the program from the Terminal by entering "python3 stats.py"

#creates a list 'data' and fills it with the digits from 0-10
data = [0,1,2,3,4,5,6,7,8,9,10]
#mean=5.5, min=1, max=10
#sets the variable length to the length of the data list
length = (len(data))

"""This function will compute the sum of the list of data from the parameter 'data', which 
is the list of numbers.  This function begins by initializing the variable thesum to 0.0.
The function then runs a for loop, which operates by adding each value in the list to 'thesum'.
As a result, the value that will be returned as thesum is the total of all of the values in
the list added together."""
def sum(data):
    thesum = 0.0            #initializes thesum to 0.0
    for i in data:          #runs a for loop for each value in the list
        i = float(i)        #casts each i value to a float
        thesum = thesum+i   #adds each value in the list to thesum
    return thesum           #returns the sum of all values in the list

#def test():
#   first = [1,2,3,4]
#   second = sum(first)
    #print(second)

"""This function will compute the mean of the list of data from the parameter 'data', which 
is the list of numbers.  This function begins by initializing the variable sum to 0.0.
The function then runs a for loop, which operates by adding each value in the list to 'sum'.
Then, the variable length is set to the value of the length of the list, and the variable 
average is set to the result of sum/length.  As a result, the value that will be returned 
as average is the mean of all of the values in the list."""
def mean(data):
    sum = 0.0               #initializes sum to 0.0
    for i in data:          #runs a for loop for each value in the list
        i = float(i)        #casts each i value to a float
        sum = sum+i         #adds each value in the list to sum
    length=len(data)        #sets the variable length to the length of the data list
    average = sum/length    #sets the variable average to the value of sum/length
    return average          #returns the mean of the values in the list

"""This function will compute the minimum value of the list of data from the parameter 
'data', which is the list of numbers.  This function begins by initializing the variable 
minimum to a large positive integer.  The function then runs a for loop, which operates by 
checking each value in the list to see if it is less than the current minimum value.  If 
a value is less than the current minimum, that value is set to minimum.  As a result, the 
value that will be returned as minimum is the minimum of all of the values in the list."""
def min(data):
    minimum = 10000000000   #initializes minimum to a large positive integer
    for i in data:          #runs a for loop for each value in the list
        i = float(i)        #casts each i value to a float
        if i<minimum:       #if the given i value in the list is less than the value of minimum
            minimum=i       #set the new minimum value to the value of i
    return minimum          #returns the minimum of the values in the list

"""This function will compute the maximum value of the list of data from the parameter 
'data', which is the list of numbers.  This function begins by initializing the variable 
maximum to a large negative integer.  The function then runs a for loop, which operates by 
checking each value in the list to see if it is greater than the current maximum value.  If 
a value is greater than the current maximum, that value is set to maximum.  As a result, the 
value that will be returned as maximum is the maximum of all of the values in the list."""
def max(data):
    maximum = -10000000000  #initializes maximum to a large negative integer
    for i in data:          #runs a for loop for each value in the list
        i = float(i)        #casts each i value to a float
        if i>maximum:       #if the given i value in the list is greater than the value of maximum
            maximum=i       #set the new maximum value to the value of i
    return maximum          #returns the maximum of the values in the list

"""This function will compute the variance of the list of data from the parameter 'data', which 
is the list of numbers.  This function begins by initializing the variable var to an empty
list.  The function then runs a for loop, which operates by appending the sum of the squared
differences between each data point and the mean using a for loop, and dividing this value by
the length of the list var - 1.  As a result, the value that will be returned is the variance
of the values in the list."""
def variance(data):
    var = []                            #initializes var to an empty list
    for i in data:                      #runs a for loop for each value in the list
        i = float(i)                    #casts each i value to a float
        var.append((i-mean(data))**2)   #appends the value of the squared differences between each data point and the mean to var
    sumvar = sum(var)                   #computes the sum of the squared differences
    lengthvar = len(var)                #sets lengthvar to the length of the list var
    test = lengthvar-1                  #sets test to the value of lengthvar-1
    finalvariance = sumvar/test         #sets finalvariance to the value of sumvar/test
    return(finalvariance)               #returns the variance of the values in the list

"""This function tests the above functions with the a list of data containing the integers
0-10."""
def test():
    data = [0,1,2,3,4,5,6,7,8,9,10]
    thesum = sum(data)                  #sets thesum to the value of the sum() function with the data list as its argument
    print("sum: ", thesum)              #prints the result with the label "sum:"
    themean = mean(data)                #sets themean to the value of the mean() function with the data list as its argument
    print("mean: ", themean)            #prints the result with the label "mean:"
    themin = min(data)                  #sets themin to the value of the min() function with the data list as its argument
    print("min: ", themin)              #prints the result with the label "min:"
    themax = max(data)                  #sets themax to the value of the max() function with the data list as its argument
    print("max: ", themax)              #prints the result with the label "max:"
    thevariance = variance(data)        #sets thevariance to the value of the variance() function with the data list as its argument
    print("variance: ", thevariance)    #prints the result with the label "variance:"
    
if __name__ == "__main__":
    test()