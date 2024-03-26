import os
import time
import datetime
import requests
import win32gui
import win32con
import win32api
import threading
from win10toast import ToastNotifier

titleName = "notiSniper.py"
os.system(f"title {titleName}")
time.sleep(0.5)
foregroundwindow = win32gui.FindWindowEx(None, None, None, titleName)

notify = ToastNotifier()
year = datetime.date.today().year
delaySeconds = 5 # amount of time you wait in between each request


courses = []
courseNumber = str(input("Course Number (STOP when done): "))
while courseNumber.lower() != "stop":
	courses.append(courseNumber)
	courseNumber = str(input("Course Number (STOP when done): "))


def showNotification(course):
	notify.show_toast("NotiSniper", f"{course} is now open!", duration = 20, threaded = True)


def showHide():
	while True:
		if win32api.GetAsyncKeyState(0x11) < 0: # Ctrl Key
			if win32api.GetAsyncKeyState(0x45) < 0: # E Key
				win32gui.ShowWindow(foregroundwindow, win32con.SW_SHOW)
			if win32api.GetAsyncKeyState(0x4C) < 0: # L Key
				win32gui.ShowWindow(foregroundwindow, win32con.SW_HIDE)
		time.sleep(0.01)

showHideThread = threading.Thread(target=showHide).start()

win32gui.ShowWindow(foregroundwindow, win32con.SW_HIDE)

print("RUCourseSniping has been started!!")

while True:
	getResp = requests.get(f"https://classes.rutgers.edu/soc/api/openSections.json?year={year}&term=1&campus=NB").text
	for course in courses:
		if course in getResp:
			showNotification(course)
	else:
		time.sleep(delaySeconds)
