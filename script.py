#Import required libraries
import pandas as pd
import json
!pip install openpyxl
from openpyxl import Workbook  

url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"

#Define the function to extract technology and number of jobs details
def get_number_of_jobs_T(technology):
    # payload must be a dictionary of key-value pairs
    payload = {"Key Skills": technology}

    # make GET request with params
    response = requests.get(api_url, params=payload)

    # load returned JSON
    data = response.json()

    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Count jobs where 'Key Skills' contains the technology (case-insensitive)
    number_of_jobs = df['Key Skills'].str.contains(technology, case=False, na=False, regex=False).sum()
    
    return technology,number_of_jobs
    
#Calling the Function for python and checking if it works
get_number_of_jobs_T("Python")

#To store the result in excel file
# List of technologies
Technology = ["Python","Java","C++","SQL","R","JavaScript","Scala"]

#create a workbook and active worksheet
wb=Workbook()
ws=wb.active

#Write the Technology name to column 1 and Number of jobs to column 2
ws.append(['Technology', 'JobPostings'])
ws.append(['Python', get_number_of_jobs_T("Python")[1]])
ws.append(['Java', get_number_of_jobs_T("Java")[1]])
ws.append(['C++', get_number_of_jobs_T("C++")[1]])
ws.append(['SQL', get_number_of_jobs_T("SQL")[1]])
ws.append(['R', get_number_of_jobs_T("R")[1]])
ws.append(['JavaScript', get_number_of_jobs_T("JavaScript")[1]])
ws.append(['Scala', get_number_of_jobs_T("Scala")[1]])

#Save the details as excel sheet named jobs-postings.xlsx
wb.save("job-postings.xlsx") 