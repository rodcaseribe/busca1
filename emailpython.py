#!/usr/bin/python
import smtplib
import os
	 
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
