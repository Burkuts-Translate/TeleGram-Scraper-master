#!/bin/env python3
# code by : youtube.com/theunknon

"""

you can re run setup.py 
if you have added some wrong value

"""
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

import os, sys
import time

def banner():
	os.system('clear')
	print(f"""
	{re}╔═╗{cy}┌─┐┌┬┐┬ ┬┌─┐
	{re}╚═╗{cy}├┤  │ │ │├─┘
	{re}╚═╝{cy}└─┘ ┴ └─┘┴
	""")

def requirements():
	def csv_lib():
		banner()
		print(gr+'['+cy+'+'+gr+']'+cy+' Bu Biraz Zaman Alabilir...')
		os.system("""
			pip3 install cython numpy pandas
			python3 -m pip install cython numpy pandas
			""")
	banner()
	print(gr+'['+cy+'+'+gr+']'+cy+' csv birleştirmeyi yüklemek 10 dakika kadar sürer.')
	input_csv = input(gr+'['+cy+'+'+gr+']'+cy+' csv birleştirmeyi etkinleştirmek istiyor musun (y/n): ').lower()
	if input_csv == "y":
		csv_lib()
	else:
		pass
	print(gr+"[+] Requierments/Gereksinimler Yükleniyor ...")
	os.system("""
		pip3 install telethon requests configparser
		python3 -m pip install telethon requests configparser
		touch config.data
		""")
	banner()
	print(gr+"[+] Requierments/Gereksinimler Yüklendi.\n")


def config_setup():
	import configparser
	banner()
	cpass = configparser.RawConfigParser()
	cpass.add_section('cred')
	xid = input(gr+"[+] enter api ID : "+re)
	cpass.set('cred', 'id', xid)
	xhash = input(gr+"[+] enter hash ID : "+re)
	cpass.set('cred', 'hash', xhash)
	xphone = input(gr+"[+] enter phone number : "+re)
	cpass.set('cred', 'phone', xphone)
	setup = open('config.data', 'w')
	cpass.write(setup)
	setup.close()
	print(gr+"[+] Kurulum Tamamlan'dı !")

def merge_csv():
	import pandas as pd
	import sys
	banner()
	file1 = pd.read_csv(sys.argv[2])
	file2 = pd.read_csv(sys.argv[3])
	print(gr+'['+cy+'+'+gr+']'+cy+' Birleştirme '+sys.argv[2]+' & '+sys.argv[3]+' ...')
	print(gr+'['+cy+'+'+gr+']'+cy+' Büyük dosyalar biraz zaman alabilir ... ')
	merge = file1.merge(file2, on='username')
	merge.to_csv("output.csv", index=False)
	print(gr+'['+cy+'+'+gr+']'+cy+' Dosya "output.csv" Olarak Kayıt Edildi\n')

def update_tool():
	import requests as r
	banner()
	source = r.get("https://raw.githubusercontent.com/th3unkn0n/TeleGram-Scraper/master/.image/.version")
	if source.text == '3':
		print(gr+'['+cy+'+'+gr+']'+cy+' Zaten Son Sürüm')
	else:
		print(gr+'['+cy+'+'+gr+']'+cy+' Eski Dosya Siliniyor ...')
		os.system('rm *.py');time.sleep(3)
		print(gr+'['+cy+'+'+gr+']'+cy+' En Son Dosyalar Alınıyor ...')
		os.system("""
			curl -s -O https://raw.githubusercontent.com/th3unkn0n/TeleGram-Scraper/master/add2group.py
			curl -s -O https://raw.githubusercontent.com/th3unkn0n/TeleGram-Scraper/master/scraper.py
			curl -s -O https://raw.githubusercontent.com/th3unkn0n/TeleGram-Scraper/master/setup.py
			curl -s -O https://raw.githubusercontent.com/th3unkn0n/TeleGram-Scraper/master/smsbot.py
			chmod 777 *.py
			""");time.sleep(3)
		print(gr+'\n['+cy+'+'+gr+']'+cy+' Güncelleme Tamamlandı.\n')

try:
	if any ([sys.argv[1] == '--config', sys.argv[1] == '-c']):
		print(gr+'['+cy+'+'+gr+']'+cy+' Modül Seçiniz : '+re+sys.argv[1])
		config_setup()
	elif any ([sys.argv[1] == '--merge', sys.argv[1] == '-m']):
		print(gr+'['+cy+'+'+gr+']'+cy+' Modül Seçiniz : '+re+sys.argv[1])
		merge_csv()
	elif any ([sys.argv[1] == '--update', sys.argv[1] == '-u']):
		print(gr+'['+cy+'+'+gr+']'+cy+' Modül Seçiniz : '+re+sys.argv[1])
		update_tool()
	elif any ([sys.argv[1] == '--install', sys.argv[1] == '-i']):
		requirements()
	elif any ([sys.argv[1] == '--help', sys.argv[1] == '-h']):
		banner()
		print("""$ python3 setup.py -m file1.csv file2.csv
			
	( --config  / -c ) kurulum api yapılandırması
	( --merge   / -m ) 2 .csv dosyasını bir arada birleştir
	( --update  / -u ) aracı en son sürüme güncelle
	( --install / -i ) yükleme gereksinimleri
	( --help    / -h ) bu mesajı göster
			""")
	else:
		print('\n'+gr+'['+re+'!'+gr+']'+cy+' Bilinmeyen Argüman : '+ sys.argv[1])
		print(gr+'['+re+'!'+gr+']'+cy+' for help use : ')
		print(gr+'$ python3 setup.py -h'+'\n')
except IndexError:
	print('\n'+gr+'['+re+'!'+gr+']'+cy+' Argüman Yok : '+ sys.argv[1])
	print(gr+'['+re+'!'+gr+']'+cy+' Yardım Kullanımı İçin : ')
	print(gr+'['+re+'!'+gr+']'+cy+' https://github.com/th3unkn0n/TeleGram-Scraper#-how-to-install-and-use')
	print(gr+'$ python3 setup.py -h'+'\n')
