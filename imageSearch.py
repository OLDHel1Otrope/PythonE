import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def google_image_search(file_path):
    driver = webdriver.Chrome()

    try:
        driver.maximize_window()
        driver.get('https://images.google.com/')
        driver.implicitly_wait(10)
        camera_icon = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Search by image']"))
        )
        camera_icon.click()
        time.sleep(1)
        upload_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/c-wiz/div[2]/div/div[3]/div[2]/div/div[2]/span"))
        )
        time.sleep(1)
        file_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file'][@name='encoded_image']"))
        )
        file_input.send_keys(file_path)
        time.sleep(10)
        results = []
        result_elements = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='G19kAf ENn9pd']"))
        )[:5]

        for index, element in enumerate(result_elements):
            try:
                #title
                title_element = element.find_element(By.XPATH, ".//div[@class='UAiK1e']")
                title = title_element.text
                
                #image URL
                image_element = element.find_element(By.XPATH, ".//img[@class='wETe9b jFVN1']")
                image_url = image_element.get_attribute("src")
                
                #page URL
                page_url_element = element.find_element(By.XPATH, ".//a[@class='GZrdsf oYxtQd lXbkTc ']")
                page_url = page_url_element.get_attribute("href")

                #results list
                results.append({
                    'title': title,
                    'image_url': image_url,
                    'page_url': page_url
                })
            except Exception as e:
                print(f"Error extracting result {index + 1}: {e}")
        with open('results.json', 'w') as file:
            json.dump(results, file, indent=4)

    finally:
        #close driver
        driver.quit()

#example
google_image_search("C:\\Users\\ALO\\Desktop\\react\\bpro1\\pythonbackend\\img3.jpg")
