from behave import *
import parse
from selenium.webdriver.common.keys import Keys
from src.scripts.appuyerSurEntree import appuyerSurEntree
from src.scripts.attendreSecondes import attendreSecondes
from src.scripts.cliquerSurSiBesoin import cliquerSurSiBesoin
from src.scripts.ecrireDansChamp import ecrireDansChamp
from src.scripts.ouvrirPage import ouvrirPage
from src.scripts.ouvrirPage import driver
from src.scripts.cliquerSur import cliquerSur
from src.scripts.extraireDonnees import extraireDonnees

@parse.with_pattern(r'.*')
def parse_nullable_string(text):
    return text

register_type(NullableString=parse_nullable_string)

@step('J\'ouvre la page {URL:NullableString}')
def step_impl(context, URL):
    context.URL = URL
    ouvrirPage(URL)

@step('J\'appuie sur entree dans le champ {locator}')
def step_impl(context, locator):
    driver.find_element_by_xpath(locator).send_keys(Keys.ENTER)

@step('Je cherche sur google "{text}"')
def step_impl(context, text):
    driver.get(text)

@step('Je clique sur "{text}"')
def step_impl(context, text):
        cliquerSur(text)

@step('Dans le champ "{locator}" j\'appuie sur entree')
def step_impl(context, locator):
        appuyerSurEntree(locator)

@step('Je clique si besoin sur "{text}"')
def step_impl(context, text):
        cliquerSurSiBesoin(text)

@step('J\'ecris "{text}" dans le champ "{locateur}"')
def step_impl(context, text, locateur):
        ecrireDansChamp(text, locateur)

@step('J\'envoie une variable {text:NullableString} dans le champ "{locateur}"')
def step_impl(context, text, locateur):
        context.text = text
        ecrireDansChamp(text, locateur)

@step('J\'extrait les donnees de "{locateur}" dans l\'excel "{excel}"')
def step_impl(context, locateur, excel):
    extraireDonnees(locateur, excel)

@step('J\'attends "{secondes}" secondes')
def step_impl(context, secondes):
    attendreSecondes(secondes)

@step('Je ferme le navigateur')
def step_impl(context):
    driver.quit()

@step('behave will test it for us!')
def step_impl(context):
    assert context.failed is False