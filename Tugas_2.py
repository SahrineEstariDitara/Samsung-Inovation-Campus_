berat = int(input("Masukkan berat badan (kg): "))
tinggi = int(input("Masukkan tinggi badan (cm): "))

# Hitung BMI
if tinggi > 0:
    bmi = berat / ((tinggi / 100) ** 2)
    print(f"BMI Anda: {bmi:.2f}")

    if bmi < 18.5:
        kategori = "Underweight"
    elif 18.5 <= bmi < 25:
        if bmi >= 20 and bmi < 22.5:
            kategori = "Normal (mid-range)"
        else:
            kategori = "Normal"
    elif bmi >= 25 and bmi < 30:
        kategori = "Overweight"
    else:
        if bmi >= 35:
            kategori = "Obese (severe)"
        else:
            kategori = "Obese"
    print(f"Kategori BMI: {kategori}")
else:
    print("Tinggi badan harus lebih dari 0!")