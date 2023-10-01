from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
driver.get("https://app.jubelio.com/")

driver.find_element(By.NAME,"email").send_keys("qa.rakamin.jubelio@gmail.com")
driver.find_element(By.NAME,"password").send_keys("Jubelio123!")
driver.find_element(By.TAG_NAME,"button").click()

    