# Program to print out the dates of the bank holidays that happen in 
# Northern Ireland.
# Author: Susan Collins

import requests
URL = "https://www.gov.uk/bank-holidays.json"


response = requests.get(URL)
bank_hol_data = response.json()

# get exact format of key for Northern Ireland - the third key. 
# The keys() method returns a dict_keys object, so must cast it as a list in 
# order to use an index value
northern_ireland = list(bank_hol_data.keys())[2]

# Print out the dates of all the NI holidays
print("The dates of bank holidays in Northern Ireland, 2024-2028, are:")

# create dict to store counts of events per year
year_count = {}

for event in bank_hol_data[northern_ireland]['events']:

    calendar_date = event["date"]
    year = int(calendar_date[0:4])

    # increment the year counts
    if year in year_count:
        year_count[year] += 1
    else:
        year_count[year] = 1

    # print date    
    print(calendar_date)

# print the year counts
for key in year_count.keys():
    print (f"{northern_ireland} has {year_count[key]} bank holidays in {key}.")
print() #newline

####################################################################
# Assignment Part 2 - Modify the program to print the bank holidays 
# that are unique to northern Ireland

# Approach:
# Make a list of all the dates of bank holidays in England/Wales and Scotland.
# This list is unordered and contains duplicates.
# Then compare each NI bank hol to this list and print if unique.

# list of events outside NI
events_outside_NI = []

# For the first two territories, England/Wales and Scotland
# (Note: in Python 3, casting a dict as a list returns a list of keys, so can 
# avoid using the keys() method.
# Found at https://stackoverflow.com/a/18552025)
for territory in list(bank_hol_data)[0:2]:

    for event in bank_hol_data[territory]['events']:

        events_outside_NI.append(event["date"])


# Now compare the NI events to the list of events outside NI
print("The bank holidays that are unique to Northern Ireland, 2024-2028, are:")

for event in bank_hol_data[northern_ireland]['events']:

    if event["date"] not in events_outside_NI:
        print (event["date"], event["title"])

