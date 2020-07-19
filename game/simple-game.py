import random

lst = ["Kertas", "Gunting", "Batu"]
def pilihanlawan():
    global lst
    return random.choice(lst)

def cek(pilihan):
    global lst
    lawan = pilihanlawan()
    rand = random.randint(0, 2)
    print ("Kamu: " + lst[pilihan])
    if rand < pilihan:
        print ("Lawan: " + lst[rand])
        print ("Hasil: Menang")
    elif rand == pilihan:
        print ("Lawan: " + lst[rand])
        print ("Hasil: Draw")
    elif rand > pilihan:
        print ("Lawan: " + lst[rand])
        print ("Hasil: Kalah")

def main():
    global lst
    print ("[ Simle Game By Gudang Tools ]")
    print ("1. Kertas")
    print ("2. Gunting")
    print ("3. Batu")

    pilih = input("  Masukan pilihan anda ~> ")
    # Cek jika yang diinput merupakan angka
    if pilih.isdigit():
        pilihanKamu = int(pilih) - 1
        cek(pilihanKamu)
    else:
        print ("Masukan angka!")

if __name__ == "__main__":
    main()