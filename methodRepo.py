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
    except Exception as e:
        print(e)
        closeBrowser()

def create_convStep(stepName):
    try:
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'AddNewStepButton')))
        element.click()

        convType = conversation_flow.convStep_type.replace('@@@', stepName)
        driver.find_element_by_xpath(convType).click()
        return True
    except Exception as e:
        print(e)
        closeBrowser()

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
        driver.find_element_by_xpath(conversation_flow.showMessage_input_opened_closed).send_keys(data.Field_Name)

        save_btn = driver.find_element_by_xpath(conversation_flow.save_conv_btn)
        action.move_to_element(save_btn).perform()
        action.click(on_element=save_btn).perform()
        driver.find_element_by_xpath(conversation_flow.preview_btn).click()
        success_msg = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, conversation_flow.save_success_alert)))
        if success_msg is not None :
            driver.save_screenshot('./screenshots/convSaved.png')
            return True
        else:
            raise AssertionError
    except AssertionError:
        return False
        print("Success message not visible")
        closeBrowser()

def del_step(stepName):
    try:
        ellipses_loc = conversation_flow.del_step_ellipses.replace('@@@', stepName)
        ellipses = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ellipses_loc)))
        ellipses.click()

        driver.find_element_by_xpath(conversation_flow.del_step).click()
        driver.save_screenshot('./screenshots/deletedStep.png')
        return True
    except Exception as e:
        print e
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
            driver.save_screenshot('./screenshots/Previewverify.png')
            return True
        else:
            return False
    elem_loc = conversation_flow.field_heading.replace('@@@', data.Field_Name)
    elements = driver.find_elements_by_xpath(elem_loc)
    if len(elements) ==  2 :
        return True
    else:
        return False

def add_conditions(stepName):
    try:
        ellipses_loc = conversation_flow.del_step_ellipses.replace('@@@', stepName)
        ellipses = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ellipses_loc)))
        ellipses.click()

        driver.find_element_by_xpath(conversation_flow.add_condition_step).click()
        conditionheading = driver.find_element_by_xpath(conversation_flow.conHeading)
        if conditionheading is not None:
            driver.save_screenshot('./screenshots/AddedCond.png')
            return True
        else:
            return False
    except Exception as e:
        print(e)
        closeBrowser()

def remCondition(stepName):
    try:
        driver.find_element_by_xpath(conversation_flow.conHeading).click()
        ellipses_loc = conversation_flow.del_step_ellipses.replace('@@@', stepName)
        ellipses = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ellipses_loc)))
        ellipses.click()

        driver.find_element_by_xpath(conversation_flow.rem_condition_step).click()
    except NoSuchElementException:
        driver.save_screenshot('./screenshots/RemovedCond.png')
    except Exception as e:
        print(e)
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
        return True
    else:
        #In-Progress
        pass
    # closeBrowser()

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
        return True
    except Exception as e:
        print(e)
        closeBrowser()

def rem_path():
    try:
        pathInp_loc = conversation_flow.path_inputs.replace('@@@', 'MyPath')
        pathElems = driver.find_element_by_xpath(pathInp_loc)
        action.move_to_element(pathElems).perform()
        time.sleep(5)
        rem_icon = driver.find_element_by_xpath(conversation_flow.remove_path_icon)
        action.move_to_element(rem_icon).perform()
        action.click(on_element=rem_icon).perform()
        return True
    except Exception as e:
        print(e)

def verify_delPath():
    try:
        toolTip = driver.find_element_by_xpath(conversation_flow.empty_pathField)
        driver.save_screenshot('./screenshots/DeletedPath.png')
        if toolTip is not None:
            closeBrowser()
            return True
    except NoSuchElementException:
        pass
    closeBrowser()
    return False

def stepOrderChange():
#Not complete
    elements = driver.find_elements_by_xpath(conversation_flow.stepsDiv)
    if len(elements) < 2:
        print("Steps not enogh to execute this step")
        return False
    else:
        sourceElem = elements[1]
        destElem = elements[2]
        # action.drag_and_drop(elements[2], driver.find_element_by_xpath(conversation_flow.add_redirect_btn))
        action.click_and_hold(elements[1]).pause(4).move_to_element(elements[2]).release(elements[2]).perform()
        # action.perform()

