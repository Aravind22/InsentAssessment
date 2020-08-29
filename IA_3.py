from methodRepo import *
#Add new Step - show a message
try:
    signin(data.emailID_val, data.password_Val,data.URL)
    createStep = create_convStep('Show a message')
    showMsg = showMessage()
    if createStep and showMsg:
        print("IA3 Pass")
    else:
        print("IA3 Fail")
    closeBrowser()
except Exception as e:
    print(e)

