import fake_headers,requests,random,json
from requests import status_codes
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class All_base: 
  
    headers = fake_headers.Headers(browser="Chrome",os="Ubuntu",headers=True).generate()
    base_url ="https://stage.05.ru"
    client_id = 'main'
    client_secret = 'ac178876-b829-11e9-b8c8-ac1f6b94fd9c'
    value_range = 3
    payload=f'grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}'
    response = requests.request("POST", base_url+"/api/v2/oauth/token", headers={'Content-Type': 'application/x-www-form-urlencoded'}, data=payload)
    token = response.json() 
  
    def delete_user_close(self):
        if self.base_url == "https://stage.05.ru":
            response = requests.request("GET",self.base_url+"/api/v1/service/delete/users/79997777777?access_token=b0e90087-f447-11eb-9c0e-f2dfe89e1ff8")
        else:   
            response = requests.request("GET",self.base_url+"/api/v1/service/delete/users/79997777777?access_token=gy5QKmD9Kx67Hn4R") 
        #headers=self.headers)
        return response.json()["success"]

    def api_autorization(self):
        payload=f'grant_type=password&client_id={self.client_id}&client_secret={self.client_secret}&username=89997777777&password=111111'
        response = requests.request("POST", url = self.base_url +"/api/v1/oauth/token", headers={'Content-Type': 'application/x-www-form-urlencoded'}, data=payload)    
        return response    
    def close_all_favourites(self):
        payload={}  
        variable_for_test = self.api_autorization()
        token = variable_for_test.json()
        if variable_for_test.status_code == 200:
            response = (requests.request("DELETE",url = self.base_url+"/api/v1/favorite/all", headers={'Authorization': f'Bearer {token["result"]["access_token"]}'}, data=payload)).json()
            return response
        return f"{variable_for_test}" 
    def catalog(self):
        token = self.token
        response = requests.request("GET", self.base_url +"/api/v1/catalog/sections", headers = {'Authorization': f'Bearer {token["result"]["access_token"]}'})
        sections = response.json()["result"]
        catalog_all = []  
        def catalog_in(sections):
            
            for section in sections:
                sectionPagePath = section["SECTION_PAGE_PATH"]
                catalog_all.append(sectionPagePath)
                if "CHILDREN" in section:
                    catalog_in(section["CHILDREN"])
        catalog_in(sections)
        return(catalog_all)
        
    def test_catalog(self):
      spisok=[]
      t = self.catalog()
      for i in range(self.value_range):
        while True:
            section = random.randint(1, len(t)-1)
            response = requests.request("GET", f"{self.base_url}{t[section]}", headers=self.headers)
            tree = BeautifulSoup(response.content, 'html.parser')
            if len(tree.find_all('div',{'class': 'catalog-page'})) == 0:
                continue
            spisok.append(f"{self.base_url}{t[section]}")
            break
      return spisok
    def all_tovary(self):
        token = self.token
        payload={}
        response = requests.request("GET", url =self.base_url + "/api/v1/catalog/paths", headers={'Authorization': f'Bearer {token["result"]["access_token"]}'}, data= payload)
        
        return response
