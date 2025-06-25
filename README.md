# Total Recall
Team Members: Sam Boardman, Khola Jamshad, Riku Kurama, Yucong Lei, Shivani Prabala


## Table of Contents
1. [Link-Text](#introduction)
2. [Link-Text](#data-processing)
3. [Link-Text](#data-exploration)
4. [Link-Text](#methods-and-models)
5. [Link-Text](#results)
6. [Link-Text](#future-work)
7. [Link-Text](#repository)


## Introduction


## Data Processing


## Data Exploration


## Methods and Models


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

Baseline Model: 
Dummy Classifier (Predict the most common class (usually 0, i.e., no recall) for everything.)
Logistic Regression (A simple linear classifier.)


### Inference Models







