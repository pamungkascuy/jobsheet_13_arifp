def tebak_angka():
    angka_rahasia = 9
    batas = 3
    penghitung = 0

    while penghitung < batas:
        user = int(input("Masukkan angka > "))
        if user == angka_rahasia:
            print("Selamat")
        break
    else:
        print("Salah")
        penghitung += 1
    if penghitung == batas:
        print("gagal")