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

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(2)
element1 = driver.find_element(By.CLASS_NAME, 'android.widget.TextView')
element1.click()
element2 = driver.find_element(By.CLASS_NAME, 'android.view.ViewGroup')
element2.click()
time.sleep(2)
wait = WebDriverWait(driver, 10)
element3 = wait.until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, 'Daftar')))
element3.click()
time.sleep(2)
driver.find_element_by_id('username').click()
driver.find_element_by_id('username').send_keys('email@email.com')
element4 = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.view.View[2]')
element4.click()
recaptcha_frame = WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha/api2/anchor']"))
)
recaptcha_checkbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='rc-anchor-center-container']//div[@class='rc-anchor-checkbox-holder']"))
)
recaptcha_checkbox.click()
element5 = driver.find_element_by_id("nextRegist1")
element5.click()

