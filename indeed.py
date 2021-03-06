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

def extract_job(html):
    title = html.find("h2", {"class":"title"}).find("a")["title"]
    #anchor = title.find("a")["title"]
    company = html.find("span", {"class":"company"})
    company_anchor = company.find("a")
    if  company_anchor is not None:
        company = str(company_anchor.string)
    else:
        company = str(company.string)

    company = company.strip()
    location = html.find("div", {"class":"recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return {"title": title, "company": company, "location":location, "link": f"https://www.indeed.com/viewjob?jk={job_id}"}



def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{INDEED_URL}&start={last_page*50}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)

    return jobs