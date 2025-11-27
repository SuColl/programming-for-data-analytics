# Program to read and manipulate sample CSV files.
# Author: Susan Collins

FILENAME = "data.csv"

import csv

# Write a program to read in the data and output each line as a list.
# 3. Modify the program to deal with the header line separately
# 4. Modify the program to calculate the average age
with open(FILENAME, "rt") as file:
    reader = csv.reader(file, delimiter = ",")
    
    linecount = 0
    sum_ages = 0
    for line in reader:
        if linecount == 0:
            print(f"-------->{line}<----------")
        else:
            print(line)
            sum_ages += int(line[1])
        linecount += 1
        

n_entries = linecount-1

print (f"VERSION 01") 
print (f"{n_entries} entries, total age {sum_ages},",
    f"average age {sum_ages/n_entries:.2f}\n\n")


# 5. The CVS file could of course have been read in as a Dictionary object
print (f"VERSION 02")

with open(FILENAME, "rt") as file:
    reader = csv.DictReader(file, delimiter="," , quoting=csv.QUOTE_NONNUMERIC) 
    total = 0
    count = 0
    for line in reader:
        total += line['age']
        print (line)
        count +=1


print (f"average is {total/(count)}") # 
