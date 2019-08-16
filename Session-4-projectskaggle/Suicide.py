import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import os
print(os.listdir("C:\\Users\\anura\\GitHub\\python-assignments\\Session-4-projectskaggle\\Input"))

# Read the file
data = pd.read_csv('C:\\Users\\anura\\GitHub\\python-assignments\\Session-4-projectskaggle\\Input\\master.csv')

# First 5 rows in the data
print(data.head(5))

# Mean, Median, Mode of the Data
print(data.describe())

# Data Column rename
data=data.rename(columns={'country':'Country','year':'Year','sex':'Gender','age':'Age','suicides_no':'SuicidesNo','population':'Population','suicides/100k pop':'Suicides100kPop','country-year':'CountryYear','HDI for year':'HDIForYear',' gdp_for_year ($) ':'GdpForYearMoney','gdp_per_capita ($)':'GdpPerCapitalMoney','generation':'Generation'})

# Null sets in the data
print(data.isnull().any())

# Number of Nulls in the data
print(data.isnull().sum())

# HDIForYear should be removed
data = data.drop(['HDIForYear'], axis = 1)
