from django.db import models

# Create your models here.

class login:
    def __init__(self,id,pas):
        self.id="admin"
        self.pas="admin"

    def check(id,pas):
        print self.id
        print lod.id
        if(self.id==log.id and self.pas==log.pas):
            print "Login success!"


log=login("","")
log.check(raw_input("Enter Login ID:"),
        input("Enter password: "))

print "Login Page" 