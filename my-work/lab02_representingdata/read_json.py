# Program to read and manipulate JSON files.
# Author: Susan Collins

# 6. Copy this URL into browser and see the JSON it returns. 
# https://www.gov.uk/bank-holidays.json
#7. Write a program to print this JSON to the console.

import requests
URL = "https://www.gov.uk/bank-holidays.json"
response = requests.get(URL)
data = response.json()
# print (data)


# Is this JSON or a Dict object that is outputted?
# print(type(data))


# 8. Modify the program to only output the first holiday in northern ireland
territory = list(data.keys())[2]

output = data[territory]['events'][0]
print(output)
print(type(output))