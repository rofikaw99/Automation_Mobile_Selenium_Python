from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from appium.webdriver.common.mobileby import MobileBy
from Login_on_EDOT_App import login
import time

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'virtualdevice'
desired_caps['appPackage'] = 'com.pmaapp.ehashtag'
desired_caps['appActivity'] = 'com.pmaapp.ehashtag.MainActivity'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['showAndroidWindowHierarchy'] = True

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)




login()
element = driver.find_element_by_xpath("//[@bound='[295,1963][352,2019]']")
element.click()
driver.implicitly_wait(5)
element1 = driver.find_element_by_xpath("//[@bound='[978,135][1024,187]']")
element1.click()
driver.implicitly_wait(5)
element2 = driver.find_element_by_xpath("//[@bound='[87,632][142,687]']")
element2.click()
element3 = driver.find_element_by_xpath("//[@bound='[717,1795][1039,1883]']")
element3.click()
driver.implicitly_wait(5)
element4 = driver.find_element_by_xpath("//[@text='Tambahkan titik lokasi (opsional)']")
element4.click()
driver.implicitly_wait(5)
element5 = driver.find_element_by_xpath("//[@text='Jl. Kedoya Raya No.RT.2, RT.2, Kedoya Utara, Kec. Kb. Jeruk, Kota Jakarta Barat, Daerah Khusus Ibukota Jakarta 11520, Indonesia']")
element5.click()
driver.implicitly_wait(5)
driver.quit()
