# program to take the csv files with an RTK point at line 1 and delete line 1
# then save as a new file with the addition of "edit" at the end

import csv

# need to get input for the filename... and directory eventually
file_name = open(input("Enter the file name- "))
save_as = open("CSV-EDIT", "w")

writer = csv.writer(save_as)

for row in csv.reader(file_name):

    if not "RTCM" in row[0]: # if it contains
        writer.writerow(row) # write all other lines
