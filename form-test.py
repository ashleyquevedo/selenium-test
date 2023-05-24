from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# options: allows window to stay open, another approach to resolve this for testing would be to use time
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(executable_path="driver/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(3)

driver.get("https://forms.gle/5MkcFovDu63dv8Z69")

# hardcoded values, next step would be to bring in information from separate config file
role = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
role.send_keys("software engineer")

location = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
location.send_keys("New York, NY")

setting_pref = "remote"

if setting_pref == "remote":
  setting = driver.find_element("xpath", '//*[@id="i16"]')

if setting:
  setting.click()

submit = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
submit.click()