"""prereq_scraper.py"""
from lxml import html
import requests

def prereq_scraper():
    """prereqscraper()"""
    url = "https://cse.ucsd.edu/undergraduate/courses/prerequisites-cse-undergraduate-classes"
    page = requests.get(url)
    tree = html.fromstring(page.content)

    print page.content

    course_name = tree.xpath("//*[@id='block-cse-content']/article/div/div/table/tbody/tr[2]/td[1]/p/strong")
    print course_name

prereq_scraper()
