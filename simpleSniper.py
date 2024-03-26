import requests
import time
import datetime

year = datetime.date.today().year
delaySeconds = 5 # amount of time you wait in between each request
courseNumber = str(input("Course Number: "))

while True:
	getResp = requests.get(f"https://classes.rutgers.edu/soc/api/openSections.json?year={year}&term=1&campus=NB").text
	if courseNumber in getResp:
		print(f"[!] Section {courseNumber} is open!")
		break
	else:
		time.sleep(delaySeconds)