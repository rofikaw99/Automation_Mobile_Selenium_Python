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
element1 = driver.find_element_by_xpath("//[@bound='[831,134][872,175]']")
element1.click()
driver.implicitly_wait(5)
element2 = driver.find_element_by_xpath("//[@text='Cari di eDOT']")
element2.click()
element2.send_keys('mi')
element3 = driver.find_element_by_xpath("//[@bound='[201,137][227,163]']")
element3.click()
driver.implicitly_wait(5)
element4 = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[8]')
element4.click()
element5 = driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_foreground_only_button")
element5.click()
element = driver.find_element_by_xpath("//[@text='Indomie Goreng Sambal Rica-Rica 85g']")
if element.is_displayed():
    print("Element is displayed")
else:
    print("Element is not displayed")
driver.implicitly_wait(5)
driver.quit()