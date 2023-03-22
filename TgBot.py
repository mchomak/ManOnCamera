# отправляет фотографии по телеграм боту пользователю
# send photos via telegram to bot to user

import telebot
import os
import time

def fileRecreate(file):
	file = file.replace('R', '')
	file = file.replace('.jpg', '')
	file = int(file)
	return file

def check_mans(score):
	token = '6181262632:AAF3sSFLw3oR95u7A_XHcVaGifZGEFR1sKA'
	users = [892023960, 1132147659, 1205339106]
	bot = telebot.TeleBot(token)
	print('Notifications bot has been started!')

	if score != None:
		if score >= 0.4:
			os.system('cmd /c "netsh" wlan connect name=Primakov_iMacs')
			time.sleep(2)
			files = os.listdir(f'results')

			for i in range(len(files)):
				files[i]=fileRecreate(files[i])

			img = open(f'results/R{max(files)}.jpg', 'rb')
			print(files)

			for i in users:
				try:
					bot.send_photo(i, img)
				except:
					files = os.listdir(f'results')
					for j in range(len(files)):
						files[j]=fileRecreate(files[j])

					files = sorted(files)
					img = open(f'results/R{max(files)}.jpg', 'rb')
					print(files)
					bot.send_photo(i, img)

				bot.send_message(i, f'<b>Найден человек!</b>\n<i>Вероятность {round(float(score)*100)}%</i>', parse_mode='html')

	os.system('cmd /c "netsh" wlan connect name=iCam-H9R_003604')
	time.sleep(2)

