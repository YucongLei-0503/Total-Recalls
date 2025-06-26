import pandas as pd
import cleaning as cl




# Load the data from a previously saved CSV file (please DO NOT edit or overwrite this file)
df = pd.read_csv("recall_data_save.csv", low_memory=False)


########################### Categorizng Columns ###########################

######## 1. Reasons for Recall ########
# Categorizes recall reasons into 6 categories: Labeling, Pathogens, Contamination, Allergen, Packaging, Quality
# entries with no reason are categorized as 'Other' and dropped
df = cl.engineer_reasons(df)


######### 2. Classification Type - Possible Target ########
# One hot encoding of the classification column indicating the degree of hazard presented
# Class I: serious risk, Class II: moderate risk, Class III: low risk, NC: not classified
# entries with no classification are NOT yet dropped in case they are needed for further analysis
df = cl.encode(df)


######### 3. Distribution ########
us_states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
    "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky",
    "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
    "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico",
    "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
    "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
    "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]
us_states_abbr = ["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "IA",
    "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO",
    "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK",
    "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI",
    "WV", "WY"]

# Keeps only firms based in the 50 US states????
df = cl.keep_entries(df, 'FIRMSTATEPRVNCNAM', us_states)

# Reads state names/abbreviations from the list and adds a new column with the corresponding abbreviation
# Maps national distribution to abbreviation "US"
df = cl.distribution_area(df, us_states, us_states_abbr)

# Drops the old distribution data column
df = cl.drop_unnecessary_columns(['DISTRIBUTIONAREASUMMARYTXT'], df)

# Drops rows with empty DISTRIBUTION column
df = cl.drop_entries(df, 'DISTRIBUTION', "")

##########################################################################



############################# Cleaning Data #############################
# Keeps only firms based in the United States (OPTIONAL???)
df = cl.keep_entries(df, 'FIRMCOUNTRYNAM', 'United States') 

# Dropping unnecessary columns
drops = ['PRODUCTTYPESHORT', 'FIRMCITYNAM', 'FIRMLINE1ADR', 'FIRMLINE2ADR', 'FIRMPOSTALCD', 'VOLUNTARYTYPETXT', 
         'CENTERCD', 'CENTERCLASSIFICATIONDT', 'POSTEDINTERNETDT', 'INITIALFIRMNOTIFICATIONTXT', 'CENTERCLASSIFICATIONTYPETXT', 
         'ENFORCEMENTREPORTDT', 'PRODUCTDISTRIBUTEDQUANTITY', 'DETERMINATIONDT', 'RID', 'FIRMCOUNTRYNAM', 'PRODUCTSHORTREASONTXT']
df = cl.drop_unnecessary_columns(drops, df)

# Drop any rows that are complete duplicates of another row (after dropping unnecessary columns)
df = cl.remove_duplicates_and_save(df, df.columns)

########################################################################

# Save the cleaned data to a new CSV file
df.to_csv('test.csv', index=False)








############################### Testing Code ###############################
# df = pd.read_csv("test.csv", low_memory=False)


# df.to_csv('test.csv', index=False)

############################################################################