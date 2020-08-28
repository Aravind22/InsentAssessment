from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from Locators import conversation_flow
from data import data
import time

chrome_options = webdriver.ChromeOptions()

prefs = {"profile.default_content_setting_values.notifications" : 2}

chrome_options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(chrome_options=chrome_options)
action = ActionChains(driver)

def signin(emailVal, passwordVal, url):
    try:   
        driver.get(url)
        driver.maximize_window()

        emailID = driver.find_element_by_xpath(conversation_flow.email_insent)
        emailID.send_keys(emailVal)

        password = driver.find_element_by_xpath(conversation_flow.password_insent)
        password.send_keys(passwordVal)

        driver.find_element_by_xpath(conversation_flow.login_btn).click()

        con_str = conversation_flow.conversation_name.replace('@@@',data.emailID_val)
        con_str = con_str.replace('###',data.conversation_name)

        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, con_str)))
        element.click()

        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, conversation_flow.conversation_flow)))
        element.click()
    except:
        print("Some error occurred while signing in")
        closeBrowser()

def create_convStep(stepName):
    try:
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'AddNewStepButton')))
        element.click()

        convType = conversation_flow.convStep_type.replace('@@@', stepName)
        driver.find_element_by_xpath(convType).click()
    except:
        print("Some exception occurred")
def showMessage():
    try:
        preview_text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, conversation_flow.preview_sampleText)))
        preview_text.click()

        input_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, conversation_flow.showMessage_input)))
        action.move_to_element(input_field).perform()
        action.click(on_element=input_field).perform()
        opened_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, conversation_flow.showMessage_input_opened)))
        opened_input.clear()

        emptyText = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, conversation_flow.empty_input_field)))
        assert emptyText is not None
        driver.save_screenshot('./screenshots/emptyInputField.png')

        emptyText.click()
        driver.find_element_by_xpath(conversation_flow.showMessage_input_opened_closed).send_keys(data.input_text_1)

        save_btn = driver.find_element_by_xpath(conversation_flow.save_conv_btn)
        action.move_to_element(save_btn).perform()
        action.click(on_element=save_btn).perform()
        driver.find_element_by_xpath(conversation_flow.preview_btn).click()
        success_msg = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, conversation_flow.save_success_alert)))
        if success_msg is not None :
            driver.save_screenshot('./screenshots/convSaved.png')
        else:
            raise AssertionError
    except AssertionError:
        print("Success message not visible")
        closeBrowser()

def del_step(stepName):
    try:
        ellipses_loc = conversation_flow.del_step_ellipses.replace('@@@', stepName)
        ellipses = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ellipses_loc)))
        ellipses.click()

        driver.find_element_by_xpath(conversation_flow.del_step).click()
    except:
        print("Some error occurred!")
        closeBrowser()

def verify_Preview(stepName):
    if stepName in 'Capture user data':
        FieldName = driver.find_element_by_xpath(conversation_flow.field_dd)
        FieldName.click()
        action.send_keys(data.Field_Name)
        action.send_keys(Keys.RETURN)
        action.perform()
    elif stepName in 'Show a message':
        pass
    elif stepName in 'Show plain text input':
        elem = driver.find_element_by_xpath(conversation_flow.plainText_ip)
        if elem is not None:
            return True
        else:
            return False
    elem_loc = conversation_flow.field_heading.replace('@@@', data.Field_Name)
    elements = driver.find_elements_by_xpath(elem_loc)
    if len(elements) ==  2 :
        return True
    else:
        return False
    closeBrowser()

def add_conditions(stepName):
    try:
        ellipses_loc = conversation_flow.del_step_ellipses.replace('@@@', stepName)
        ellipses = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ellipses_loc)))
        ellipses.click()

        driver.find_element_by_xpath(conversation_flow.add_condition_step).click()
        conditionheading = driver.find_element_by_xpath(conversation_flow.conHeading)
        if conditionheading is not None:
            return True
        else:
            return False
    except:
        print("Some error occurred!")
        closeBrowser()

def remCondition(stepName):
    try:
        driver.find_element_by_xpath(conversation_flow.conHeading).click()
        ellipses_loc = conversation_flow.del_step_ellipses.replace('@@@', stepName)
        ellipses = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ellipses_loc)))
        ellipses.click()

        driver.find_element_by_xpath(conversation_flow.rem_condition_step).click()
    except NoSuchElementException:
        pass
    closeBrowser()
    return True

def add_Redirect(redirectType, pathName1="MyPath", pathName2="SecondPath"):
    driver.find_element_by_xpath(conversation_flow.add_redirect_btn).click()
    typeLoc = conversation_flow.field_heading.replace('@@@', redirectType)
    driver.find_element_by_xpath(typeLoc).click()
    if 'path' in redirectType:
        driver.find_element_by_xpath(conversation_flow.redirectPathField).click()
        action.send_keys(pathName1)
        action.send_keys(Keys.RETURN)
        action.perform()
    else:
        #In-Progress
        pass
    closeBrowser()

def add_path(pathName="MyPath"):
    try:
        addPath_tbn_loc = conversation_flow.field_heading.replace('@@@','Add new path')
        driver.find_element_by_xpath(addPath_tbn_loc).click()

        path_inp_loc = conversation_flow.path_inputs.replace('@@@', 'New path')
        pathElems = driver.find_elements_by_xpath(path_inp_loc)
        pathElems[-1].send_keys(Keys.CONTROL + 'a')
        pathElems[-1].send_keys(Keys.BACKSPACE)
        pathElems[-1].send_keys(pathName)
        pathElems[-1].send_keys(Keys.RETURN)
    except:
        print('Some error occurred')

def rem_path():
    try:
        pathInp_loc = conversation_flow.path_inputs.replace('@@@', 'MyPath')
        pathElems = driver.find_element_by_xpath(pathInp_loc)
        action.move_to_element(pathElems).perform()
        time.sleep(5)
        rem_icon = driver.find_element_by_xpath(conversation_flow.remove_path_icon)
        action.move_to_element(rem_icon).perform()
        action.click(on_element=rem_icon).perform()
    except:
        print("Some error occurred")

def verify_delPath():
    try:
        toolTip = driver.find_element_by_xpath(conversation_flow.empty_pathField)
        if toolTip is not None:
            closeBrowser()
            return True
    except NoSuchElementException:
        pass
    closeBrowser()
    return False

def closeBrowser():
    driver.close()

signin(data.emailID_val, data.password_Val, data.URL)
add_path()
add_Redirect('Go to path')
rem_path()
# create_convStep('Show plain text input')
# print(add_conditions('Show plain text input'))
# print(remCondition('Show plain text input'))
# verify_Preview('Show plain text input')
# del_step('Show a message')