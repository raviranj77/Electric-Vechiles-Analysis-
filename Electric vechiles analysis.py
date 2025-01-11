# -*- coding: utf-8 -*-
"""Untitled83.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DLfml3yDKvgbAhq036q-V_kUv8zqVrOa

# FIRST OF ALL IMPORT **LIBARIES**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

"""## LOAD **DATASET**"""

df=pd.read_excel("/content/drive/MyDrive/DATASET/Electric_Vehicle_Population_Data1.xlsx")
df

"""#BASIC EXPLORATION"""

df.head()

df.info()

df.describe()

"""#HANDEL MISSING VALUE"""

df.fillna(0,inplace=True)

"""#STANDARIZE COLUMN NAMES"""

df.columns = df.columns.str.strip().str.replace(" ", "_").str.lower()

"""#COUNT THE NUMBER OF VEHICLES BY TYPE"""

vehicle_counts = df['electric_vehicle_type'].value_counts()
print(vehicle_counts)
vehicle_counts.plot(kind='bar', title='Number of Vehicles by Type')
plt.show()

"""#DISTRIBUTION OF ELECTRIC RANGES"""

sns.histplot(df['electric_range'], bins=10, kde=True)
plt.title('Distribution of Electric Ranges')
plt.xlabel('Electric Range')
plt.show()

"""#VEHICLES BY CITY OR COUNTRY"""

top_cities = df['city'].value_counts().head(10)
top_cities.plot(kind='bar', title='Top 10 Vehicles by City', figsize=(10, 6))
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

"""#CAFV ElIGIBILITY ANALYSIS"""

cafv_eligibility = df['clean_alternative_fuel_vehicle_(cafv)_eligibility'].value_counts()
print(cafv_eligibility)
cafv_eligibility.plot(kind='pie', autopct='%1.1f%%', title='CAFV Eligibility')
plt.show()

"""#VEHICLES BY MODEL YEAR"""

model_year_counts = df['model_year'].value_counts().sort_index()
print(model_year_counts)
model_year_counts.plot(kind='bar', title='Vehicles by Model Year', color='purple')
plt.xlabel('Model Year')
plt.ylabel('Number of Vehicles')
plt.show()

"""#ELECTRIC UTILITY ANALYSIS **bold text**"""

utility_counts = df['electric_utility'].value_counts().head(10)
print(utility_counts)
utility_counts.plot(kind='bar', title='Top 10 Electric Utilities Associated with Vehicles', color='coral')
plt.xlabel('Electric Utility')
plt.ylabel('Number of Vehicles')
plt.xticks(rotation=70)
plt.show()

"""#ELECTRIC RANGE VS MODEL **YEAR**"""

sns.boxplot(x='model_year', y='electric_range', data=df, palette='Set2')
plt.title('Electric Range by Model Year')
plt.xlabel('Model Year')
plt.ylabel('Electric Range')
plt.xticks(rotation=45)
plt.show()

"""#ELECTRIC RANGE BY COUNTRY"""

range_by_county = df.groupby('county')['electric_range'].mean().sort_values(ascending=False).head(10)
print(range_by_county)
range_by_county.plot(kind='bar', title='Average Electric Range by County', color='gold')
plt.xlabel('County')
plt.ylabel('Average Electric Range')
plt.show()

"""#TOP MODELS WITH HIGH ELECTRIC RANGES"""

top_models = df[df['electric_range'] > 200][['make', 'model', 'electric_range']]
top_models['make_model'] = top_models['make'] + " " + top_models['model']
top_models_sorted = top_models.sort_values(by='electric_range', ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(
    x='electric_range',
    y='make_model',
    data=top_models_sorted,
    palette='viridis'
)
plt.title('Top Electric Vehicle Models with Range > 200')
plt.xlabel('Electric Range')
plt.ylabel('Make and Model')
plt.tight_layout()
plt.show()

"""#TREND OF ELECTRIC VEHICLE ADOPTION OVER THE YEARS**

"""

vehicles_by_year = df['model_year'].value_counts().sort_index()
print(vehicles_by_year)
vehicles_by_year.plot(kind='line', marker='o', color='green', title='Electric Vehicle Adoption Over the Years')
plt.xlabel('Model Year')
plt.ylabel('Number of Vehicles')
plt.show()

"""#OUTLIER DETECTION IN ELECTRIC RANGE **"""

sns.boxplot(x=df['electric_range'], color='red')
plt.title('Boxplot of Electric Range')
plt.xlabel('Electric Range')
plt.show()

zip_counts = df['postal_code'].value_counts().head(10)
print(zip_counts)
zip_counts.plot(kind='bar', color='lightblue', title='Top 10 postal_code for Electric Vehicle Adoption')
plt.xlabel('postal_code')
plt.ylabel('Number of Vehicles')
plt.xticks(rotation=45)
plt.show()

"""#AVERAGE VECHICLE AGE"""

current_year = 2025  # Adjust to the current year
df['vehicle_age'] = current_year - df['model_year']
average_age = df['vehicle_age'].mean()
print(f"Average Vehicle Age: {average_age:.2f} years")
sns.histplot(df['vehicle_age'], bins=10, kde=True, color='brown')
plt.title('Distribution of Vehicle Age')
plt.xlabel('Vehicle Age (Years)')
plt.ylabel('Frequency')
plt.show()

df.columns