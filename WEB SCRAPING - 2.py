from matplotlib.pyplot import title
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
import csv
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers = ["Star_name", "Distance", "Mass", "Radius"]
    star_data = []
    for i in range(0, 50):
       page = requests.get(START_URL)
       soup = BeautifulSoup(page.text, "html.parser")
       star_table = soup.find_all("table",attrs={"class", "wikitable sortable jquery-tablesorter"})
       temp_list = []
       table_rows = star_table.find_all("tr")

       for tr in table_rows:
            td_tags = tr.find_all("td")
            row = [i.text.rstrip() for i in td_tags]
            temp_list.append(row)
      
       temp_list1 = []

       for index, td_tag in enumerate(temp_list):
               #print(td_tag)
                if index == 0:
                    a_tag = td_tag.find_all("a")
                    temp_list1.append(a_tag)
                elif index == 5:
                   temp_list1.append(td_tag)                   
                elif index == 8:
                   temp_list1.append(td_tag)
                elif index == 9:
                   temp_list1.append(td_tag)
                else:
                    try:
                        temp_list1.append(td_tag)
                    except:
                        temp_list1.append("")
    star_data.append(temp_list1)

    with open("WEB SCRAPING - 2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)

scrape()