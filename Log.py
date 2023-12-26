import FBTools
from FBTools.Login import Login

email = 'Input Email Here'
password = 'Input Password Here'
L = Login()
L.LoginEmail(email=email,password=password,cookie=True)
