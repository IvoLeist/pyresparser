#taken from
#https://github.com/OmkarPathak/pyresparser/blob/master/export_to_csv.py
#accessed on 2024-16-03

from pyresparser.resume_parser import ResumeParser
from rank_candidate import sort_candidates
from datetime import datetime
import pandas as pd
import sys
import os

import requests
from bs4 import BeautifulSoup

def get_job_description(url, div_class):
    """
    Get the job description from the web
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    job_description = soup.find('div', class_= div_class).get_text()
    return job_description

result = []
fields = ['Date', 'Skills', 'Name', 'Contact Number', 'Email ID', 'Current Company', 'Experience', 'College Name', 'Designation', 'Filename']

for root, directories, filenames in os.walk(sys.argv[1]):
    for filename in filenames:
        try:
            file_name = os.path.join(root, filename)
            print('Extracting data from ' + file_name)
            parser = ResumeParser(file_name)
            data = parser.get_extracted_data()
            name = data.get('name')
            email = data.get('email')
            mobile_number = data.get('mobile_number')
            skills = ', '.join(data.get('skills')) if data.get('skills') else ''
            total_experience = str(data.get('total_experience'))
            experience = ' '.join(data.get('experience')) if data.get('experience') else ''
            company_names = ', '.join(data.get('company_names')) if data.get('company_names') else ''
            college_name = data.get('college_name')
            designation = ', '.join(data.get('designation')) if data.get('designation') else ''

            result.append(
                [
                    datetime.today().strftime('%d-%B-%y'),
                    skills,
                    name,
                    mobile_number,
                    email,
                    company_names, 
                    experience,
                    college_name,
                    designation,
                    file_name
                ]
            )
        except:
            continue

# writing to csv file
df = pd.DataFrame(result, columns=fields)
df = df.applymap(lambda x: x.replace('\n', ' ') if isinstance(x, str) else x)

try:
    url = "https://www.cnag.eu/jobs/front-end-software-engineer-data-platforms-tools-dev-unit"
    div_class = "main-content"
    job_description = get_job_description(url, div_class)
    ranked_df = sort_candidates(job_description, df)

    # Sort candidates in descending order of score
    ranked_df.sort_values(by="Score", ascending=False, inplace=True)
    ranked_df.to_csv(
        os.path.join(
            root, 
            (datetime.today().strftime('Extracted-Resumes-Ranked%d-%m-%y.csv'))
        ),
        index=False,
        sep=";",
        escapechar="\\"
    )
except IndexError:
    df.to_csv(
        os.path.join(
            root, 
            (datetime.today().strftime('Extracted-Resumes-%d-%m-%y.csv'))
        ), 
        index=False,
        sep=";",
        escapechar="\\"
    )

# *df_to_csv still seems to be buggy
# because the output file has one row more than expected
# for a working export to csv see scripts/convert_json_to_csv.py

# with open(os.path.join(root, (datetime.today().strftime('%d-%m-%y.csv'))), 'w', encoding="utf-8") as csvfile: 
#     try:
#         # creating a csv writer object 
#         csvwriter = csv.writer(csvfile) 
            
#         # writing the fields 
#         csvwriter.writerow(fields) 
            
#         # writing the data rows 
#         csvwriter.writerows(result)
#     except:
#         print('Some of the file might be corrupted or is not supported by parser')
# print(ranked_df)
