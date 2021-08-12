class logindata(object):

    
    
        
    def getLoginData(self,testCase):
        invalidEmail = "something@gmail.com"
        invalidPassword = "123123123123131323"
        validEmail = 'siam.qups@gmail.com'
        validPassword='Siamsami1'
        if(testCase==1):
            email=validEmail
            password=validPassword
        elif (testCase==2):
            email=validEmail
            password=invalidPassword
        elif (testCase==3):
            email=invalidEmail
            password=validPassword
        else:
            email=invalidEmail
            password=invalidPassword
        return email,password
        