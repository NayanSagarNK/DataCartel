import csv
import random
import datetime

# File name
output_file = "sample_data.csv"

# Number of records
num_records = 1000

# Define headers
headers = ["id", "name", "age", "city", "event_time"]

# Sample values
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Helen"]
cities = ["New York", "London", "Paris", "Tokyo", "Mumbai", "Berlin", "Sydney"]

# Write CSV
with open(output_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # Write header row
    
    for i in range(1, num_records + 1):
        row = [
            i,  # id
            random.choice(names),  # random name
            random.randint(18, 60),  # random age
            random.choice(cities),  # random city
            (datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 30))).isoformat()  # timestamp
        ]
        writer.writerow(row)

print(f"{num_records} records written to {output_file}")
