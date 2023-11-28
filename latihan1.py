from prettytable import PrettyTable

def tambah_kontak():
    nama_baru = input("Masukkan nama kontak baru: ")
    nomor_baru = input(f"Masukkan nomor telepon untuk {nama_baru}: ")
    daftar_kontak[nama_baru] = nomor_baru
    print(f"Kontak {nama_baru} berhasil ditambahkan.")

def ubah_kontak(nama):
    if nama in daftar_kontak:
        nomor_baru = input(f"Masukkan nomor telepon baru untuk {nama}: ")
        daftar_kontak[nama] = nomor_baru
        print(f"Nomor telepon {nama} berhasil diubah.")
    else:
        print("Kontak tidak ditemukan.")

def cari_kontak(nama):
    nomor = daftar_kontak.get(nama, "Kontak tidak ditemukan")
    print(f"Nomor telepon {nama}: {nomor}")

def hapus_kontak(nama):
    if nama in daftar_kontak:
        del daftar_kontak[nama]
        print(f"Kontak {nama} berhasil dihapus.")
    else:
        print("Kontak tidak ditemukan.")

def tampilkan_semua_kontak():
    table = PrettyTable()
    table.field_names = ["Nama", "Nomor Telepon"]

    for nama, nomor in daftar_kontak.items():
        table.add_row([nama, nomor])

    print(table)

# Inisialisasi Dictionary daftar kontak
daftar_kontak = {}

while True:
    print("\n=== Menu Kontak ===")
    print("1. Tambah kontak")
    print("2. Ubah kontak")
    print("3. Cari kontak")
    print("4. Hapus kontak")
    print("5. Tampilkan semua Nama dan Nomor")
    print("0. Keluar")

    pilihan = input("Masukkan pilihan (0-5): ")

    if pilihan == '1':
        tambah_kontak()
    elif pilihan == '2':
        nama = input("Masukkan nama kontak yang ingin diubah: ")
        ubah_kontak(nama)
    elif pilihan == '3':
        nama = input("Masukkan nama kontak yang ingin dicari: ")
        cari_kontak(nama)
    elif pilihan == '4':
        nama = input("Masukkan nama kontak yang ingin dihapus: ")
        hapus_kontak(nama)
    elif pilihan == '5':
        tampilkan_semua_kontak()
    elif pilihan == '0':
        print("Program selesai. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Masukkan pilihan antara 0 hingga 5.")
