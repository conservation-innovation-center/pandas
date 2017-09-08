
## Import libraries
import os               ## short for "operating system"... lots of utility functions
import pandas as pd     ## using 'as pd' give us a shorter nickname to use as a reference

## Create path to data and set it as our working directory
dataDirectory = '/Users/colin/Desktop/chescon-github/pandas/sample-data'
os.chdir(dataDirectory)

## Create dataframe from Excel file
hucs = pd.read_excel('huc_table.xls')

## Loop through the columns your dataframe
for column in hucs.columns:
    print(column)