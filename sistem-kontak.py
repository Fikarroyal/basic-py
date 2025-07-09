def tampilkan_menu():
    """Menampilkan menu utama."""
    print("\n" + "=" * 30)
    print("  Sistem Manajemen Kontak  ")
    print("=" * 30)
    print("1. Tambah Kontak")
    print("2. Lihat Semua Kontak")
    print("3. Cari Kontak")
    print("4. Hapus Kontak")
    print("5. Keluar")
    print("-" * 30)

def tambah_kontak(daftar_kontak):
    """Menambahkan kontak baru ke daftar."""
    print("\n----- Tambah Kontak Baru -----")
    nama = input("Nama: ").strip().title()
    if not nama:
        print("Nama tidak boleh kosong.")
        return

    telepon = input("Telepon: ").strip()
    email = input("Email (opsional): ").strip()

    # Cek apakah nama sudah ada
    for kontak in daftar_kontak:
        if kontak['nama'].lower() == nama.lower():
            print(f"Kontak dengan nama '{nama}' sudah ada.")
            return

    kontak_baru = {
        'nama': nama,
        'telepon': telepon,
        'email': email if email else 'Tidak Ada' # Jika email kosong, isi 'Tidak Ada'
    }
    daftar_kontak.append(kontak_baru)
    print(f"Kontak '{nama}' berhasil ditambahkan!")

def lihat_semua_kontak(daftar_kontak):
    """Menampilkan semua kontak dalam daftar."""
    print("\n------- Daftar Kontak -------")
    if not daftar_kontak:
        print("Daftar kontak masih kosong.")
        return

    for i, kontak in enumerate(daftar_kontak, 1):
        print(f"{i}. Nama: {kontak['nama']}")
        print(f"   Telepon: {kontak['telepon']}")
        print(f"   Email: {kontak['email']}")
        print("-" * 30)

def cari_kontak(daftar_kontak):
    """Mencari kontak berdasarkan nama."""
    print("\n-------- Cari Kontak --------")
    kata_kunci = input("Masukkan nama yang ingin dicari: ").strip().lower()
    ditemukan = False
    for kontak in daftar_kontak:
        if kata_kunci in kontak['nama'].lower():
            print("\nKontak Ditemukan:")
            print(f"Nama: {kontak['nama']}")
            print(f"Telepon: {kontak['telepon']}")
            print(f"Email: {kontak['email']}")
            ditemukan = True
            break # Berhenti setelah menemukan kontak pertama yang cocok
    if not ditemukan:
        print(f"Kontak dengan nama '{kata_kunci}' tidak ditemukan.")

def hapus_kontak(daftar_kontak):
    """Menghapus kontak berdasarkan nama."""
    print("\n-------- Hapus Kontak --------")
    nama_hapus = input("Masukkan nama kontak yang ingin dihapus: ").strip().title()
    ditemukan = False
    for i, kontak in enumerate(daftar_kontak):
        if kontak['nama'].lower() == nama_hapus.lower():
            konfirmasi = input(f"Anda yakin ingin menghapus kontak '{kontak['nama']}'? (ya/tidak): ").lower()
            if konfirmasi == 'ya':
                del daftar_kontak[i]
                print(f"Kontak '{nama_hapus}' berhasil dihapus.")
            else:
                print("Penghapusan dibatalkan.")
            ditemukan = True
            break
    if not ditemukan:
        print(f"Kontak dengan nama '{nama_hapus}' tidak ditemukan.")

def main_manajemen_kontak():
    """Fungsi utama untuk menjalankan program."""
    kontak = [] # List untuk menyimpan semua kontak

    while True:
        tampilkan_menu()
        pilihan = input("Pilih opsi (1-5): ").strip()

        if pilihan == '1':
            tambah_kontak(kontak)
        elif pilihan == '2':
            lihat_semua_kontak(kontak)
        elif pilihan == '3':
            cari_kontak(kontak)
        elif pilihan == '4':
            hapus_kontak(kontak)
        elif pilihan == '5':
            print("\nTerima kasih telah menggunakan Sistem Manajemen Kontak!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Panggil fungsi utama
if __name__ == "__main__":
    main_manajemen_kontak()
