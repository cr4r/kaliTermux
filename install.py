import os
from shutil import copyfile
import shutil

#os.system('pkg update&&pkg install wget')

syStem = "https://images.kali.org/nethunter/kalifs-arm64-full.tar.xz"
sha1 = "https://images.kali.org/nethunter/kalifs-arm64-full.sha512sum"
namaSystem = 'kalifs-arm64-full.tar.xz'
namaSha1 = 'kalifs-arm64-full.sha512sum'

def pilih():
	os.system('clear')
	print('',' Silahkan pilih '.center(40,'='))
	try:
		plh = int(input('1. Download di termux\n2. Download di browser\n==> '))
		if plh == 1:
			jwb ='y'
			while jb == 'y' or jb =='ya' or jb=='Ya' or jb=='yes' or jb=='Ya' or p=='iya':
				os.system('rm '+namaSystem)
				os.system('wget '+syStem)
				jwb = input('Apakah anda mau mengulang download (y/t)')

			jwb ='y'
			while jb == 'y' or jb =='ya' or jb=='Ya' or jb=='yes' or jb=='Ya' or p=='iya':
				os.system('rm '+namaSha1)
				os.system('wget '+sha1)
				jwb = input('Apakah anda mau mengulang download (y/t)')
			try:
				shutil.move(namaSystem, '~/'+namaSystem)
				shutil.move(namaSha1, '~/'+namaSha1)
				shutil.move('kali', '~/kali')
				os.system('bash kali')
			except(NameError) as e:
				print(e)
				exit
			
		elif plh == 2:
			os.system('termux-open '+syStem)
			print('',' Mendownload system '.center(40,'='))
			p = input('Apakah file system sudah download(y/t): ')
			while p == 't' or p =='No' or p=='no' or p=='tidak' or p=='Tidak' or p=='':
				os.system('termux-open '+syStem)
				p = input('Apakah file system sudah download(y/t): ')
				
			p = os.system('termux-open '+sha1)
			print('\n',' Mendownload SHA1 '.center(40,'='))
			p = input('Apakah file SHA1 sudah download(y/t): ')
			while p == 't' or p =='No' or p=='no' or p=='tidak' or p=='Tidak' or p=='':
				os.system('termux-open '+sha1)
				p = input('Apakah file SHA1 sudah download(y/t): ')

			print('\n\n',' Peletakan file '.center(40,'='))
			x = input('1. File yang didownload tadi apakah mau meletakkan secara manual\n2. path\n(1/2) ==> ')
			if x =='1':
				print('Letakkan file di\n/data/data/com.termux/files/home/\nHARAP NAMA FILE JANGAN DI UBAH!!!')
			elif x == '2':
				jb = 'y'
				while jb == 'y' or jb =='ya' or jb=='Ya' or jb=='yes' or jb=='Ya' or p=='iya':
					try:
						d = input('Letak filemu ex:(/sdcard/Download)\n==> ')
						copyfile(d, '~/'+namaSystem)
						copyfile(d, '~/'+namaSha1)
						jb = ''
					except(NameError) as e:
						print(e)

			os.system('chmod +x kali&&cp kali ~')
			os.system('bash kali')
		else:
			print('Pilih 1/2')
			pilih()
	except(ValueError):
		print('Masukkan ANGKA bukan huruf')
		input()
		pilih()
	except(KeyboardInterrupt):
		print('tekan CTRL+Z untuk keluar')
		input()
		pilih()
pilih()
