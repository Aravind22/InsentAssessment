from methodRepo import *

try:
    signin(data.emailID_val, data.password_Val,data.URL)
    createStep = create_convStep('Show a message')
    createCond = add_conditions('Show a message')
    verifyRem = remCondition('Show a message')
    if createStep and createCond and verifyRem:
        print("IA_26 Pass")
        closeBrowser()
    else:
        print("IA_26 Fail")
except Exception as e:
    print e