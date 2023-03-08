jumlahSol = 0
jumlahSur = 0
jumlahJog = 0
jumlahMag = 0

def hitung_mobil():
    while True:
        asal = str(input("masukkan asal mobil (ketik done untuk keluar): ")).lower()
        if asal == "done":
            break
        elif asal == "Solo":
            jumlahSol = jumlahSol + 1
        elif asal == "Surabaya":
            jumlahSur = jumlahSur + 1
        elif asal == "Jogja":
            jumlahJog = jumlahJog + 1
        elif asal == "Magelang":
            jumlahMag = jumlahMag + 1

print("Jumlah Mobil Solo    :", hitung_mobil())
print("Jumlah Mobil Surabaya    :", hitung_mobil())
print("Jumlah Mobil Jogja   : ", hitung_mobil())
print("Jumlah Mobil Magelang    :", hitung_mobil())