#Tamsin Rogers
#September 18, 2019
#CS152
#Project3
#part 4 - compute the thermocline


def density(temps):
        rhos = []
        for t in temps:
            rho = 1000 * (1 - (t + 288.9414) * (t - 3.9863)**2 / (508929.2*(t + 68.12963)))
            rhos.append(rho)
        return(rhos)

def thermocline_depth( temps, depths ):
    # assign to rhos the result of calling the density function with temps as the argument
    rhos = density(temps)
    n = len(rhos)
    newrhos = n-1
    #i = int(n-1)
    # assign to drho_dz the empty list
    drho_dz = []
    # loop for one less than the length of rhos
    for i in range(newrhos):
        # append to drho_dz  the quantity rhos[i+1] minus rhos[i] divided by the quantity depths[i+1] minus depths[i]
        drho_dz.append((rhos[(i+1)]-rhos[i])/(depths[(i+1)]-depths[i]))
        # optional step: print out temps[i], rhos[i], and drho_dz[i]
        print("temps", temps[i], "rhos", rhos[i], "drho_dz", drho_dz[i])
    # assign to max_drho_dz the value -1.0
    max_drho_dz = -1.0
    # assign the maxindex the value -1
    maxindex = -1
    # loop for the length of drho_dz (loop variable i)
    for i in range(len(drho_dz)):
        i = int(i)
        # if drho_dz[i] is greater than max_drho_dz
        if drho_dz[i] > max_drho_dz:
            # assign to max_drho_dz the value drho_dz[i]
            max_drho_dz = drho_dz[i]
            # assign to maxindex the value i
            maxindex=i
                

    # assign to thermoDepth the average of depths[maxindex] and depths[maxindex+1]
    thermoDepth = (depths[maxindex]+depths[maxindex+1])/2 
    return thermoDepth

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
    fp2.write("Date" + "," + "Depth" + "\n")    #writes headers for date/time and depth onto goldiethermocline.csv
    line = fp.readline()
    fp3 = open( '12am.csv', 'w' )
    #writes the new file 12am.csv
    fp3.write("Date" + "," + "Depth" + "\n")    #writes headers for date/time and depth onto 12am.csv
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
        time = "12:03:00 PM"
        # if the time is about midnight (12:03:00 AM)
        midnight = "12:03:00 AM"
        date = words[0]#assigns the values in the first column of data to the variable datetime
        line = fp.readline()
        
        
        if time in date:#checks to see if the time 12:03 is contained in the original data set,
            # add one to the day variable
            day = day+1
            # assign to temps the empty list
            temps = []
            # loop over the number of items in depths (loop variable i)
            for i in range(len(depths)):
                # append to temps the result of casting words[ fields[i] ] to a float
                temps.append(float(words[fields[i]]))
            # assign to thermo_depth the result of calling thermocline_depth with temps and depths as arguments
            thermo_depth = thermocline_depth(temps, depths)
            # print (or save to a file) the day of the month and thermo_depth separated by a comma
            fp2.write(date + "," + str(thermo_depth) + "\n")
        # update line with readline
        line = fp.readline()
        
        if midnight in date:#checks to see if the time 12:03 is contained in the original data set,
            # add one to the day variable
            day = day+1
            # assign to temps the empty list
            temps = []
            # loop over the number of items in depths (loop variable i)
            for i in range(len(depths)):
                # append to temps the result of casting words[ fields[i] ] to a float
                temps.append(float(words[fields[i]]))
            # assign to thermo_depth the result of calling thermocline_depth with temps and depths as arguments
            thermo_depth = thermocline_depth(temps, depths)
            # print (or save to a file) the day of the month and thermo_depth separated by a comma
            fp3.write(date + "," + str(thermo_depth) + "\n")
        # update line with readline
        line = fp.readline()
    return

if __name__ == "__main__":
    main()