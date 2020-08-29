from methodRepo import *

try:
    signin(data.emailID_val, data.password_Val,data.URL)
    createStep = create_convStep('Show a message')
    delay = addDelay()
    if createStep and delay:
        print("IA_15 Pass")
    else:
        print("IA_15 Fail")
    closeBrowser()
except Exception as e:
    print e