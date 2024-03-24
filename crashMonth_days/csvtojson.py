import csv 
import json

def csv_to_json(csv_file, json_file_2022, json_file_2023): 
    with open(csv_file) as file: 
        reader = csv.DictReader(file)
        data_2022 = []
        data_2023 = []
        for row in reader:
            crash_date = row['CRASH_DATE']
            crash_year = crash_date.split('-')[0]  # Extract year from "CRASH_DATE": "2023-12-31 23:50:00", split at first dash (-)
            if crash_year == '2022':
                data_2022.append({
                    'CRASH_DATE': row['CRASH_DATE'],
                    'Weekday': row['Weekday'],
                    'CRASH_DAY_OF_WEEK': row['CRASH_DAY_OF_WEEK'],
                    'CRASH_MONTH': row['CRASH_MONTH']
                })
            elif crash_year == '2023':
                data_2023.append({
                    'CRASH_DATE': row['CRASH_DATE'],
                    'Weekday': row['Weekday'],
                    'CRASH_DAY_OF_WEEK': row['CRASH_DAY_OF_WEEK'],
                    'CRASH_MONTH': row['CRASH_MONTH']
                })

    with open(json_file_2022, "w") as file:
        json.dump(data_2022, file, indent=4)

    with open(json_file_2023, "w") as file:
        json.dump(data_2023, file, indent=4)

csv_to_json("2022-2023.csv", "2022.json", "2023.json")
