from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
import time

url = "https://www.gob.mx/curp/"
day = "01"
month = "01"
year = "2000"
nombre = "TU NOMBRE"
apellido_paterno = "TU APELLIDO PATERNO"
apellido_materno = "TU APELLIDO MATERNO"
gender = "Mujer"  # o "Hombre"
city = "CIUDAD DE MÉXICO"  # o "ESTADO DE MÉXICO", etc.
try:
    options = uc.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')  # Evitar la detección de automatización
    options.add_argument('--use-fake-ui-for-media-stream')  # Permitir los permisos automáticamente
    options.add_argument('--disable-geolocation')
    options.add_argument('--disable-infobars')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36')
    browser = uc.Chrome(options=options)
    browser.get(url)
    browser.implicitly_wait(25)
    browser.execute_script("window.scrollTo(0, 100);")
    datos_personales_tab = browser.find_element(By.ID, "datos")
    datos_personales_tab.click()
    time.sleep(2)
    nombre_input = browser.find_element(By.ID, "nombre")
    nombre_input.send_keys(nombre)
    apellido_paterno_input = browser.find_element(By.ID, "primerApellido")
    apellido_paterno_input.send_keys(apellido_paterno)
    apellido_materno_input = browser.find_element(By.ID, "segundoApellido")
    apellido_materno_input.send_keys(apellido_materno)
    day_input = browser.find_element(By.ID, "diaNacimiento")
    day_input.send_keys(day)
    day_input = browser.find_element(By.ID, "mesNacimiento")
    day_input.send_keys(month)
    day_input = browser.find_element(By.ID, "selectedYear")
    day_input.send_keys(str(year))
    sexo_select = browser.find_element(By.ID, "sexo")
    sexo_select.send_keys(gender)
    entidad_select = browser.find_element(By.ID, "claveEntidad")
    entidad_select.send_keys(city)  # o "ESTADO DE MÉXICO", etc.
    time.sleep(2)
    buscar_button = browser.find_element(By.ID, "searchButton")
    buscar_button.click()
    time.sleep(2)
    contenedor = browser.find_element(By.CLASS_NAME, "col-md-7")
    tabla = contenedor.find_element(By.TAG_NAME, "table")
    filas = tabla.find_elements(By.TAG_NAME, "tr")
    primera_fila = filas[0]
    celdas = primera_fila.find_elements(By.TAG_NAME, "td")
    celda = {"nameField": celdas[0].text, "curpField": celdas[1].text}
except Exception as e:
    celda = {"nameField": "CURP", "curpField": "SIN DATOS"}
finally:
    print(celda)
    browser.quit()