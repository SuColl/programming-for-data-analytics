# Programming for Data Analytics - Assignments
author: Susan Collins

Description of this repository:  
A collection of assignments  for the Programming for Data Analytics  Module, part of the Higher Diploma in Data Analytics, at Atlantic Technological University, Ireland, Autumn 2025.

 Developed using [python](https://www.python.org/) v3.12.7  

----------------------------------------------------------------------
## Assignment 02: assignment02-bankholidays.py
This program prints out the dates of the bank holidays that happen in Northern Ireland 2024-2028, taken from https://www.gov.uk/bank-holidays.json.

It then prints the number of bank holidays in each calendar year, and then prints the bank holidays that are unique to Northern Ireland within the UK.


### Expected Output
```
$ python assignment02-bankholidays.py
The dates of bank holidays in Northern Ireland, 2024-2028, are:
2024-01-01
2024-03-18
2024-03-29
[...]
2028-08-28
2028-12-25
2028-12-26
northern-ireland has 10 bank holidays in 2024.
northern-ireland has 10 bank holidays in 2025.
northern-ireland has 10 bank holidays in 2026.
northern-ireland has 10 bank holidays in 2027.
northern-ireland has 10 bank holidays in 2028.

The bank holidays that are unique to Northern Ireland, 2024-2028, are:
2024-03-18 St Patrick’s Day
2024-07-12 Battle of the Boyne (Orangemen’s Day)
2025-03-17 St Patrick’s Day
2025-07-14 Battle of the Boyne (Orangemen’s Day)
2026-03-17 St Patrick’s Day
2026-07-13 Battle of the Boyne (Orangemen’s Day)
2027-03-17 St Patrick’s Day
2027-07-12 Battle of the Boyne (Orangemen’s Day)
2028-03-17 St Patrick’s Day
2028-07-12 Battle of the Boyne (Orangemen’s Day)
```

----------------------------------------------------------------------
## Assignment 03: assignment03-pie.ipynb
This note book creates a pie chart of  email domains in the csv file at the url:
https://drive.google.com/uc?id=1AWPf-pJodJKeHsARQK_RHiNsE8fjPCVK&export=download

----------------------------------------------------------------------
## Assignment 05: assignment05-population.ipynb
This notebook analyses some differences between the sexes by age in Ireland, based on 2022 Census data. 
it:
- Calculates the weighted mean age by sex,
- Analyses the difference between the sexes by age
- Calculates the population difference between the sexes in a user-specified age group.
- Calculates which region in Ireland has the biggest population difference between the sexes in that age group.

----------------------------------------------------------------------
## Assignment 06: assignment_6_Weather.ipynb
This notebook analyses weather data from Knock Airport:
https://cli.fusio.net/cli/climate_data/webdata/hly4935.csv
It plots:
- The hourly temperature
- The mean temperature each day
- The mean temperature for each month
- The hourly windspeed readings
- The 24-hour rolling mean windspeed
- The maximum daily windspeed
- The monthly mean of the maximum daily windspeeds
