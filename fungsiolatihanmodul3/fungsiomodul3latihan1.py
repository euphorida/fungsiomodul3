def convert_to_minutes(weeks):
    def inner1(days):
        def inner2(hours):
            def inner3(minutes):
                return weeks * 7 * 24 * 60 + days * 24 * 60 + hours * 60 + minutes
            return inner3
        return inner2
    return inner1

# Menggunakan currying
convert = convert_to_minutes

# Meminta input dari pengguna
weeks = int(input("Masukkan jumlah minggu: "))
days = int(input("Masukkan jumlah hari: "))
hours = int(input("Masukkan jumlah jam: "))
minutes = int(input("Masukkan jumlah menit: "))

# Menggunakan input pengguna untuk mengkonversi ke menit
total_minutes = convert(weeks)(days)(hours)(minutes)
print("Total menit:", total_minutes)
