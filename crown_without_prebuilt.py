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
    "appium:appPackage": "uni.UNI161FE76",
    "appium:appActivity": "io.dcloud.PandoraEntry",
    "newCommandTimeout": 600
}


driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(5)
driver.start_recording_screen()
driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
time.sleep(1)
driver.implicitly_wait(5)
driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
driver.implicitly_wait(15)
time.sleep(10)
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(527, 2311)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

driver.implicitly_wait(25)

xpath = "//android.widget.TextView[@text='Please enter the account number']"
driver.find_element(By.XPATH, xpath).click()
xpath = "//android.widget.EditText[@bounds='[247,1028][976,1133]']"
driver.find_element(By.XPATH, xpath).send_keys("dolantor")
xpath = "//android.widget.TextView[@text='Please input a password']"
driver.find_element(By.XPATH, xpath).click()
xpath = "//android.widget.EditText[@bounds='[247,1246][976,1345]']"
driver.find_element(By.XPATH, xpath).send_keys("antor1234")
driver.execute_script('mobile: performEditorAction', {'action': 'go'})

xpath = "//android.widget.TextView[@text='determine']"
driver.find_element(By.XPATH, xpath).click()
time.sleep(5)
driver.implicitly_wait(25)
time.sleep(5)
driver.find_element(By.XPATH, xpath).click()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(527, 2311)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()


def grab_order():
    driver.implicitly_wait(15)
    xpath = "//android.widget.TextView[@text='Start grabbing orders']"
    driver.find_element(By.XPATH, xpath).click()
    driver.implicitly_wait(20)


def submit_order():
    driver.implicitly_wait(15)
    xpath = "//android.widget.TextView[@text='Submit now']"
    driver.find_element(By.XPATH, xpath).click()
    driver.implicitly_wait(15)


for i in range(30):
    xpath = "//android.widget.TextView[@bounds='[404,1474][687,1537]']"
    prev_order_count = driver.find_element(By.XPATH, xpath).get_attribute('text')
    print('grabbing ' + prev_order_count)
    xpath = "//android.widget.TextView[@bounds='[107,1730][390,1793]']"
    prev_commission = driver.find_element(By.XPATH, xpath).get_attribute('text')
    print('previous commission ' + prev_commission)
    for j in range(70):
        new_order_count = driver.find_element(By.XPATH, "//android.widget.TextView[@bounds='[404,1474][687,1537]']").get_attribute('text')
        if prev_order_count == new_order_count:
            driver.implicitly_wait(15)
            print('grabbing new order ' + new_order_count)
            try:
                grab_order()
                # time.sleep(11)
            except:
                print("Oops! Grabbing failed!", sys.exc_info()[0], "occurred.")
                time.sleep(2)
            time.sleep(11)
            try:
                submit_order()
            except:
                print("Oops! Submitting failed", sys.exc_info()[0], "occurred.")
                time.sleep(2)

            time.sleep(11)
        else:
            break

video_rawdata = driver.stop_recording_screen()
video_name = 'screen_record_' + time.strftime('%Y-%m-%d_%H-%M-%S')
img_name = 'screen_shot_' + time.strftime('%Y-%m-%d_%H-%M-%S')
filepath = os.path.join('C:/Users/user/PycharmProjects/AppiumProjects/Video/', video_name + '.mp4')

# Taking screenshot
# driver.save_screenshot('C:/Users/user/PycharmProjects/AppiumProjects/Image/'+img_name+'.png')

with open(filepath, 'wb') as vd:
    vd.write(base64.b64decode(video_rawdata))
