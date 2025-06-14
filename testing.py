import pandas as pd
import cleaning as cl

# Load the data
df = pd.read_csv("recall_data_save.csv", low_memory=False)

df = cl.engineer_reasons(df)

df = cl.encode(df)

df = cl.keep_entries(df, 'FIRMCOUNTRYNAM', 'United States')

drops = ['PRODUCTTYPESHORT', 'FIRMCITYNAM', 'FIRMLINE1ADR', 'FIRMLINE2ADR', 'FIRMPOSTALCD', 'VOLUNTARYTYPETXT', 
         'CENTERCD', 'CENTERCLASSIFICATIONDT', 'POSTEDINTERNETDT', 'INITIALFIRMNOTIFICATIONTXT', 'CENTERCLASSIFICATIONTYPETXT', 
         'ENFORCEMENTREPORTDT', 'PRODUCTDISTRIBUTEDQUANTITY', 'DETERMINATIONDT', 'RID', 'FIRMCOUNTRYNAM', 'PRODUCTSHORTREASONTXT']
df = cl.drop_unnecessary_columns(drops, df)

df = cl.remove_duplicates_and_save(df, df.columns)

us_states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
    "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky",
    "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
    "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico",
    "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
    "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
    "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

df = cl.keep_entries(df, 'FIRMSTATEPRVNCNAM', us_states)


df.to_csv('test.csv', index=False)



df = pd.read_csv("test.csv", low_memory=False)

# count unique entries in each column and print
for column in df.columns:
    unique_count = df[column].nunique()
    print(f"Column '{column}' has {unique_count} unique entries.")


# # Check for duplicates
# cl.check_duplicates(df, df.columns)


# cl.list_unique_entries(df, 'FIRMSTATEPRVNCNAM')

us_states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
    "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky",
    "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
    "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico",
    "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
    "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
    "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

# all_states = ['California', 'Idaho', 'Alabama', 'Florida', 'Arkansas', 'Virginia' ,'New York',
#  'Texas', 'Oregon', 'Massachusetts', 'Ohio', 'Tennessee' ,'Indiana',
#  'South Carolina', 'Illinois' ,'Colorado', 'Hawaii' ,'Iowa', 'Utah',
#  'Pennsylvania', 'New Hampshire' ,'Washington', 'Kansas' ,'Wyoming', 'Maryland',
#  'New Jersey' ,'Michigan' ,'Connecticut' ,'Rhode Island', 'Vermont',
#  'Minnesota', 'New Mexico','Georgia', 'Wisconsin' ,'Arizona', 'Missouri',
#  'Oklahoma' ,'North Carolina' ,'Nebraska' ,'South Dakota' ,'Puerto Rico',
#  'Kentucky' ,'Maine', 'Louisiana', 'Delaware', 'Nevada' ,'Mississippi',
#  'West Virginia', 'Montana', 'North Dakota' ,'District of Columbia' ,'Alaska',
#  'Virgin Islands']

# print entries in all_states that are not in us_states
# for state in all_states:
#     if state not in us_states:
#         print(f"{state} is not in us_states")
# df = cl.keep_entries(df, 'FIRMSTATEPRVNCNAM', us_states)


# df.to_csv('test.csv', index=False)