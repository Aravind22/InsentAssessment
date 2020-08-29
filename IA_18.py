from methodRepo import *

try:
    signin(data.emailID_val, data.password_Val,data.URL)
    createStep = create_convStep('Show a message')
    createMsg = showMessage()
    verifypreview = verify_Preview('Show a message')
    if createStep and verifypreview:
        print("IA_18 Pass")
    else:
        print("IA_18 Fail")
    closeBrowser()
except Exception as e:
    print e