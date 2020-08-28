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
add_condition_step = "//div[contains(text(),'Add condition')]"
rem_condition_step = "//div[contains(text(),'Remove condition')]"
preview_btn = "//div[contains(text(),'Preview')]"

empty_input_field = "//div[@class='text-danger mt-1' and contains(.,'Please enter a message')]"

save_conv_btn = "//span[contains(text(), 'Save conversation flow')]"

save_success_alert = "//div[contains(text(),'Conversation saved successfully') and @role='alert']"

add_redirect_btn = "//button/span/span[contains(text(),'Add redirect')]"

#Capture user data
field_dd = "//div[contains(text(),'Select or type to create a new field')]/.."
field_heading = "//div[contains(text(), '@@@')]"
plainText_ip = "//div[contains(text(), 'User sends an input')]"
redirectPathField = "//div[contains(text(),'Select a path')]/.."

#conditions
conHeading = "//button/span/span[contains(text(),'Show conditions')]"

#paths
path_inputs = "//input[@value='@@@']"
remove_path_icon = "(//input[@value='MyPath']/../../../../span/div/*[name()='svg'])"
empty_pathField = "//div[contains(text(), 'This field cannot be empty')]"