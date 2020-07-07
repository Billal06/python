import sqlite3
import sys

db = "./belajar_crud.db"

def koneksi():
	"Berfungsi untuk menghubungkan ke database"
	try:
		konek = sqlite3.connect(db)
		print ("[!] Anda sudah terhubung ke database")
		return konek
	except Exception as e:
		print ("[!] Tidak terkoneksi ke database, silahkan buat file bernama 'belajar_crud.db' di folder ini")
		sys.exit()

def buat_table(koneksi_db, nama_table):
	"Berfungsi untuk membuat table"
	perintah = f"""CREATE TABLE IF NOT EXISTS {nama_table} (
		id integer PRIMARY KEY,
		nama_barang text,
		harga integer
	);"""

	cursor = koneksi_db.cursor()
	cursor.execute(perintah)
	print (f"[!] Table berhasil di buat dengan nama '{nama_table}'")

def isi_data(koneksi_db, nama_table, nama_barang, harga):
	perintah = f"""INSERT INTO {nama_table} VALUES (NULL, '{nama_barang}', {harga});"""
	cursor = koneksi_db.cursor()
	cursor.execute(perintah)
	print (f"[!] Barang '{nama_barang}' telah ditambahkan")

def  lihat_data(koneksi_db, nama_table):
	perintah = f"""
	SELECT * FROM {nama_table}
	"""
	cursor = koneksi_db.cursor()
	cursor.execute(perintah)
	for data in cursor:
		print (f"[{data[0]}] Barang: {data[1]}, harga: {data[2]}")

def cari_data(koneksi_db, nama_table, cari):
	ketemu = False
	perintah = f"SELECT * FROM {nama_table}"
	cursor = koneksi_db.cursor()
	cursor.execute(perintah)
	for a in cursor:
		if cari in a[1]:
			ketemu = True
			print (f"[{a[0]}] Barang: {a[1]}, harga: {a[2]}")

	if ketemu != True:
		print ("[!] Barang yang anda cari tidak ditemukan")

if __name__ == '__main__':
	konek = None
	nama_table = ""
	while True:
		print ("[1]. Konek ke database")
		print ("[2]. Buat table")
		print ("[3]. Tambah data")
		print ("[4]. Lihat data")
		print ("[5]. Cari data")
		pilih = input("  Masukan pilihan anda ~> ")
		if pilih == "1" or pilih == "01":
			konek = koneksi()

		if konek != None:
			if pilih == "02" or pilih == "2":
				nama_table = input("[?] Masukan nama table: ")
				if " " in nama_table:
					print ("[!] Nama tidak boleh ada spasi")
				else:
					buat_table(konek, nama_table)
			elif pilih == "03" or pilih == "3":
				if nama_table != "":
					print ("[!] CTRL + C untuk berhenti")
					while  True:
						try:
							barang = input("[?] Masukan nama barang (contoh: mainan): ")
							harga = input("[?] Masukan harga barang (contoh: 25000: ")
							isi_data(konek, nama_table, barang, harga)
						except KeyboardInterrupt:
							print ()
							break
				else:
					print ("[!] Silahkan buat table terlebih dahulu")
			elif pilih == "04" or pilih == "4":
				if nama_table != "":
					lihat_data(konek, nama_table)
				else:
					print ("[!] Silahkan buat table terlebih dahulu")
			elif pilih == "05" or pilih == "5":
				if nama_table != "":
					cari = input("[?] Mau cari barang apa? ")
					cari_data(konek, nama_table, cari)
				else:
					print ("[!] Silahkan buat table terlebih dahulu")
		else:		
			print ("[#] Belum terhubung ke database, silahhkan hubungkan ke database")

		print ("-" * 30)