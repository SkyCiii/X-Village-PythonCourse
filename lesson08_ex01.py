
import re

class Auth :
    def __init__(self) :
        self.p_username = r'([A-Z][a-z][a-z])'
        self.p_password = r'([a-z][a-z][a-z][0][0-9][0-9][0-9][0-9][0-9])'
        self.username_regex = re.compile(self.p_username)
        self.password_regex = re.compile(self.p_password)
    
    def _username_check (self, username) :
        if self.username_regex.search(username) is not None :
            print ('Correct username')
            return True
        else :
            print ('Username format error, your username is', username)
            return False

    def _password_check (self, password) :
        print(len(password), len(self.p_password))
        if self.password_regex.search(password) is not None and len(password) == len(self.p_password)/5 :
            print ('Correct password')
            return True
        elif self.password_regex.search(password) is None and len(password) == len(self.p_password)/5 :
            print ('Password format error, your password is', password)
            return False
        elif self.password_regex.search(password) is not None or len(password) != len(self.p_password)/5 :
            print ('Password length error, your passowrd is', password)
            return False
            
    def authenticate (self, username, password) :
        if not self._username_check(username) :
            return
        if not self._password_check(password) :
            return
        print ('Welcome', username)


username = input ('username : ')
password = input ('password : ')
auth = Auth()
auth.authenticate(username, password)