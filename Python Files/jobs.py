from bs4 import BeautifulSoup
import requests

job = input('search for a job :')
unfamiliar = input('do you have any skills youre unfamiliaar with ? :')
while job != 'q':
    replaced = job.replace(' ','+')
    page = BeautifulSoup(requests.get(f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={replaced}&txtLocation=').text, 'lxml')
    jobli = page.find_all('li', class_="clearfix job-bx wht-shd-bx")
    for i in jobli:
        company = i.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        skills = i.find('span', class_='srp-skills').text.replace(' ', '')
        dateposted = i.find('span', class_='sim-posted').span.text.replace(' ', '')
        link = i.find('h2').find('a').get('href')
        if unfamiliar not in skills:
            print(f'\nCompany: {company.strip()}')
            print(f'Skills required: {skills.strip()}')
            print(f'Date Posted: {dateposted.strip()}')
            print(f'Link to the job: {link}')
    
    job = input('\nsearch for a job :')
    unfamiliar = input('do you have any skills youre unfamiliaar with ? :')