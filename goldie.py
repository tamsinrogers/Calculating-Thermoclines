import thermocline

def main():


    # these are the fields corresponding to the temperatures in order by depth
    # note they use 0-indexing 
    fields = [10, 11, 16, 17, 15, 14, 13, 12]

    # these are the depth values for each temperature measurement
    depths = [ 1, 3, 5, 7, 9, 11, 13, 15 ]

    # open the data file and read past the header line
    fp = open( "GoldieJuly2019.csv", "r" )
    fp2 = open( 'goldiethermocline.csv', 'w' )
    #writes the new file goldiethermocline.csv
    fp2.write("Date/Time" + "," + "Depth" + "\n")	#writes headers for date/time and depth onto goldiethermocline.csv
    line = fp.readline()
    # assign to day the value 0
    day = 0

    # read the first data line
    line = fp.readline()
    # start a while loop while there is still data
    while len(line) > 0:
        # split the line on commas and assign it to words
        words = line.split(",")
        # if the time is about noon (12:03:00 PM)
        time = "12:03"
        datetime = words[0]#assigns the values in the first column of data to the variable datetime
        line = fp.readline()
        
        if time in datetime:#checks to see if the time 12:03 is contained in the original data set,
            # add one to the day variable
            day = day+1
            # assign to temps the empty list
            temps = []
            # loop over the number of items in depths (loop variable i)
            for i in range(len(depths)):
                # append to temps the result of casting words[ fields[i] ] to a float
                temps.append(float(words[fields[i]]))
            # assign to thermo_depth the result of calling thermocline_depth with temps and depths as arguments
            thermodepth = thermocline_depth(temps, depths)
            # print (or save to a file) the day of the month and thermo_depth separated by a comma
            fp2.write(datetime + "," + str(thermo_depth) + "\n")
        # update line with readline
        line = fp.readline()
    return

if __name__ == "__main__":
    main()