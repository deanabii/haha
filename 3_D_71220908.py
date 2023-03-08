import math

while True:
    awal = input("Masukkan jarak awal (dalam meter): ").lower()
    if awal == "Berhenti" or awal == "Stop":
        print("Program dihentikan")
        break
    awal = float(awal)
    ke5 = float(input("Masukkan sudut elevasi pada menit ke-5 (dalam derajat): "))
    ke6 = float(input("Masukkan sudut elevasi pada menit ke-6 (dalam derajat): "))

    tinggi_awal = awal * math.tan(ke5)
    jarak_akhir = awal * math.tan(ke6) - math.tan(ke5)
    selisih = jarak_akhir * math.tan((ke6))

    print("Ketinggian drone pada menit ke-5 adalah", tinggi_awal)
    print("Selisih ketinggian drone saat menit ke-5 dan ke-6 adalah", selisih)
