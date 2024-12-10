# i want to compare put_object() vs upload_object() to upload bigfile.db to an s3 path.

import boto3
import time
import csv
import pandas as pd

s3 = boto3.client('s3')
bucket_name = 'fix-inconsistency-of-schema'
file = 'bigfile.db'
key = 'test_botos3/bigfile.db'

def measure_put_object():
    start_time = time.time()
    s3.put_object(Bucket=bucket_name, Key=key, Body=open(file, 'rb'))
    end_time = time.time()
    return end_time - start_time

def measure_upload_file():
    start_time = time.time()
    s3.upload_file(file, bucket_name, key)
    end_time = time.time()
    return end_time - start_time

put_object_times = []
upload_file_times = []

for i in range(25):
    print(f"Running put_object() iteration {i+1}/10")
    put_object_times.append(measure_put_object())
    print(f"Running upload_file() iteration {i+1}/10")
    upload_file_times.append(measure_upload_file())

with open('upload_times.csv', 'w', newline='') as csvfile:
    fieldnames = ['put_object', 'upload_file']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for put_time, upload_time in zip(put_object_times, upload_file_times):
        writer.writerow({'put_object': put_time, 'upload_file': upload_time})

# Analyze the results using pandas
df = pd.read_csv('upload_times.csv')
print(df.describe())


