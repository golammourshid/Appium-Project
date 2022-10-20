import base64
import os.path
import sys
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from appium import webdriver

# "appPackage": "com.google.android.contacts",
# "appActivity": "com.google.android.apps.contacts.activities.peopleActivity",              "appActivity": "com.cricbuzz.android.lithium.app.view.activity.SplashActivity",
desired_cap = {
    "platformName": "Android",
    "appium:deviceName": "d18d2eb7",
    "appium:appPackage": "org.telegram.messenger",
    "appium:appActivity": "org.telegram.ui.LaunchActivity",
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

driver.implicitly_wait(5)
driver.start_recording_screen()
xpath = "//android.widget.TextView[@text='Start Messaging']"
driver.find_element(By.XPATH, xpath).click()
xpath = "//android.widget.TextView[@text='CONTINUE']"
driver.find_element(By.XPATH, xpath).click()
driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
time.sleep(1)
driver.implicitly_wait(15)
xpath = "//android.widget.TextView[@bounds='[94,847][881,972]']"
driver.find_element(By.XPATH, xpath).click()
xpath = "//android.widget.ImageView[@bounds='[948,91][1080,245]']"
driver.find_element(By.XPATH, xpath).click()
xpath = "//android.widget.EditText[@text='Search']"
driver.find_element(By.XPATH, xpath).send_keys('Bangladesh')
driver.execute_script('mobile: performEditorAction', {'action': 'search'})
xpath = "//android.widget.TextView[@text='🇧🇩 Bangladesh']"
driver.find_element(By.XPATH, xpath).click()
xpath = "//android.widget.EditText[@bounds='[337,1081][942,1180]']"
driver.find_element(By.XPATH, xpath).send_keys('1521413688')
time.sleep(2)
xpath = "//android.view.View[@bounds='[860,1569][1014,1723]']"
driver.find_element(By.XPATH, xpath).click()
driver.implicitly_wait(10)
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(932, 1639)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

time.sleep(1)
xpath = "//android.widget.TextView[@text='CONTINUE']"
driver.find_element(By.XPATH, xpath).click()
time.sleep(1)
driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()

time.sleep(12)
xpath = "//android.view.ViewGroup[@bounds='[0,643][1080,842]']"
driver.find_element(By.XPATH, xpath).click()

driver.implicitly_wait(100)
j = .99
for i in range(901):
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//android.widget.EditText[@bounds='[138,2278][810,2400]']").send_keys(
        "{:.2f}".format(j))
    time.sleep(0.075)
    driver.find_element(By.XPATH, "//android.view.View[@bounds='[948,2268][1080,2400]']").click()
    j = j + 0.01
    time.sleep(0.075)

video_rawdata = driver.stop_recording_screen()
video_name = 'screen_record_' + time.strftime('%Y-%m-%d_%H-%M-%S')
img_name = 'screen_shot_' + time.strftime('%Y-%m-%d_%H-%M-%S')
filepath = os.path.join('C:/Users/user/PycharmProjects/AppiumProjects/Video/', video_name + '.mp4')

# Taking screenshot
# driver.save_screenshot('C:/Users/user/PycharmProjects/AppiumProjects/Image/'+img_name+'.png')

with open(filepath, 'wb') as vd:
    vd.write(base64.b64decode(video_rawdata))
