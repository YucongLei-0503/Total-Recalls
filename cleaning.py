import pandas as pd




# function to see duplicates in the CSV file
def check_duplicates(df, columns):

    # check for duplicates based on PRODUCTID and RECALLEVENTID only
    duplicates = df.duplicated(subset=columns, keep=False)
    if duplicates.any():
        # for each unique duplicate, print the rows where it is repeated
        for value in df[duplicates][columns[0]].unique():
            indexes = df[df[columns[0]] == value].index.tolist()
            print(f"Duplicate found for {columns} = {value} at indexes: {indexes}")
    else:
        print("No duplicates found.")






# function to remove duplicates based on the columns specified
def remove_duplicates_and_save(df, cols):
    df = df.loc[~df.duplicated(subset=cols, keep='first')]

    return df
    




# function to drop unnecessary columns
def drop_unnecessary_columns(drop_list, df):
    df.drop(columns=drop_list, inplace=True, errors='ignore')

    return df



def drop_entries(df, column, value):
    # drop entries where the column has the specified value
    if isinstance(value, list):
        df = df[~df[column].isin(value)]
    else:
        df = df[df[column] != value]


    return df


def keep_entries(df, column, value):
    # keep entries where the column has the specified value
    if isinstance(value, list):
        df = df[df[column].isin(value)]
    else:
        df = df[df[column] == value]

    return df





# function to one-hot encode the product classification
def encode(df):
    # one-hot encode the CLASSIFICATION column
    df = pd.get_dummies(df, columns=['CENTERCLASSIFICATIONTYPETXT'], prefix='CLASSIFICATION')

    return df




# function to identify most common reasons for recall
def analyze_most_common_words(data_series, n=10):
    from collections import Counter
    import re
    import nltk
    nltk.download('stopwords')

    # Clean the text
    text = ' '.join(str(item) for item in data_series)
    text = re.sub(r'[^\w\s]', '', text).lower()
    words = text.split()
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    # Count word frequencies
    word_counts = Counter(words)

    # Get the most common words
    most_common = word_counts.most_common(n)
    
    return most_common




    # function to engineer reasons for recall and group them into categories
def engineer_reasons(df):
    # define a mapping of reasons to categories
    reason_mapping = {
        'Labeling': ['mislabeling', 'mislabeled', 'without labeling,', 'statement listed ', 'old label:', 'undeclared', 'not declared', 'not declare ', 'unlisted', 'not listed', 'not identifying', 'not identified', 'failed to declare'],
        'Pathogens': ['bacteria', 'mites', 'virus', 'salmonella', 'listeria', 'l. mono.', 'l monocytogenes.', 'burkholderia cepacia.', 'enterobacter gergoviae.', 'e. coli', 'e.coli', 'b cereus', 'pathogen', 'pathogens', 'mold', 'micro growth', 'parasite'],
        'Contamination': ['plastic', 'metal', 'glass', 'broken', 'foreign', 'chemical', 'chemicals', 'elevated', 'lead', 'iodine', 'level', 'levels', 'pesticide', 'pesticides', 'residue', 'residues', 'extraneous', 'fragment', 'fragments', 'melamine', 'inorganic'],
        'Allergens' :  ['allergens', 'allergen', 'peanut', 'nut', 'soy', 'egg', 'anchovies'],
        'Packaging': ['packaging', 'seal', 'leakage', 'leak', 'lid', 'cap'],
        'Quality': ['quality', 'spoilage', 'spoiled', 'under-processing', 'under-processed', 'violation', 'violations', 'deficiencies', 'temperature'],
    }

    # function to categorize reasons
    def categorize_reason(reason):
        # for loop ensures case-insensitive matching and only first match is used
        for category, keywords in reason_mapping.items():
            if any(keyword in reason.lower() for keyword in keywords):

                return category
        return 'Other'  # Default category if no match found
    
    # Apply the categorization to the PRODUCTSHORTREASONTXT column
    df['REASON_CATEGORY'] = df['PRODUCTSHORTREASONTXT'].apply(categorize_reason)

    # Remove all entries with 'Other' category
    df = df[df['REASON_CATEGORY'] != 'Other']

    return df



def list_unique_entries(df, column):
    # list unique entries in the specified column
    unique_entries = df[column].unique()
    print(unique_entries)
    # count of each unique entry
    counts = df[column].value_counts()
    print(counts)




# function to categorize DISTRIBUTIONAREASUMMARYTXT column
def distribution_area(df, states, states_abbr):
    
    # map of 50 US states to their abbreviations
    state_map = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY"}
    # function to categorize states
    def categorize_state(dist):
        states_found = ""
        for state in states:
            if pd.notnull(dist) and state in dist:
                # map state to its abbreviation using the state_map
                states_found = states_found + state_map[state] + ', '

        for state_abbr in states_abbr:
            if pd.notnull(dist) and state_abbr in dist:
                states_found = states_found + state_abbr + ', '
        return states_found if states_found else ""
    
        # None: no states identified i.e only number of centers or states given, or no information

            
    # create a new column with the categorized states
    df['DISTRIBUTION'] = df['DISTRIBUTIONAREASUMMARYTXT'].apply(categorize_state)

    # Covers cases where distribution is nationwide
    df.loc[df['DISTRIBUTION'].isnull() & df['DISTRIBUTIONAREASUMMARYTXT'].str.contains('nationwide|all 50|national', case=False, na=False), 'DISTRIBUTION'] = 'US'

    return df

