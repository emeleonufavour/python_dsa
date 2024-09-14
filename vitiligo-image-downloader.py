import csv
import os
import requests
from urllib.parse import urlparse
import time

def download_image(url, filepath):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers, stream=True)
    if response.status_code == 200:
        with open(filepath, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Downloaded: {filepath}")
    else:
        print(f"Failed to download: {url}")

output_dir = '/Users/mac/dataset/skin_diseases_images/img/vitiligo'
os.makedirs(output_dir, exist_ok=True)

with open('/Users/mac/dataset/skin_diseases_images/csv/vitiligo.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        url = row['url']

        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        filepath = os.path.join(output_dir, filename)
        
        download_image(url, filepath)
        
        time.sleep(1)

print("Download complete!")
