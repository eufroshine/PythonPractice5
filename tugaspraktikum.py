from prettytable import PrettyTable

# Inisialisasi dictionary untuk menyimpan data mahasiswa
data_mahasiswa = {}

def tambah_data():
    nama = input("Masukkan nama mahasiswa: ")
    tugas = float(input("Masukkan nilai tugas (0-100): "))
    uts = float(input("Masukkan nilai UTS (0-100): "))
    uas = float(input("Masukkan nilai UAS (0-100): "))
    
    # Hitung nilai akhir
    nilai_akhir = 0.3 * tugas + 0.35 * uts + 0.35 * uas
    
    # Simpan data dalam dictionary
    data_mahasiswa[nama] = {
        'Tugas': tugas,
        'UTS': uts,
        'UAS': uas,
        'Nilai Akhir': nilai_akhir
    }
    print("Data mahasiswa berhasil ditambahkan!")

def ubah_data():
    nama = input("Masukkan nama mahasiswa yang ingin diubah datanya: ")
    
    # Periksa apakah nama mahasiswa ada dalam dictionary
    if nama in data_mahasiswa:
        tugas = float(input("Masukkan nilai tugas baru (0-100): "))
        uts = float(input("Masukkan nilai UTS baru (0-100): "))
        uas = float(input("Masukkan nilai UAS baru (0-100): "))
        
        # Hitung nilai akhir baru
        nilai_akhir = 0.3 * tugas + 0.35 * uts + 0.35 * uas
        
        # Perbarui data dalam dictionary
        data_mahasiswa[nama]['Tugas'] = tugas
        data_mahasiswa[nama]['UTS'] = uts
        data_mahasiswa[nama]['UAS'] = uas
        data_mahasiswa[nama]['Nilai Akhir'] = nilai_akhir
        
        print("Data mahasiswa berhasil diubah!")
    else:
        print("Nama mahasiswa tidak ditemukan.")

def hapus_data():
    nama = input("Masukkan nama mahasiswa yang ingin dihapus datanya: ")
    
    # Periksa apakah nama mahasiswa ada dalam dictionary
    if nama in data_mahasiswa:
        # Hapus data mahasiswa
        del data_mahasiswa[nama]
        print("Data mahasiswa berhasil dihapus!")
    else:
        print("Nama mahasiswa tidak ditemukan.")

def tampilkan_data():
    table = PrettyTable()
    table.field_names = ["Nama", "Tugas", "UTS", "UAS", "Nilai Akhir"]

    for nama, nilai in data_mahasiswa.items():
        table.add_row([nama, nilai['Tugas'], nilai['UTS'], nilai['UAS'], nilai['Nilai Akhir']])

    print(table)

def cari_data():
    nama = input("Masukkan nama mahasiswa yang ingin dicari datanya: ")
    
    # Periksa apakah nama mahasiswa ada dalam dictionary
    if nama in data_mahasiswa:
        nilai = data_mahasiswa[nama]
        print("\n=== Detail Nilai Mahasiswa ===")
        print(f"Nama: {nama}")
        print(f"Nilai Tugas: {nilai['Tugas']}")
        print(f"Nilai UTS: {nilai['UTS']}")
        print(f"Nilai UAS: {nilai['UAS']}")
        print(f"Nilai Akhir: {nilai['Nilai Akhir']}")
        print("============================")
    else:
        print("Nama mahasiswa tidak ditemukan.")

# Fungsi utama
while True:
    print("\n=== Menu Pilihan ===")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("0. Keluar")

    pilihan = input("Masukkan pilihan (0-5): ")

    if pilihan == '1':
        tambah_data()
    elif pilihan == '2':
        ubah_data()
    elif pilihan == '3':
        hapus_data()
    elif pilihan == '4':
        tampilkan_data()
    elif pilihan == '5':
        cari_data()
    elif pilihan == '0':
        print("Program selesai. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Masukkan pilihan antara 0 hingga 5.")
