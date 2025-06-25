# Total Recall
Team Members: Sam Boardman, Khola Jamshad, Riku Kurama, Yucong Lei, Shivani Prabala


## Table of Contents
1. [Introduction](#introduction)
2. [Data Processing](#data-processing)
3. [Data Exploration](#data-exploration)
4. [Methods and Modelst](#methods-and-models)
5. [Results](#results)
6. [Future Work](#future-work)
7. [Repository](#repository)


## Introduction
Introduction
Recent [workforce reductions at the FDA](https://www.theguardian.com/us-news/2025/apr/17/fda-suspends-quality-control-food-testing-staff-cuts) and the subsequent suspension of a quality-control program at its food-testing laboratories, have elucidated the need for an efficient contamination tracking of food products. Our aim is to predict which products are likely to face recalls and to understand the relationship between recalls and outbreaks using inference modeling to inform further efforts to reduce the risk and harm of contaminated food products.
Our primary company KPIs are as follows
- Prevention rate of contaminated products reaching consumers
- Cost savings to manufacturers from early warnings and avoided recalls


## Data Processing
Our primary dataset is of [FDA recalls](https://datadashboard.fda.gov/oii/cd/recalls.htm) which we filter for food product type and remove miscellaneous features mostly relating to company descriptions. Feature engineering was done to categorize the states included in the distribution of the product and reasons for recall. We append a separate [FDA inspection](https://datadashboard.fda.gov/oii/cd/inspections.htm) dataset to provide a counterbalance of non-recalled food products. Entries in both datasets are matched using their FEI (FDA assigned identifying numbers), _recall bool_ is used to label any entry in both datasets as recalled (1) and the remaining as not recalled (0). 

For food related outbreaks, we used the CDC database [BEAM](https://data.cdc.gov/Foodborne-Waterborne-and-Related-Diseases/BEAM-Dashboard-Report-Data/jbhn-e8xn/data_preview) which records various disease outbreaks with different pathogen types such as salmonella and Campylobacter from 2018 to 2025. The features that we exploited in this data set are year, month and the pathogen type.

## Data Exploration



## Methods and Models
We used a total of 15 features including the state of inspections, days since last inspection etc.

Baseline Model: 
Dummy Classifier (Predict the most common class (usually 0, i.e., no recall) for everything.)
Logistic Regression (A simple linear classifier.)


## Results


## Future Work


## Repository

### Data
recall_data_save.csv = the original data of recalled items from the FDA recalls API
test.csv = cleaned FDA recalls API
fda_inspections.xslx = all FDA inspections data from their website
beam.csv = 

final_engineered_features.csv = takes the inspection data, and creates a 'recalled_bool' column that is 0 or 1 depending on if the same FEI number appears in the test.csv file (original recall dataset), and also creates a new column called classification_flag that is 1 if the 'Classification' value is in the high-risk list: ['Official Action Indicated (OAI)', 'Voluntary Action Indicated (VAI)'] and is 0 otherwise.

monthly_recall_percentage.csv = 

### Predictive Models




### Inference Models







