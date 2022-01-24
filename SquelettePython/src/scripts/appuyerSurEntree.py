from src.helpers.autoLocators import locatorToFind
from src.scripts.ouvrirPage import driver

def appuyerSurEntree(locator) :

    driver.implicitly_wait(10)
    localisation = locatorToFind(locator)
    element = driver.find_element_by_xpath(localisation)
    element.send_keys(u'\ue007')

