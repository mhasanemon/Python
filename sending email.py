import smtplib

connection = smtplib.SMTP('smtp.gmail.com',587)
connection.starttls()
connection.login('emon3500@gmail.com','01925789785')

connection.sendmail('emon3500@gmail.com','emon3500@yahoo.com','Subject:MC')