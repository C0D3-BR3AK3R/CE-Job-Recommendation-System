from bs4 import BeautifulSoup
import requests

class JobScraper:
    
    def __init__(self):
        super().__init__()    
        
    def webscrape_jobs(self, lst):
            
        print(lst)
        print(lst)
        
        for i in lst:
            your_skill = i
            print("----------------------------------------------------------------------")
            url = str(f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={your_skill}&txtLocation=")
            html_text = requests.get(url).text
            soup = BeautifulSoup(html_text, 'html.parser')
            jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
            
            for job in jobs:
                published_date = job.find('span',class_ = 'sim-posted').span.text
                
                if 'few' in published_date:
                    
                    company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
                    skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
                    location = job.find('ul', class_ = 'top-jd-dtl clearfix').span.text
                    more_info = job.header.h2.a['href']
                    
                    print(f"Company Name : {company_name.strip()}")
                    print(f"Required Skills : {skills.strip()}")
                    print(f"Location : {location}")
                    print(f"More Info : {more_info}")
                    print('')