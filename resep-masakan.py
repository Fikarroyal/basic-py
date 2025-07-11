def tampilkan_menu():
    """Menampilkan menu utama aplikasi resep."""
    print("\n" + "=" * 40)
    print("     Sistem Manajemen Resep Masakan.    ")
    print("=" * 40)
    print("1. Tambah Resep Baru")
    print("2. Lihat Semua Resep")
    print("3. Cari Resep")
    print("4. Keluar")
    print("-" * 40)

def tambah_resep(daftar_resep):
    """Menambahkan resep baru ke dalam daftar."""
    print("\n----------- Tambah Resep Baru ----------")
    nama_resep = input("Nama Resep: ").strip().title()
    if not nama_resep:
        print("Nama resep tidak boleh kosong.")
        return

    # Cek apakah resep sudah ada
    if nama_resep in daftar_resep:
        print(f"Resep '{nama_resep}' sudah ada dalam daftar. Silakan perbarui atau gunakan nama lain.")
        return

    print("Masukkan bahan-bahan (satu per baris, ketik 'selesai' untuk mengakhiri):")
    bahan_bahan = []
    while True:
        bahan = input("- ").strip()
        if bahan.lower() == 'selesai':
            break
        if bahan: # Hanya tambahkan jika tidak kosong
            bahan_bahan.append(bahan.capitalize())
    
    if not bahan_bahan:
        print("Bahan-bahan tidak boleh kosong. Resep tidak ditambahkan.")
        return

    print("Masukkan instruksi (satu per baris, ketik 'selesai' untuk mengakhiri):")
    instruksi = []
    while True:
        instruksi_baris = input("- ").strip()
        if instruksi_baris.lower() == 'selesai':
            break
        if instruksi_baris: # Hanya tambahkan jika tidak kosong
            instruksi.append(instruksi_baris)

    if not instruksi:
        print("Instruksi tidak boleh kosong. Resep tidak ditambahkan.")
        return

    daftar_resep[nama_resep] = {
        'bahan': bahan_bahan,
        'instruksi': instruksi
    }
    print(f"Resep '{nama_resep}' berhasil ditambahkan!")

def lihat_semua_resep(daftar_resep):
    """Menampilkan semua resep dalam daftar."""
    print("\n---------- Daftar Semua Resep ----------")
    if not daftar_resep:
        print("Daftar resep masih kosong.")
        return

    for nama, detail in daftar_resep.items():
        print(f"\nResep: **{nama}**")
        print("  Bahan-bahan:")
        for i, bahan in enumerate(detail['bahan'], 1):
            print(f"    {i}. {bahan}")
        print("  Instruksi:")
        for i, langkah in enumerate(detail['instruksi'], 1):
            print(f"    {i}. {langkah}")
        print("-" * 40) # Garis pemisah antar resep

def cari_resep(daftar_resep):
    """Mencari dan menampilkan resep berdasarkan nama."""
    print("\n-------------- Cari Resep --------------")
    kata_kunci = input("Masukkan nama resep yang ingin dicari: ").strip().title()

    if kata_kunci in daftar_resep:
        detail = daftar_resep[kata_kunci]
        print(f"\nResep Ditemukan: **{kata_kunci}**")
        print("  Bahan-bahan:")
        for i, bahan in enumerate(detail['bahan'], 1):
            print(f"    {i}. {bahan}")
        print("  Instruksi:")
        for i, langkah in enumerate(detail['instruksi'], 1):
            print(f"    {i}. {langkah}")
        print("-" * 30)
    else:
        print(f"Resep '{kata_kunci}' tidak ditemukan.")

def main_manajemen_resep():
    """Fungsi utama untuk menjalankan aplikasi manajemen resep."""
    resep_masakan = {} # Dictionary untuk menyimpan resep

    while True:
        tampilkan_menu()
        pilihan = input("Pilih opsi (1-4): ").strip()

        if pilihan == '1':
            tambah_resep(resep_masakan)
        elif pilihan == '2':
            lihat_semua_resep(resep_masakan)
        elif pilihan == '3':
            cari_resep(resep_masakan)
        elif pilihan == '4':
            print("\nTerima kasih telah menggunakan Sistem Manajemen Resep Masakan Kami! Selamat Memasak.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Jalankan fungsi utama
if __name__ == "__main__":
    main_manajemen_resep()
