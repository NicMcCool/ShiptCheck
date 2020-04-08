from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from pushbullet.pushbullet import PushBullet
from bs4 import BeautifulSoup
from time import sleep
import config, re, time, schedule

# ESTABLISH PUSHBULLET API
pb = PushBullet(config.pbAPI)

# ESTABLISH CHROME HEADLESS SESSION
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36")

# LOG IN TO GOOGLE THEN MIGRATE LOGIN THROUGH SHIPT
def ShiptScrape():
    # Open Headless Chrome using options above
    driver=webdriver.Chrome(options=chrome_options, executable_path=config.driverLoc)
    sleep(3)

    # Log into Chrome
    driver.get(config.googlePage)
    sleep(3)
    driver.find_element_by_xpath('//input[@type="email"]').send_keys(config.userID)
    driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
    sleep(3)
    driver.find_element_by_xpath('//input[@type="password"]').send_keys(config.userPW)
    driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
    sleep(2)

    # Migrate Chrome login to Shipt
    driver.get('https://shop.shipt.com/')
    sleep(2)
    driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[3]/form[2]/button').click()
    sleep(5)

    # Parse Shipt main page for Header text
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    headerText = soup.find("header", {"class": "fixed w-100 z-999"}).text
    regPat = re.compile(r"check\sback\ssoon", re.IGNORECASE)

    # Act on results of header scrape
    if regPat.search(headerText) != None:
        # End job run
        print("Delivery not available.")
        driver.quit()

    else:
        # Send Pushbullet notification
        devices = pb.getDevices()
        pb.pushNote(devices[0]["iden"], 'Shipt Notification', 'You can schedule delivery now!')
        driver.quit()

schedule.every(10).minutes.do(ShiptScrape)

while True:
    schedule.run_pending()
    time.sleep(1)