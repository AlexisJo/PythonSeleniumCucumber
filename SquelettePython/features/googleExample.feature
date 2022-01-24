@excel

Feature: googleExample

  Scenario: run a simple test
     Given J'ouvre la page "https://google.com/"
     And J'attends "5" secondes
     When Je clique sur "Accepter Google Cookies"
     And J'ecris "Hardis Group" dans le champ "Champ Recherche"
     And Dans le champ "Champ Recherche" j'appuie sur entree

#Any Scenario Outline using excel to define the steps need to have 'excel' in its name
  Scenario Outline: using excel to search and extract information
    Given J'ouvre la page "https://google.com/"
    And J'envoie une variable <Variable Example> dans le champ "Champ Recherche"
      Examples:
          | Variable Example |
    And Dans le champ "Champ Recherche" j'appuie sur entree
    And J'extrait les donnees de "Titre premier resultat" dans l'excel "extractionExample"