# konversi suhu 

def celsius_to_fahrenheit (value):
    farhenheit = (value * 9/5) + 32
    return farhenheit

def celsius_to_kelvin (value):
    kelvin = (value + 273.15)
    return kelvin

def fahrenheit_to_celsius (value):
    celsius = (value - 32) * 5/9
    return celsius

def fahrenheit_to_kelvin (value):
    kelvin = (value - 32) * 5/9 + 273.15
    return kelvin

def kelvin_to_celsius (value):
    celsius = (value - 273.15)
    return celsius

def  kelvin_to_fahrenheit (value):
    fahrenheit = (value - 273.15) * 9/5 +32

# ==============================================

def konversi_suhu(value, nilai_awal, nilai_akhir):
    nilai_awal = nilai_awal.lower()
    nilai_akhir = nilai_akhir.lower()

    if nilai_awal not in ["c", "f", "k"] or nilai_akhir not in ["c", "f", "k"]:
        return "Error: Satuan tidak valid. Gunakan 'C', 'F', atau 'K'."

    if nilai_awal == "k" and value < 0:
        return "Error: Suhu Kelvin tidak boleh negatif."

    if nilai_awal == nilai_akhir:
        return value

    match (nilai_awal, nilai_akhir):
        case ("c", "f"):
            return celsius_to_fahrenheit(value)
        case ("c", "k"):
            return celsius_to_kelvin(value)
        case ("f", "c"):
            return fahrenheit_to_celsius(value)
        case ("f", "k"):
            return fahrenheit_to_kelvin(value)
        case ("k", "c"):
            return kelvin_to_celsius(value)
        case ("k", "f"):
            return kelvin_to_fahrenheit(value)

