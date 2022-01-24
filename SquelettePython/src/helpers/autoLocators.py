import os, json
#string = ''.join([str(item) for item in json_files])

#key="Champ Recherche"
def locatorToFind(keyVal) : 
    # search all json files in directory
    path_to_json = 'src/locators/'
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    # print(json_files)
    # load the json data
    for jsonToOpen in json_files:
        # print(path_to_json+jsonToOpen)
        f = open(path_to_json+jsonToOpen,)
        customer = json.load(f)
        # Search the key value using 'in' operator
        if keyVal in customer:
        # Print the success message and the value of the key
            # print("%s is found in JSON data" %keyVal)
            # print("The value of", keyVal,"is", customer[keyVal])
            verif = True
            return customer[keyVal]
        else:
            # Print the message if the value does not exist
            # print(keyVal+" is not found in JSON data :"+path_to_json+jsonToOpen)
            verif = False
            #return NameError
    if verif == False:
       return keyVal 
#locatorToFind(key)
