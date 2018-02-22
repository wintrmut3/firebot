#Firebot
import smtplib, random, time
print("I am firebot - I send spam emails!")

gmail_user = 'firebot625'
gmail_password = 'licentious'

ppl_list = ['jamesx03@gmail.com','349646414@gapps.yrdsb.ca']

sent_from = gmail_user
to = ppl_list
subject = 'Your Lucky Lottery Number'
body = random.randint(0,11000000)
numMail = 20
email_text = """
From: %s
To: %s
Subject: %s
%s
""" % (sent_from, ", ".join(to), subject, body)
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login(gmail_user,gmail_password)
    for i in range (numMail):
        #email code
        email_text = """
        From: %s
        To: %s
        Subject: %s
        %s
        """ % (sent_from, ", ".join(to), subject, random.randint(0,1100000))
        #end email code
        server.sendmail(sent_from,to,email_text)
        print ("EMAIL SENT! x "+str(i+1))
        time.sleep(0.1)
    server.close()
except:
    print ("Something went wrong! Oops ...")
