email_insent = "//input[@name='email']"
password_insent = "//input[@name='password']"
login_btn = "//button/span/span[contains(.,'Login')]"
conversation_name = "//span/div[contains(.,'@@@')]/../../../../../../div[contains(.,'###')][1]"
conversation_flow = "//div[contains(text(),'Conversation flow')]"
addnewStep_btn = "//button[@id='AddNewStepButton']"
convStep_type = "//div[@id='PopupContainer']/div/div[contains(text(),'@@@')]"

showMessage_input = "(//div[contains(text(),'This is a sample text')]/..)"
showMessage_input_opened = "//div/p[contains(text(),'This is a sample text')]"
showMessage_input_opened_closed = "//span[contains(text(), 'What do you want to say?')]/../.."
preview_sampleText = "(//div[contains(text(),'This is a sample text')])[2]"

del_step_ellipses = "//div[contains(text(),'@@@')]/../div/div/div/div/div/button"
del_step = "//div[contains(text(),'Delete step')]"

preview_btn = "//div[contains(text(),'Preview')]"

empty_input_field = "//div[@class='text-danger mt-1' and contains(.,'Please enter a message')]"

save_conv_btn = "//span[contains(text(), 'Save conversation flow')]"

save_success_alert = "//div[contains(text(),'Conversation saved successfully') and @role='alert']"