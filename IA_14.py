from methodRepo import *

#Validate 'end this path with' field if an associated path is deleted
try:
    signin(data.emailID_val, data.password_Val,data.URL)
    addpath = add_path()
    redirectAdd = add_Redirect('Go to path')
    rempath = rem_path()
    verify = verify_delPath()
    if addpath and rempath and verify and redirectAdd:
        print("IA14 Pass")
    else:
        print("IA14 Fail")
except Exception as e:
        print(e)