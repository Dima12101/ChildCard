import os
import sys
import ftplib

BASE_DIR_CLIENT = os.path.dirname(os.path.abspath(__file__))

ftp = ftplib.FTP()


def download_file(name_file_server, path_file_client):
	with open(path_file_client, 'wb') as file_client:
		ftp.retrbinary('RETR ' + name_file_server, file_client.write)

def main():

	print('Connect to FTP-server ...')
	print('>', ftp.connect('46.149.233.52', 30))

	print('')

	print('Login in FTP-server ...')
	ftp.login(os.environ['FTP_USER'], os.environ['FTP_PASSWORD'])

	ftp.cwd('ChildCard_images')

	print(ftp.retrlines('LIST'))

	download_file('cock_morning.jpg', './cock_morning.jpg')

	print(os.listdir('./'))


if __name__ == "__main__":
	main()