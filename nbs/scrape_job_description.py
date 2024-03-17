# %%
import requests
from bs4 import BeautifulSoup

# %%
def get_job_description(url, div_class):
    """
    Get the job description from the web
    """
    #use requests to get the job description from the web
    page = requests.get(url)
    # print(page.content)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup)
    job_description = soup.find('div', class_= div_class).get_text()
    return job_description

url = "https://www.cnag.eu/jobs/front-end-software-engineer-data-platforms-tools-dev-unit"
div_class = "main-content"

res = get_job_description(url, div_class)
print(res)
# %%
