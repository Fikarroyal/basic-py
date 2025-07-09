def tampilkan_menu():
    """Menampilkan opsi menu utama kepada pengguna."""
    print("\n" + "=" * 35)
    print("  Sistem Manajemen Daftar Belanja  ")
    print("=" * 35)
    print("1. Tambah Item ke Daftar Belanja")
    print("2. Lihat Daftar Belanja")
    print("3. Tandai Item Sudah Dibeli")
    print("4. Hapus Item dari Daftar")
    print("5. Bersihkan Daftar (Hapus Semua Item)")
    print("6. Keluar")
    print("-" * 35)

def tambah_item(daftar_belanja):
    """Menambahkan item baru ke daftar belanja."""
    print("\n----------- Tambah Item -----------")
    item = input("Masukkan nama item yang ingin ditambahkan: ").strip().title()
    if not item:
        print("Nama item tidak boleh kosong!")
        return

    # Menambahkan item sebagai dictionary dengan status 'belum dibeli'
    daftar_belanja.append({"nama": item, "dibeli": False})
    print(f"'{item}' berhasil ditambahkan ke daftar.")

def lihat_daftar(daftar_belanja):
    """Menampilkan semua item dalam daftar belanja beserta statusnya."""
    print("\n------- Daftar Belanja Anda -------")
    if not daftar_belanja:
        print("Daftar belanja Anda kosong.")
        return

    for i, item in enumerate(daftar_belanja, 1):
        status = "✅ Dibeli" if item["dibeli"] else "❌ Belum Dibeli"
        print(f"{i}. {item['nama']} ({status})")
    print("-" * 35)

def tandai_dibeli(daftar_belanja):
    """Menandai item tertentu sebagai sudah dibeli."""
    print("\n----- Tandai Item Sudah Dibeli ----")
    lihat_daftar(daftar_belanja) # Tampilkan daftar untuk memudahkan pemilihan
    if not daftar_belanja: # Cek lagi jika daftar kosong setelah tampilkan_daftar
        return

    try:
        nomor_item = int(input("Masukkan nomor item yang sudah dibeli: "))
        if 1 <= nomor_item <= len(daftar_belanja):
            daftar_belanja[nomor_item - 1]["dibeli"] = True
            print(f"'{daftar_belanja[nomor_item - 1]['nama']}' berhasil ditandai sebagai sudah dibeli.")
        else:
            print("Nomor item tidak valid.")
    except ValueError:
        print("Input tidak valid! Masukkan nomor.")

def hapus_item(daftar_belanja):
    """Menghapus item tertentu dari daftar belanja."""
    print("\n----------- Hapus Item ------------")
    lihat_daftar(daftar_belanja) # Tampilkan daftar untuk memudahkan pemilihan
    if not daftar_belanja: # Cek lagi jika daftar kosong setelah tampilkan_daftar
        return

    try:
        nomor_item = int(input("Masukkan nomor item yang ingin dihapus: "))
        if 1 <= nomor_item <= len(daftar_belanja):
            item_terhapus = daftar_belanja.pop(nomor_item - 1)
            print(f"'{item_terhapus['nama']}' berhasil dihapus dari daftar.")
        else:
            print("Nomor item tidak valid.")
    except ValueError:
        print("Input tidak valid! Masukkan nomor.")

def bersihkan_daftar(daftar_belanja):
    """Menghapus semua item dari daftar belanja."""
    if not daftar_belanja:
        print("\nDaftar belanja sudah kosong.")
        return

    konfirmasi = input("\nAnda yakin ingin membersihkan seluruh daftar belanja? (ya/tidak): ").lower()
    if konfirmasi == 'ya':
        daftar_belanja.clear()
        print("Daftar belanja berhasil dikosongkan.")
    else:
        print("Pembersihan daftar dibatalkan.")

def main_daftar_belanja():
    """Fungsi utama untuk menjalankan aplikasi daftar belanja."""
    daftar_belanja = [] # List untuk menyimpan item belanja

    while True:
        tampilkan_menu()
        pilihan = input("Pilih opsi (1-6): ").strip()

        if pilihan == '1':
            tambah_item(daftar_belanja)
        elif pilihan == '2':
            lihat_daftar(daftar_belanja)
        elif pilihan == '3':
            tandai_dibeli(daftar_belanja)
        elif pilihan == '4':
            hapus_item(daftar_belanja)
        elif pilihan == '5':
            bersihkan_daftar(daftar_belanja)
        elif pilihan == '6':
            print("\nTerima kasih telah menggunakan Sistem Manajemen Daftar Belanja! Selamat berbelanja!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Panggil fungsi utama saat script dijalankan
if __name__ == "__main__":
    main_daftar_belanja()
