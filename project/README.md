# Arts Council Funding by Artform, 2003-2010, 2016, 2017  
This repository explores the funding awarded to individual artists by the Irish 
Arts Council, and analyses funding trends by artform.


## Overview  
This repository contains a Jupyter Notebook project analysing Arts Council of Ireland grant funding awarded to individual artists. The project was completed as part of a final-year undergraduate module in Programming for Data Analytics and demonstrates the full data analysis workflow: data acquisition, cleaning, analysis, and presentation.

The analysis focuses on funding patterns by artform, gender representation, and changes over time using limited publicly available data.


## Data Source  
**Arts Council Grants to Artists by Artform, 2003-2010, 2016, 2017**  
- The Arts Council does not publish historical funding data but breakdowns by artform and gender are available for the above years from the [Central Statistics Office](www.cso.ie), via CSO publications on ["Women and Men in Ireland"](https://www.cso.ie/en/statistics/womenandmeninireland/).  
(2013 publication does not contain any Arts Council data.)  
- **Note: the date in the URL refers to the date of publication, not the period of the data.**
- These tables do not represent all grants made by the Arts Council, but only grants 
made to individual artists (via schemes such as Cnuas, Artists’ Bursaries, Artists’ Awards.)

## Repository structure
```
project/
├── data/ # Cleaned datasets and intermediate files
├── README.md # Project overview
├── notebook.ipynb # Main analysis notebook (run end-to-end)
├── requirements.txt # Required Python libraries
```


## Requirements
- Python 3+
- Data Manipulation:
  - [NumPy](https://numpy.org/doc/stable/ ) Array manipulation 
  - [Pandas](https://pandas.pydata.org/docs/) Python Data Analysis Library
  - [xlrd](https://pypi.org/project/xlrd/) to read historical (.xls) Excel files.
- Data Visualisation:
  - [Matplotlib.PyPlot](https://matplotlib.org/stable/api/pyplot_summary.html)
  - [Seaborn](https://seaborn.pydata.org)

## Project Provenance
The work in this repository is submitted for assessment for the **Programming for Data Analytics** module, part of the [**Higher Diploma in Data Analytics**](https://www.atu.ie/courses/higher-diploma-in-science-data-analytics) at [**Atlantic Technological University, Ireland**](https://www.atu.ie/) (Autumn 2025).

**Author:** Susan Collins  
