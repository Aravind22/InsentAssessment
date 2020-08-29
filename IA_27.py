from methodRepo import *

try:
    signin(data.emailID_val, data.password_Val,data.URL)
    verifyStep = validateAddNewSteps()
    if verifyStep:
        print("IA_27 Pass")
        closeBrowser()
    else:
        print("IA_27 Fail")
except Exception as e:
    print e