# client while checking out, enters his email id
# and then recieve a mail containing details of his visit

import time
from time import gmtime, strftime
import smtplib
from checkin import SiteManager

def client_details():
	print("Please enter client email Id: ",end="")
	client_email = input()
	CheckOut_time = ""
	message = ""
	host_name = ""
	file = open(r"Client_Info", "r")
	for entry in file.readlines():
		entry = entry.split()
		if entry[1] == client_email:
			CheckOut_time = strftime("%Y-%m-%d/%H:%M:%S", time.localtime())
			host_name = entry[4]
			message = "\nName: " + entry[0] + "\n" + "Phone: " + entry[2] + "\n" + "Check-in Time: " + entry[3] + "\n" + "Check-out Time: " + CheckOut_time + "\n"
			break
	email_to_client(message, client_email,host_name)

def email_to_client(bodytext, client_email, host_name):

	site_manager_obj = SiteManager()	
	
	address,account_sid,auth_token,twilio_contact,login_id,login_password = site_manager_obj.manager_info()
	
	bodytext += "Host Name: " + host_name + "\n" + "Address Visited: " + address
	
	subject = "Your visit to " + address + "."
	message = 'Subject: {}\n\n{}'.format(subject, bodytext)
	try:
		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.starttls()
		s.login(login_id, login_password)
	except:
		print("Unable to LogIn")
	try:
		s.sendmail(login_id, client_email, message)
		print("Client Check-out Successful")
	except:
		print("Unable to check-out")
	s.quit()

if __name__ == "__main__":
	client_details()
