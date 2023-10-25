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
user_input = input("Masukkan jumlah minggu, hari, jam, dan menit (pisahkan dengan spasi): ")

# Membagi input pengguna menjadi daftar string
input_values = user_input.split()

# Menggunakan filter untuk mengambil hanya nilai integer
input_values = list(filter(lambda x: x.isdigit(), input_values))

# Konversi nilai ke integer
input_values = [int(value) for value in input_values]

if len(input_values) == 4:
    weeks, days, hours, minutes = input_values

    # Menggunakan input pengguna untuk mengkonversi ke menit
    total_minutes = convert(weeks)(days)(hours)(minutes)
    print("Hasil:", str(total_minutes))
else:
    print("Input harus terdiri dari tepat 4 nilai integer (minggu, hari, jam, menit).")
