Electric Vehicle Dataset Analysis

This repository contains an in-depth analysis of an Electric Vehicle (EV) dataset. The dataset includes details such as vehicle models, manufacturers, electric ranges, counties of registration, and more. The analysis focuses on identifying trends, patterns, and insights related to electric vehicle adoption and performance.

Dataset Overview

The dataset provides the following key features:

Make: The manufacturer of the vehicle.

Model: The specific model of the electric vehicle.

Model Year: The year the vehicle model was manufactured.

Electric Range: The range of the vehicle on a full charge.

Electric Vehicle Type: Battery Electric Vehicle (BEV) or Plug-in Hybrid Electric Vehicle (PHEV).

County: The county where the vehicle is registered.

Electric Utility: The utility provider for the registered vehicle's location.

Exclusions

The analysis excludes the following columns, as they are not present in the dataset:

Electric Range Type

Year Group

CAFV Eligible Vehicles

Analysis Goals

Understand Adoption Trends: Analyze how electric vehicle adoption has evolved over time.

Manufacturer Insights: Identify the most popular EV manufacturers and their average electric ranges.

Geographical Distribution: Explore EV registration patterns across counties and zip codes.

Vehicle Performance: Examine the electric range distribution and identify outliers.

Utility Analysis: Investigate the relationship between electric utilities and vehicle performance.

Key Insights

Popular Models and Manufacturers: The analysis identifies the top electric vehicle models and manufacturers.

Geographical Trends: Highlights counties and zip codes with the highest EV registrations.

Performance Metrics: Provides insights into average electric ranges and identifies outliers.

Growth Over Time: Tracks the adoption of EVs by model year.

Visualizations

The analysis includes several visualizations:

Top Electric Vehicle Models: A bar chart showing the most popular EV models.

Adoption Trends: A line graph depicting EV registrations over the years.

Electric Vehicle Type Distribution: A pie chart comparing BEVs and PHEVs.

County-Wise Distribution: A bar chart showing the top counties by EV registration.

Electric Range Analysis: Box plots and scatter plots to understand electric range distribution and trends.

Repository Structure

data/: Contains the raw and cleaned datasets.

notebooks/: Jupyter notebooks with step-by-step analysis.

visualizations/: Saved plots and charts generated during the analysis.

README.md: This file, providing an overview of the project.

Tools and Libraries

The following tools and libraries were used for this analysis:

Python: Core programming language for data analysis.

Pandas: Data manipulation and cleaning.

Matplotlib & Seaborn: Data visualization.

NumPy: Numerical computations.
