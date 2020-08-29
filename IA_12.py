from methodRepo import *
#Delete a step
try:
    signin(data.emailID_val, data.password_Val,data.URL)
    createStep = create_convStep('Show a message')
    deleteStep = del_step('Show a message')
    if createStep and deleteStep:
        print("IA12 Pass")
    else:
        print("IA12 Fail")
    closeBrowser()
except Exception as e:
    print(e)