from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from appium.webdriver.common.mobileby import MobileBy
import time

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'virtualdevice'
desired_caps['appPackage'] = 'com.pmaapp.ehashtag'
desired_caps['appActivity'] = 'com.pmaapp.ehashtag.MainActivity'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['showAndroidWindowHierarchy'] = True

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(2)
element = driver.find_element(By.CLASS_NAME, 'android.widget.ImageView')
if element.is_displayed():
    print("Element is displayed")
else:
    print("Element is not displayed")
element1 = driver.find_element(By.CLASS_NAME, 'android.widget.TextView')
element1.click()
time.sleep(2)
element2 = driver.find_element(By.CLASS_NAME, 'android.widget.TextView')
element2.click()
time.sleep(2)
element3 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'android.widget.EditText')))
element3.click()
element3.send_keys('rofik.awaludin@edenfarm.id')
element4 = driver.find_element(By.CLASS_NAME, 'android.widget.CheckBox')
element4.click()
element5 = driver.find_element_by_id("nextLogin1")
element5.click()
element6 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'android.widget.EditText')))
element6.click()
element6.send_keys('@Abcde123')
element7 = driver.find_element(By.CLASS_NAME, 'android.widget.ImageView')
element7.click()
element8 = driver.find_element(By.CLASS_NAME, 'com.horcrux.svg.SvgView')
element8.click()
time.sleep(2)




