# Membuat list kosong untuk menyimpan input pengguna
user_data = []

# Meminta input dari pengguna
n = int(input("Jumlah data yang akan dimasukkan: "))

for i in range(n):
    data = input(f"Masukkan data ke-{i + 1}: ")
    user_data.append(data)

# Menggunakan map() dan filter() untuk memisahkan tipe data
int_values = list(map(int, filter(lambda x: x.isdigit() and not '.' in x, user_data)))

# Mencetak hasilnya dengan keterangan ratusan, puluhan, dan satuan
for value in int_values:
    ratusan = value // 100
    puluhan = (value % 100) // 10
    satuan = value % 10

    keterangan = f"{ratusan} ratusan, {puluhan} puluhan, {satuan} satuan"
    
    print(f"Data int: {value} ({keterangan})")

float_values = list(map(float, filter(lambda x: '.' in x, user_data)))
string_values = list(filter(lambda x: not x.isdigit() and '.' not in x, user_data))

# Mencetak hasil data float dan string
print("Data float:", float_values)
print("Data string:", string_values)
