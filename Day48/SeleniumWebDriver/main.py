from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://en.wikipedia.org/wiki/Main_Page")

search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("Python")
search_box.send_keys(Keys.ENTER)

sleep(10)


# driver.close()  # Close Chrome Tab
# driver.quit()  # Quit Chrome program