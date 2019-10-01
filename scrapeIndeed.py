from bs4 import BeautifulSoup
import requests
page_html = requests.get('https://www.indeed.com/jobs?q=marketing&l=St.+Louis,+MO&start=0').content
soup = BeautifulSoup(page_html, 'html.parser')

job_links = soup.findAll("div", {"class": "title"})

# Going through all of the clickable jobs now...
for current_link in job_links:
    a_link = current_link.findChildren("a", recursive=False)[0]
    page_to_view = a_link.attrs['href']

    # Hey Logan, the print statement here is the HTML of the job description.  This simulates your "click"
    actual_soup = BeautifulSoup(requests.get('https://www.indeed.com/' + page_to_view).content, 'html.parser')
    print(actual_soup)