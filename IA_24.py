from methodRepo import *

try:
    signin(data.emailID_val, data.password_Val,data.URL)
    createStep = create_convStep('Capture user data')
    createCustom = createCustomField()
    time.sleep(2)
    delStep = del_step('Capture user data')
    createStep = create_convStep('Capture user data')
    verifyRoute = verifyCustomField()
    if createStep and verifyRoute and createCustom and del_step:
        print("IA_24 Pass")
        closeBrowser()
    else:
        print("IA_24 Fail")
except Exception as e:
    print e