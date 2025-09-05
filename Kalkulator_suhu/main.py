from utils import konversi_suhu


print("=== KONVERSI SUHU ===")


try :
    value       =  int (input("Masukkan nilai suhu: "))
    nilai_awal  = input("Dari satuan (C/F/K): ")
    nilai_akhir = input("ke satuan (C/F/K): ")

    hasil = konversi_suhu(value, nilai_awal, nilai_akhir)

    print(f"Hasil: {value}°{nilai_awal.upper()} = {hasil:.1f}°{nilai_akhir.upper()}")

except ValueError:
    print("=====================================")
    print("Error: value suhu harus berupa angka.")
    print("=====================================")
    
