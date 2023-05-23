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
element4 = driver.find_element_by_xpath("//[@text='Pilih Kurir']")
element4.click()
element5 = driver.find_element_by_xpath("//[@bound='[871,1149][962,1240]']")
element5.click()
element6 = driver.find_element_by_xpath("//[@text='Gunakan Kurir Terpilih']")
element6.click()
driver.implicitly_wait(5)
element7 = driver.find_element_by_xpath("//[@text='Pilih metode pembayaran']")
element7.click()
driver.implicitly_wait(5)
element8 = driver.find_element_by_xpath("//[@bound='[902,866][992,957]']")
element8.click()
element9 = driver.find_element_by_xpath("//[@text='Gunakan Metode Terpilih']")
element9.click()
driver.quit()