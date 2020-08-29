from methodRepo import *

try:
    signin(data.emailID_val, data.password_Val,data.URL)
    createStep = create_convStep('Connect to an agent')
    verifyRoute = verifyRoutingSteps(3)
    if createStep and verifyRoute:
        print("IA_22 Pass")
    else:
        print("IA_22 Fail")
    closeBrowser()
except Exception as e:
    print e