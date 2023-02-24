# Python Jobs Web Scaper (using BeautifulSoup)

From **Day 92** of **100 Days Of Code** taught by _Angela Yu_.

### Course Section Instructions:
> Build a custom web scraper to collect data on things that you are interested in.

This project scrapes jobs from [PythonJobs](https://pythonjobs.github.io/) using the `bs4` module. It also implements the `requests` module and the `os` module; to make **GET** requests and to save the results to a **.csv** file. It also uses the `pprint` module to output scraped data to the console.

Each run of the script will create and save a new .csv file to the directory, renamed by an increment of 1 (i.e. - `python_jobs_002.csv`). Each scraped section contains:
- Job Title
- Summary
- URL (which contains the full job description)
