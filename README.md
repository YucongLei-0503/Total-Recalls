# Erdos-Data-Science-project-Environmental-science-and-climate-modeling

#Project for Erdos Data Science BootCamp 2025 

#Definitions: 
#recall_data_save = the original data of recalled items from the FDA website

#final_engineered_features = takes the inspection data, and creates a 'recalled_bool' column that is 0 or 1 depending on if the same FEI number appears in the test.csv file (original recall dataset), and also creates a new column called classification_flag that is 1 if the 'Classification' value is in the high-risk list: ['Official Action Indicated (OAI)', 'Voluntary Action Indicated (VAI)'] and is 0 otherwise.

#Baseline Models: 
#Dummy Classifier (Predict the most common class (usually 0, i.e., no recall) for everything.)
#Logistic Regression (A simple linear classifier.)

