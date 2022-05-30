from selenium import webdriver
import time
import random
from fake_useragent import FakeUserAgent
from selenium.webdriver.common.by import By

user_agent = FakeUserAgent()

# options
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={user_agent.random}")

driver = webdriver.Chrome(
    executable_path="utils/misc/googledriver",
    options=options
)

try:
    driver.get(url="https://openbudget.uz/boards/5/118109")
    time.sleep(1)
    #
    # nomer_input = driver.find_element(by=By.XPATH, value=)

except Exception as ex:
    pass
finally:
    driver.close()
    driver.quit()
