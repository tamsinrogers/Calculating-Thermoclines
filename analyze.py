# Tamsin Rogers
# September 18, 2019
# CS 152 
# Project 3: Calculating Thermoclines
# Part 3 - write a program to compute statistics of a column of data
# Run the program from the Terminal by entering "python3 analyze.py"
# To compute statistics from hurricanes.csv, run the program from the Terminal by entering "python3 analyze.py hurricanes.csv 1"

import sys      #imports the sys package
import stats    #imports stats.py

"""This function computes the sum, mean, variance, min, and max statistics from the stats.py
program for the selected column of data from the specified file and prints the statistics
to the terminal.  The user enters values for filename and columnID in the command line."""
def main(filename, columnID):   #defines the main function with the parameters filename and columnID
    # assign to fp the result of opening the file hurricanes.csv for reading
    fp = open("hurricanes.csv", "r")
    # assign to line the first line of the data file
    line = fp.readline()
    # assign to headers the result of splitting the line using commas
    headers = line.split(",")
    # print headers
    print(headers)
    # assign to data an empty list
    data = []
    # assign to line the next line of the data file
    line = line = fp.readline()
    # while the length of line is greater than 0 
    while len(line) > 0:
        # assign to words the result of splitting the line using commas
        words = line.split(",")
        # append to data the second item in words (which index is that?)
        data.append(words[columnID])
        # assign to line the next line of the data file
        line = fp.readline()
    length=len(data)                    #sets length to the length of the data list
    thesum = stats.sum(data)            #sets thesum to the value of the sum() function from stats.py with the data list as its argument
    print("sum: ", thesum)              #prints the result with the label "sum:"
    themean = stats.mean(data)          #sets themean to the value of the mean() function from stats.py with the data list as its argument
    print("mean: ", themean)            #prints the result with the label "mean:"
    themin = stats.min(data)            #sets themin to the value of the min() function from stats.py with the data list as its argument
    print("min: ", themin)              #prints the result with the label "min:"
    themax = stats.max(data)            #sets themax to the value of the max() function from stats.py with the data list as its argument
    print("max: ", themax)              #prints the result with the label "max:"
    thevariance = stats.variance(data)  #sets thevariance to the value of the mean() function from stats.py with the data list as its argument
    print("variance: ", thevariance)    #prints the result with the label "variance:"
    # close the data file
    fp.close()
    #print(data)
    """Calling analyze.py with the hurricanes.csv file and column 1 produces the following statistics:
    sum:  103.0
	mean:  7.357142857142857
	min:  2.0
	max:  15.0
	variance:  12.554945054945055"""

if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2])) #takes a file name and a column ID from the command line as arguments