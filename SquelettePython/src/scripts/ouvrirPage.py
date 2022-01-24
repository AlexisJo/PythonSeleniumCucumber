import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
def ouvrirPage(URL):
    driver.maximize_window()
    final_url = URL.replace("\"", "")
    print("The URL IS GODDAMN : " + final_url)
    driver.get(final_url)
    time.sleep(5)
