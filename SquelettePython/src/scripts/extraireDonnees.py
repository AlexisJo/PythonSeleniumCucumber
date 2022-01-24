from src.scripts.attendreSecondes import attendreSecondes
from src.helpers.autoLocators import locatorToFind
from src.scripts.ouvrirPage import driver
from selenium.common.exceptions import NoSuchElementException 
from openpyxl import load_workbook
import datetime


def extraireDonnees(locator, nom):
    
    localisation = locatorToFind(locator)
    element = driver.find_element_by_xpath(localisation)

    #load excel file
    workbook = load_workbook(filename="src/files/"+nom+".xlsx")

    # Open workbook
    worksheet = workbook.active
    
    #add the text from the element to the excel
    worksheet.append({'A':element.text})

    #Save modifications
    workbook.save(filename="src/files/"+nom+".xlsx")
    attendreSecondes('2')

