from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Locators import conversation_flow
from data import data

chrome_options = webdriver.ChromeOptions()

prefs = {"profile.default_content_setting_values.notifications" : 2}

chrome_options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(chrome_options=chrome_options)

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
        driver.close()

def add_showMsg():
        convType = conversation_flow.convStep_type.replace('@@@', 'Show a message')
        driver.find_element_by_xpath(convType).click()

def create_convStep(stepName):
    try:
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'AddNewStepButton')))
        element.click()

        convType = conversation_flow.convStep_type.replace('@@@', stepName)
        driver.find_element_by_xpath(convType).click()

        preview_text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, conversation_flow.preview_sampleText)))
        preview_text.click()

        input_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, conversation_flow.showMessage_input)))
        action = ActionChains(driver)
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
            # driver.close()
        else:
            raise AssertionError
    except AssertionError:
        print("Success message not visible")
        driver.close()

def del_step(stepName):
    try:
        ellipses_loc = conversation_flow.del_step_ellipses.replace('@@@', stepName)
        ellipses = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ellipses_loc)))
        ellipses.click()

        driver.find_element_by_xpath(conversation_flow.del_step).click()
    except:
        print("Some error occurred!")
        driver.close()

signin(data.emailID_val, data.password_Val, data.URL)
create_convStep('Show a message')
del_step('Show a message')