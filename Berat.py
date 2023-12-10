def konversi_berat():
    berat = int(input("Masukkan berat badan: "))
    tipe = input("(kg/lbs): ")

    if tipe.upper() == "K":
        print("berat", round(berat/0.45), "lbs")
    elif tipe.upper() == "L":
        print("berat", round(berat*0.45), "kg")
    else:
        print("Salah, masukkan (k/l).")