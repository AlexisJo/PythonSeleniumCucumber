from selenium import webdriver
from src.helpers.autoLocators import locatorToFind
from src.scripts.ouvrirPage import driver
from selenium.common.exceptions import NoSuchElementException 

def cliquerSurSiBesoin(locator) :

    driver.implicitly_wait(3)
    try:
        localisation = locatorToFind(locator)
        element = driver.find_element_by_xpath(localisation)
        element.click()
    except NoSuchElementException:
        print("element not found")

