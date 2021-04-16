import requests 
from bs4 import BeautifulSoup 

INDEED_URL = "https://www.indeed.com/jobs?q=python&limit=50"

def extract_indeed_pages():
    result = requests.get(INDEED_URL)

    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class":"pagination"})

    link = pagination.find_all('a')
    pages = []

    for link in link[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]

    return max_page

def extract_indeed_jobs(last_page):
    jobs = []
    #for page in range(last_page):
    result = requests.get(f"{INDEED_URL}&start={0*50}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
    for result in results:
        titles = result.find("h2", {"class":"title"})
        anchor = titles.find("a")["title"]
        print(anchor)

    return jobs