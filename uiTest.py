from selenium import webdriver
from Locators import conversation_flow
from data import data

driver = webdriver.Chrome()
driver.get(data.URL)

emailID = driver.find_element_by_xpath(conversation_flow.email_insent)
emailID.send_keys(data.emailID_val)

password = driver.find_element_by_xpath(conversation_flow.password_insent)
password.send_keys(data.password_Val)

driver.find_element_by_xpath(conversation_flow.login_btn).click()

driver.close()