from methodRepo import *

try:
    signin(data.emailID_val, data.password_Val,data.URL)
    verifyPathName = editPathName()
    if verifyPathName:
        print("IA_28 Pass")
        closeBrowser()
    else:
        print("IA_28 Fail")
except Exception as e:
    print e