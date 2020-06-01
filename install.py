import os

#os.system('pkg update&&pkg install wget')
def menu():
	os.system('clear')
	print(' Silahkan pilih '.center(40,'='))
	print('1. Download di termux\n2. Download di browser')
	pilih()

def pilih():
	try:
		plh = int(input('==> '))
		if plh == 1:
			os.system('wget https://images.kali.org/nethunter/kalifs-arm64-full.tar.xz ')
			os.system('wget https://images.kali.org/nethunter/kalifs-arm64-full.sha512sum')
		elif plh == 2:
			os.system('termux-open https://images.kali.org/nethunter/kalifs-arm64-full.tar.xz')
			p = input('Apakah sudah download ?')
			os.system('termux-open https://images.kali.org/nethunter/kalifs-arm64-full.sha512sum')
			os.system('chmod +x install.py')
		else:
			print('Pilih 1/2')
			input()
#			menu()
	except(ValueError):
		print('Masukkan ANGKA bukan huruf')
		input()
		menu()
	except(KeyboardInterrupt):
		print('tekan CTRL+Z untuk keluar')
		input()
		menu()
menu()
