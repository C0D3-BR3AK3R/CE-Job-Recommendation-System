from bs4 import BeautifulSoup
import requests
import pandas as pd

class JobScraper:
    
    def __init__(self):
        super().__init__()    
        
    def webscrape_jobs(self, lst):
        
        print('PRINTING RESULTS')
        
        company_name_lst = []
        skills_lst = []
        location_lst = []
        more_info_lst = []
        
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
                    
                    company_name_lst.append(company_name.strip())
                    skills_lst.append(skills.strip())
                    location_lst.append(location)
                    more_info_lst.append(more_info)
                    
                    
                    """ print(f"Company Name : {company_name.strip()}")
                    print(f"Required Skills : {skills.strip()}")
                    print(f"Location : {location}")
                    print(f"More Info : {more_info}")
                    print('') """
                
        """ print(company_name_lst)
        print(skills_lst)
        print(location_lst)
        print(more_info_lst)
        
        print("Company Name list len:", len(company_name_lst))
        print("Skills list len:", len(skills_lst))
        print("Location list len:", len(location_lst))
        print("More Info List len:", len(more_info_lst)) """
        
        data_dict = {
            'Company_Name':company_name_lst,
            'Skills':skills_lst,
            'location':location_lst,
            'more_info':more_info_lst
        }
        
        data_df = pd.DataFrame(data_dict)
        print(data_df.head())
        data_df.to_csv('FlaskApp\data\jobs_data.csv', index=False)