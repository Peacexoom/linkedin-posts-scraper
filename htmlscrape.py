from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome('chromedriver')


#Replace with you username and password
email = "your-email"
password = "your-password"

time.sleep(10)

#Open login page
browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
time.sleep(20)

#Enter login info:
elementID = browser.find_element(By.ID, 'username')
elementID.send_keys(email)

elementID = browser.find_element(By.ID,'password')
elementID.send_keys(password)
elementID.submit()

time.sleep(10)

#If this doesn't work comment the login part and login manually

#To get this url go to Profile you want to scrape > Show all posts
#Example url = https://www.linkedin.com/in/profilename/recent-activity/all/
browser.get('url-you-want-to-scrape')

time.sleep(10)

last_height = browser.execute_script("return document.body.scrollHeight")

while True:

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(5)

    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


company_page = browser.page_source   

with open("posts.html", "w", encoding="utf-8") as f:
    f.write(company_page)

