import os
import sys
import ftplib

BASE_DIR_CLIENT = f'{os.path.dirname(os.path.abspath(__file__))}/static/main/image/child_photo'

ftp = ftplib.FTP()


def download_file(name_file_server, path_file_client):
	with open(path_file_client, 'wb') as file_client:
		ftp.retrbinary('RETR ' + name_file_server, file_client.write)


ftp_log = open('ftp_log.txt', 'w')

print('Load images from FTP-server')
ftp_log.write('Load images from FTP-server\n')

response = ftp.connect('46.149.233.52', 30)
print('>', response)
ftp_log.write('> ' + response + '\n')

print('> Login in FTP-server ...')
ftp_log.write('> Login in FTP-server ...\n')

ftp.login(os.environ['FTP_USER'], os.environ['FTP_PASSWORD'])

ftp.cwd('ChildCard_images')
print('> Loading...')
ftp_log.write('> Loading...\n')
for user_name in ftp.nlst():
	if not os.path.exists(f'{BASE_DIR_CLIENT}/{user_name}'):
		os.makedirs(f'{BASE_DIR_CLIENT}/{user_name}')
	ftp.cwd(user_name)
	for image_name in ftp.nlst():
		download_file(image_name, f'{BASE_DIR_CLIENT}/{user_name}/{image_name}')
	ftp.cwd('..')
print('> Success!')
ftp_log.write('> Success!\n')

ftp_log.close()

ftp.close()

open('is_load.', 'w').close()