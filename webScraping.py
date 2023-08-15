from selenium import webdriver 
from selenium.webdriver.common.by import By
import pandas as pd

url = "https://datosmacro.expansion.com/demografia/mortalidad"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window() 

data = {'pais': [], 'fecha': [], 'muerte': [], 'tasa de mortalidad': [], 'variacion' : []}

  
boton = driver.find_element(By.ID, "didomi-notice-agree-button")
boton.click()
elements = driver.find_elements(By.CSS_SELECTOR, "#tb1 tbody > tr") 

for item in elements:
    data["pais"].append(item.find_element(By.CSS_SELECTOR, "td:nth-child(1) a").text)
    data["fecha"].append(item.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text)
    data["muerte"].append(item.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text)
    data["tasa de mortalidad"].append(item.find_element(By.CSS_SELECTOR, "td:nth-child(4)").text) 
    data["variacion"].append(item.find_element(By.CSS_SELECTOR, "td:nth-child(6)").text) 

    
driver.quit()

df = pd.DataFrame(data)
df.to_csv("NombreDelaBasedeDatos.csv", index=False) 