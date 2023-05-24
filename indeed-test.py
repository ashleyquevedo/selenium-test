from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# options: allows window to stay open, another approach to resolve this for testing would be to use time
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(executable_path="driver/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.indeed.com/")

searchbox = driver.find_element("xpath", "/html/body/div/div[1]/div/span/div[3]/div[1]/div/div/div/div/form/div/div[1]/div/div[1]/div/div[2]/input")

searchbox.send_keys("software engineer")

searchbox.send_keys(Keys.RETURN)

# note: bot detection activates during this test