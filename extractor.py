import zipfile
import os

def extract_files(zipFiles):
	for file in zipFiles:
		zFile = zipfile.ZipFile(file)
		try:
			print('[+] Extracting: ' + file)
			zFile.extractall()
		except:
			pass

def Main():
	zipfiles = []
	for root, dirs, files in os.walk('.'):
		i = 0
		for file in files:
			if file.endswith('.zip'):
				i += 1
				print('[+] ' + str(i) + '. Zip File: ' + file)
				zipfiles.append(file)
	eInput = input('Would you like to extract all the zip files in this directory? (y/n)')
	if eInput == 'y':
		extract_files(zipfiles)
	else:
		print('[-] Closing Program.')
		exit(0)

if __name__ == '__main__':
	Main()
