import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

now = datetime.datetime.now()

content = ''

#extracting hacker news stories

def extract_news(url):
 print("Extracting Hacker news Stories...")
 cnt = ''
 cnt +=('<b>HN Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
 response = requests.get(url)
 content = response.content
 soup = BeautifulSoup(content, 'html.parser')
 for i, tag in enumerate(soup.find_all('td', attrs={'class':'title', 'valign': ''})):
  cnt += ((str(i+1) + '::' + tag.text + "\n"+ '<br>') if tag.text!='More' else '')
  #print(tag.prettify) #find all ('span', attrs = {'class': 'sitestr'}))
 return (cnt)

#concatenation is the following one:
cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>------<br>')
content += ('<br><br> End of Message')
#website structure of hacker news frontpage

#lets send the email
print('Composing Email...')

#call the function and put the custom function for email authentication
#update your email details
SERVER = 'smtp.gmail.com' # your smtp server
PORT = 587 #your port number
FROM  = '' ##your from email id
TO = ''  #your to email ids can be a list
PASS = '' #your email id's passwordo


#fp = open(file_name, 'rb')
#create a text/planin message
#msg = MIMEText ('')
msg = MIMEMultipart()
msg['Subject'] = 'Top News Stories HN [Automated Email]' + ' ' + str(now.day) + '-' + str(now.month) + '-'+ str(now.year)
msg['From'] = FROM
msg['To'] = TO
msg.attach(MIMEText(content, 'html'))
print('Initiating the server...')
server = smtplib.SMTP(SERVER, PORT)
#srver = smtplib.SMTP SSL ('smtp.gmail.com', 465)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.ehlo
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())
print('Email sent...')
server.quit()