def addDelay(stepName='Show a message', delay='2'):
    delayIpLoc = conversation_flow.delayInput.replace('@@@', stepName)
    delayIp = driver.find_element_by_xpath(delayIpLoc)  
    delayIp.click()
    delayIp.send_keys(Keys.CONTROL + 'a')
    delayIp.send_keys(Keys.BACKSPACE)
    delayIp.send_keys(delay)

    action.move_to_element(driver.find_element_by_xpath(conversation_flow.save_conv_btn))
    action.click(on_element=driver.find_element_by_xpath(conversation_flow.save_conv_btn))
    action.perform()  

    success_msg = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, conversation_flow.save_success_alert)))
    if success_msg is not None :
         driver.save_screenshot('./screenshots/convSaved.png')
         return True
    else:
        raise AssertionError

def editPathName():
    try:
        pathsLoc = conversation_flow.path_inputs.replace('@@@','New path')
        paths = driver.find_elements_by_xpath(pathsLoc)
        if 'list' in str(type(paths)) :
            paths = paths[0]
        paths.click()
        paths.send_keys(Keys.CONTROL + 'a')
        paths.send_keys(Keys.BACKSPACE)
        paths.send_keys(data.Field_Name)

        action.move_to_element(driver.find_element_by_xpath(conversation_flow.save_conv_btn))
        action.click(driver.find_element_by_xpath(conversation_flow.save_conv_btn))
        if paths.get_attribute('value') in data.Field_Name:
            driver.save_screenshot('./screenshots/EditPathName.png')
            return True
        else:
            return False
    except Exception as e:
        print(e)
        closeBrowser()

def validateAddNewSteps():
    try:
        testVal = []
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'AddNewStepButton')))
        element.click()

        steptypes = driver.find_elements_by_xpath(conversation_flow.stepsTypes)
        for types in steptypes:
            testVal.append(types.text)
        if testVal == data.stepTypes:
            driver.save_screenshot('./screenshots/AddStepVals.png')
            return True
        else: 
            return False
    except Exception as e:
        print(e)
        closeBrowser()

def createCustomField():
    try:
        FieldName = driver.find_element_by_xpath(conversation_flow.field_dd)
        FieldName.click()
        action.send_keys(data.Field_Name)
        action.send_keys(Keys.RETURN)
        action.perform()
        driver.find_element_by_xpath(conversation_flow.customFieldSubmit).click()
        return True
    except Exception as e:
        print(e)
        
def verifyCustomField():
    try:
        FieldName = driver.find_element_by_xpath(conversation_flow.field_dd)
        FieldName.click()
        action.send_keys(Keys.ARROW_UP)
        action.send_keys(Keys.RETURN)
        action.perform()

        fieldHeadingLoc = conversation_flow.FieldInput.replace('@@@',data.Field_Name)
        fieldHeading = driver.find_element_by_xpath(fieldHeadingLoc)
        if fieldHeading is not None:
            driver.save_screenshot('./screenshots/CustomFields.png')
            return True
        else:
            return False
    except Exception as e:
        print(e)
        closeBrowser()

def verifyRoutingSteps(times):
    try:
        addStepLoc = conversation_flow.routingSteps.replace('@@@','Add routing step')
        routingStepsLoc = conversation_flow.routingSteps.replace('@@@','Alert')

        for i in range(0, times):
            action.move_to_element(driver.find_element_by_xpath(addStepLoc))
            driver.find_element_by_xpath(addStepLoc).click()

        routingElems = driver.find_elements_by_xpath(routingStepsLoc)
        if len(routingElems) == times+1:
            driver.save_screenshot('./screenshots/RoutingSteps.png')
            return True
        else:
            return False
    except Exception as e:
        print(e)

def closeBrowser():
    driver.close()

