import json
import requests


class Token_api:
    url = "https://test.05.ru/api/v2/oauth/token"
    headers = {
        
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    def work_json():
        with open('data_file.json', 'r', encoding='utf-8') as f: 
            token = json.load(f)
        return token
    
    
    def get_token():
        
        client_id = 'main'
        client_secret = 'ac178876-b829-11e9-b8c8-ac1f6b94fd9c'
        payload=f'grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}'
        headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
    }

        response = requests.request("POST", Token_api.url, headers=headers, data=payload)
        with open("data_file.json", "w") as write_file:
            json.dump(response.json(), write_file)

    def restart_token():
        
        
        url = "https://test.05.ru/api/v2/oauth/token"

        payload=f'grant_type=refresh_token&refresh_token={Token_api.work_json()["result"]["refresh_token"]}'
        

        response = requests.request("POST", url, headers=Token_api.headers, data=payload)

        with open("data_file.json", "w") as write_file:
            json.dump(response.json(), write_file)
    def catalog_json():
        url = "https://test.05.ru/api/v1/catalog/sections" 
        payload={}
        test = (Token_api.work_json())["result"]["access_token"]
        
        headers = {
        'Authorization': f'Bearer {test}'
}

        response = requests.request("GET", url, headers=headers, data=payload)

        
       
        #my_file = open("catalog_all.py","a+")
        #my_file.write('catalog_all =[')
        #my_file.close()
        return(Token_api.catalog(response.json()["result"]))
        #my_file = open("catalog_all.py","a+")
        #my_file.write(']\n')  
        #my_file.close()
    def catalog(sections):  
        catalog_all = []  
        def catalog_in(sections):
            
            for section in sections:
                sectionPagePath = section["SECTION_PAGE_PATH"]
                catalog_all.append(sectionPagePath)
                #my_file = open("catalog_all.py","a+")
                #my_file.write(f'"{sectionPagePath}",\n')
                #my_file.close()
                if "CHILDREN" in section:
                    catalog_in(section["CHILDREN"])
        catalog_in(sections)
        return(catalog_all)   
Token_api.restart_token()      
        




   

    
    
        




