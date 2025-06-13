#pip install requests -> needed to run this script
# This script fetches data from the FDA recalls API, filters it, and saves it to a CSV file.
# Creates CSV files recall_data.csv and recall_data_test.csv that overwrite previous files.
# Currently filters for food recalls before June 1, 2025 -> change in if RESULT loop
# Might taka a while to run so I'm uploading recall_data_save.csv to the repo

import requests
import json
import datetime
import pandas as pd
import os
import time


#function to fetch data using API
def fetch_and_save(start, rows=5000, max_retries=5):
    # Generate a unique signature for each request
    signature = str(int(datetime.datetime.now().timestamp()))
    url = 'https://www.accessdata.fda.gov/rest/iresapi/recalls/?signature=' + signature
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization-User': 'kjamshad@umich.edu',
        'Authorization-Key': 'fLzOCH0k7otndBOk',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }

    #displaycolumns determines which columns are returned in the response
    payload = {
        "displaycolumns": "productid,recalleventid,producttypeshort,firmcitynam,firmcountrynam,firmline1adr,firmline2adr,firmpostalcd,phasetxt,recallinitiationdt,firmlegalnam,voluntarytypetxt,distributionareasummarytxt,centercd,firmstateprvncnam,centerclassificationdt,terminationdt,initialfirmnotificationtxt,centerclassificationtypetxt,enforcementreportdt,firmfeinum,firmsurvivingnam,firmsurvivingfei,eventlmd,productdescriptiontxt,productshortreasontxt,recallnum,productdistributedquantity,determinationdt,postedinternetdt",
        "filter": '[]',
        "start": start,
        "rows": rows,
        "sort": "recalleventid",
        "sortorder": "desc"
    }

    # requesting the API
    data = {"payload": json.dumps(payload)}
    for attempt in range(max_retries):
        try:
            response = requests.post(url, headers=headers, data=data, timeout=60)
            print(f"Status: {response.status_code}, Start: {start}")
            if response.status_code == 200 and response.text.strip():
                responses = response.json()
                if 'RESULT' in responses:
                    filtered = []
                    for entry in responses['RESULT']:
                        date_str = entry.get('RECALLINITIATIONDT') # ensuring recall initiation date is present
                        if date_str and entry.get('PRODUCTTYPESHORT') == 'Food': #filtering for food recalls
                            # Check if the date is before June 1, 2025
                            # Converts string to datetime object for comparison
                            try:
                                dt = datetime.datetime.strptime(date_str, "%m/%d/%Y")
                                if dt < datetime.datetime(2025, 6, 1):
                                    filtered.append(entry)
                            except Exception as e:
                                print(f"Date parse error: {date_str} ({e})")

                    print(f"Filtered records: {len(filtered)}")

                    # Save to CSV
                    df = pd.DataFrame(filtered)
                    file_exists = os.path.isfile("recall_data.csv")
                    df.to_csv("recall_data.csv", mode='a', header=not file_exists, index=False)
                    print("Filtered data saved to recall_data.csv")
                else:
                    print("No 'RESULT' key in response.")
                break  # Success, exit retry loop
            else:
                print("Response is not JSON or status code is not 200.")
                time.sleep(2 ** attempt)
        except Exception as e:
            print(f"Request failed (attempt {attempt+1}/{max_retries}): {e}")
            time.sleep(2 ** attempt)
    else:
        print(f"Failed to fetch data for start={start} after {max_retries} attempts.")


    # Clear any previous CSV file before writing
    if os.path.exists("recall_data.csv"):
        os.remove("recall_data.csv")


    # Loop through batches of rows (5000 is maximum allowed by the API)
    # Assuming less than 100000 total records by looking at website database
    for i in range(1, 100000, 2000):
        fetch_and_save(start=i, rows=2000)
        time.sleep(5)  # Sleep to avoid hitting API too hard





# function to see duplicates in the CSV file
def check_duplicates():
    # load the CSV file
    df = pd.read_csv("recall_data.csv", low_memory=False)

    # check for duplicates based on PRODUCTID and RECALLEVENTID only
    duplicates = df.duplicated(subset=['PRODUCTID', 'RECALLEVENTID'], keep=False)
    if duplicates.any():
        print("Duplicates found at indices:")
        print(df[duplicates].index.tolist())
        print(df[duplicates][['PRODUCTID', 'RECALLEVENTID']])
    else:
        print("No duplicates found.")






# function to remove duplicates and save to new CSV file
def remove_duplicates_and_save():
    # load the CSV file
    df = pd.read_csv("recall_data.csv", low_memory=False)

    # remove if all columns except the last one (RID) are duplicates
    df = df.loc[~df.duplicated(subset=df.columns[:-1], keep='first')]
    df.to_csv("recall_data_test.csv", index=False)




