import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


CHROME_DRIVER_PATH = 'C:\\webdrivers\\chromedriver.exe'


options = Options()
options.headless = True  
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

BASE_URL = "https://www.1mg.com"

def get_diseases_list():
    driver.get(f"{BASE_URL}/all-diseases")
    time.sleep(5)  

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    diseases = []

    
    for link in soup.find_all('a', class_='style__product-name___HASYw'):
        disease_name = link.find('div').text.strip()
        disease_url = BASE_URL + link['href']
        print(f"Found disease: {disease_name} with URL: {disease_url}")
        diseases.append((disease_name, disease_url))
    
    print(f"Total diseases found: {len(diseases)}")
    return diseases

def get_disease_details(disease_name, disease_url):
    driver.get(disease_url)
    time.sleep(5)  
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Get the disease name
    disease_name_tag = soup.find('h1', class_='l1Bold')
    disease_name = disease_name_tag.text.strip() if disease_name_tag else "Unknown Disease"

    def get_section_data(section):
        section_data = soup.find('h2', text=section)
        if section_data:
            p_tag = section_data.find_next('p')
            if p_tag:
                return p_tag.text.strip()
        return None
    
    disease_data = {
        'Disease Name': disease_name,
        'URL': disease_url,
        'Overview': get_section_data('Overview'),
        'Key Facts': get_section_data('Key Facts'),
    }

    print(f"Scraped data for {disease_name}")
    return disease_data

def scrape_all_diseases():
    diseases_list = get_diseases_list()
    all_diseases_data = []
    
    
    for disease_name, disease_url in diseases_list[:10]:
        disease_data = get_disease_details(disease_name, disease_url)
        if disease_data:
            all_diseases_data.append(disease_data)
        time.sleep(1)  
    
    
    with open('diseases_data.json', 'w') as f:
        json.dump(all_diseases_data, f, indent=4)
    
    print(f"Total diseases scraped: {len(all_diseases_data)}")


scrape_all_diseases()


driver.quit()
