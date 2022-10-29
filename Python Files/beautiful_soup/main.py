import time
from bs4 import BeautifulSoup
import requests

job = input("search for a job :")
unfamiliar = input("do you have any skills youre unfamiliaar with ? :")


def jobityjab():
    replaced = job.replace(" ", "+")
    page = BeautifulSoup(
        requests.get(
            f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={replaced}&txtLocation="
        ).text,
        "lxml",
    )
    jobli = page.find_all("li", class_="clearfix job-bx wht-shd-bx")
    for index, i in enumerate(jobli):
        company = i.find("h3",
                         class_="joblist-comp-name").text.replace(" ", "")
        skills = i.find("span", class_="srp-skills").text.replace(" ", "")
        dateposted = i.find("span",
                            class_="sim-posted").span.text.replace(" ", "")
        link = i.find("h2").find("a").get("href")
        if unfamiliar not in skills:
            with open(f'jobs\{index}.txt', 'a') as j:
                j.write(f'\nCompany: {company.strip()}\n')
                j.write(f'Skills required: {skills.strip()}\n')
                j.write(f'Date Posted: {dateposted.strip()}\n')
                j.write(f'Link to the job: {link}\n')
            print(f"\nCompany: {company.strip()}")
            print(f"Skills required: {skills.strip()}")
            print(f"Date Posted: {dateposted.strip()}")
            print(f"Link to the job: {link}")


if __name__ == '__main__':
    while True:
        jobityjab()
        print('waiting. . . ')
        time.sleep(600)
