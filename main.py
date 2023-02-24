# Import statements:
import requests
from bs4 import BeautifulSoup
import csv
import os
from pprint import pprint

# Increment the saved .csv filename by 1 each time the script runs:
num = 1
while os.path.exists(f'python_jobs_{num:03}.csv'):
    num += 1

# Create the filename with the appended/updated number:
filename = f'python_jobs_{num:03}.csv'

# Save scraped URL to a variable:
url = 'https://pythonjobs.github.io/'

# Make the GET request and initialize BeautifulSoup:
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Locate the <div> element that contains the date & save as a variable:
jobs = soup.find_all('div', class_='job')

# Create the .csv file for the scraped data:
with open(filename, mode='w', newline='') as csv_file:
    fieldnames = ['Job Title', 'Summary', 'URL']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    # Begin the web scrape for the data:
    for job in jobs:
        # Extract the job title:
        job_title = job.find('h1').find('a').get('href')
        title = job.find('h1').text.strip()

        # Extract the job description and display the text:
        job_desc = job.find('p', class_='detail').text.strip()

        # Extract the URL for the full job description/etc:
        job_url = job.find('h1').find('a').get('href')

        # Write the scraped data to the .csv file:
        writer.writerow(
            {
                'Job Title': title,
                'Summary': job_desc,
                'URL': job_url
            }
        )

        # Output the scraped data to the console using the pprint module:
        pprint(
            {
                'Job Title': title,
                'Summary': job_desc,
                'URL': job_url
            }
        )
        print()

# Confirm the created .csv and filename in the console output:
print(f'Web Scrape Job Output saved to {filename}')