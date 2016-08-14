import smtplib
import sys

ip = sys.argv[1]
name = sys.argv[2]

gmail_user = ############  
gmail_password = #########


#to = ['5154180061@vtext.com'] 
to = ['6414171599@email.uscc.net'] 


email_text = "device " + name + " has problems at IP " + ip

try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, to, email_text)
    server.close()

    print 'SMS Sent'
except:  
    print 'Error'
