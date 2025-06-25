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
Our primary dataset is of [FDA recalls](https://datadashboard.fda.gov/oii/cd/recalls.htm) which we filter for food product type and remove miscellaneous features mostly relating to company descriptions. Feature engineering was done to categorize the states included in the distribution of the product and reasons for recall. We append a separate [FDA inspection](https://datadashboard.fda.gov/oii/cd/inspections.htm) dataset to provide a counterbalance of non-recalled food products. Entries in both datasets are matched using their FEI (FDA assigned identifying numbers), _recall bool_ is used to label any entry in both datasets as recalled (1) and the remaining as not recalled (0). We engineered a count of the cities mentioned as a new feature and one hot encoded all categorical variables. Since our data was imbalanced, with a lot more non-recalled products, we removed any entries associated with firms that had never faced recalls leaving us with 18287 entries on which we ran our model.

For food related outbreaks, we used the CDC database [BEAM](https://data.cdc.gov/Foodborne-Waterborne-and-Related-Diseases/BEAM-Dashboard-Report-Data/jbhn-e8xn/data_preview) which records various disease outbreaks with different pathogen types such as salmonella and Campylobacter from 2018 to 2025. The features that we exploited in this data set are year, month and the pathogen type.

## Data Exploration
We investigated the FDA recall data initially with an interest in whether there was a correlation between the location of the firm and recalls, and also whether certain states were most affected by recalls due to distribution pathways of the product. We see a strong correlation between the firm locations and states most impacted indicating that the firm locations are a good indicator of whether a product will be recalled.

![US map of firms](/Images/geofirm.png)

![US map of recalled product distributions](/Images/geodist.png)

Once we had integrated the recalls and inspections datasets, we also looked at temporal trends by grouping them by months and calculating recalls as a percentage of inspections, which would indicate whether inspection count and times affect recalls. We find that there seems to be some oscillatory behavior in the peaking of recall \% every 4-6 years. While we do not focus on covid years in this project, we did note a high in the covid years which was interesting since the absolute number of recalls was down hinting at a direct impact of workforce reduction. 

![Monthly recalls as percent of inspections](/Images/monthlypercent.png)

Since we had a good understanding of the spatial relation of the FDA recall-inspection data, we wanted to compare it with the outbreak data from BEAM. While there is some correlation particularly for the highest outbreak and recall areas, there are discrepancies. These may be due to the climate since northern areas are colder and therefore less hospitable to the pathogens (Campylobacter, STEC, Shigella, salmonella, and vibrio) that are associated with these outbreaks.

![US map of outbreaks](/Images/geooutbreaks.png)

At this point, we ran a preliminary random forest classifier to see relative feature importance for predicting recalls and unsurprisingly find state and days since the last inspection to be most important. This lists the 14 features we included later in our models with the exception of city frequency.

![Feature selection](/Images/feature-selection.png)



## Models
### Predicting Recalls

We investigated 3 different models in comparison to a baseline
- As a baseline model, we used a dummy classifier (DC) which always predict the majority class.
- Logistic regression (LR)
- Random forest classification (RF)
- Support vector machine (SVM)

We first independently tested the RF and SVM models on the data and found that because of the imbalance in the data, we had low scores for predicting recalls. To counter this, we included balanced class weights for all 3 models and ran GridSearchCSV to find the best hyperparameters.


### Food Recalls and Outbreaks
We used time series analysis for the inference modeling with 7 features: the month and 6 pathogens associated with the outbreaks. 
We used two models: a naive seasonal model and a vector autoregression (VAR) model. For the VAR model, we combined the FDA and the BEAM datasets to better predict future recall probabilities, which however forced us to truncate our available dataset to the timeframe from 2018 to 2025. We also added some aspect of seasonality to the final VAR model by including the variable which records the average recall percentage in the same months over the past three years. 


## Results
![Random forest decision tree](/Images/rftree.png)

According to our kfold-split cross validation with k=5, the VAR model without this added seasonality has less predictive power than the naive seasonal model, but the final VAR model with this added seasonality outperformed the seasonal model. 


## Future Work


## Repository

### Data
(Data/recall_data_save.csv) : the original data of recalled items from the FDA recalls API
(Data/test.csv) : cleaned FDA recalls API
fda_inspections.xslx = all FDA inspections data from their website
beam.csv = 

final_engineered_features.csv = takes the inspection data, and creates a 'recalled_bool' column that is 0 or 1 depending on if the same FEI number appears in the test.csv file (original recall dataset), and also creates a new column called classification_flag that is 1 if the 'Classification' value is in the high-risk list: ['Official Action Indicated (OAI)', 'Voluntary Action Indicated (VAI)'] and is 0 otherwise.

monthly_recall_percentage.csv = 

### Predictive Models




### Inference Models







