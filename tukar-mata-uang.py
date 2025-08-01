NILAI_TUKAR = {
    "USD": 16500.00,  # Dolar Amerika Serikat
    "EUR": 18000.00,  # Euro
    "JPY": 110.00,    # Yen Jepang (per 1 Yen)
    "GBP": 21000.00,  # Pound Sterling Inggris
    "AUD": 11000.00,  # Dolar Australia
    "CAD": 12500.00,  # Dolar Kanada
    "CHF": 17500.00,  # Franc Swiss
    "CNY": 2300.00,   # Yuan Tiongkok
    "SGD": 12000.00,  # Dolar Singapura
    "HKD": 2100.00,   # Dolar Hong Kong
    "MYR": 3700.00,   # Ringgit Malaysia
    "KRW": 12.50,     # Won Korea Selatan (per 1 Won)
    "THB": 470.00,    # Baht Thailand
    "INR": 200.00,    # Rupee India
    "PHP": 280.00,    # Peso Filipina
    "IDR": 1.00       # Rupiah Indonesia (basis)
}

def tampilkan_menu():
    """Menampilkan menu opsi konversi dan daftar mata uang."""
    print("\n" + "=" * 51)
    print("  Pertukaran mata uang rupiah dgn mata uang asing  ")
    print("=" * 51)
    print("Mata Uang Asing Tersedia:")
    # Buat string daftar mata uang asing dengan rapi
    mata_uang_asing_list = [k for k in NILAI_TUKAR.keys() if k != "IDR"]
    # Pisahkan per 5 mata uang untuk kerapihan
    for i in range(0, len(mata_uang_asing_list), 5):
        print(f"  {', '.join(mata_uang_asing_list[i:i+5])}")
    print("-" * 50)
    print("1. Konversi dari Rupiah (IDR)")
    print("2. Konversi ke Rupiah (IDR)")
    print("3. Tampilkan Semua Nilai Tukar")
    print("4. Keluar")
    print("-" * 50)

def konversi_dari_rupiah(nilai_tukar_data):
    """Mengkonversi Rupiah ke mata uang asing."""
    print("\n----------- Konversi dari Rupiah (IDR) -----------")
    try:
        jumlah_idr_str = input("Masukkan jumlah Rupiah (IDR): ")
        jumlah_idr = float(jumlah_idr_str)
        if jumlah_idr < 0:
            print("Jumlah tidak boleh negatif.")
            return

        mata_uang_tujuan = input("Konversi ke mata uang apa (contoh: USD, EUR, JPY)? ").upper().strip()

        if mata_uang_tujuan not in nilai_tukar_data or mata_uang_tujuan == "IDR":
            print("Kode mata uang tujuan tidak valid atau tidak didukung.")
            return

        nilai_kurs = nilai_tukar_data[mata_uang_tujuan]
        hasil_konversi = jumlah_idr / nilai_kurs
        
        print("\n" + "=" * 40)
        print(f"  IDR {jumlah_idr:,.2f} = {mata_uang_tujuan} {hasil_konversi:,.2f}")
        print("=" * 40)
        print(f"(Kurs 1 {mata_uang_tujuan} = IDR {nilai_kurs:,.2f})")

    except ValueError:
        print("Input jumlah tidak valid. Masukkan angka.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def konversi_ke_rupiah(nilai_tukar_data):
    """Mengkonversi mata uang asing ke Rupiah."""
    print("\n--- Konversi ke Rupiah (IDR) ---")
    try:
        mata_uang_asal = input("Konversi dari mata uang apa (contoh: USD, EUR, JPY)? ").upper().strip()

        if mata_uang_asal not in nilai_tukar_data or mata_uang_asal == "IDR":
            print("Kode mata uang asal tidak valid atau tidak didukung.")
            return

        jumlah_asing_str = input(f"Masukkan jumlah {mata_uang_asal}: ")
        jumlah_asing = float(jumlah_asing_str)
        if jumlah_asing < 0:
            print("Jumlah tidak boleh negatif.")
            return

        nilai_kurs = nilai_tukar_data[mata_uang_asal]
        hasil_konversi = jumlah_asing * nilai_kurs
        
        print("\n" + "=" * 40)
        print(f"  {mata_uang_asal} {jumlah_asing:,.2f} = IDR {hasil_konversi:,.2f}")
        print("=" * 40)
        print(f"(Kurs 1 {mata_uang_asal} = IDR {nilai_kurs:,.2f})")

    except ValueError:
        print("Input jumlah tidak valid. Masukkan angka.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def tampilkan_semua_nilai_tukar(nilai_tukar_data):
    """Menampilkan semua nilai tukar yang tersedia."""
    print("\n--- Semua Nilai Tukar (IDR) ---")
    print("Mata Uang | Kurs per 1 Unit")
    print("----------------------------")
    # Urutkan berdasarkan kode mata uang untuk tampilan yang rapi
    sorted_mata_uang = sorted([k for k in nilai_tukar_data.keys() if k != "IDR"])
    
    for mata_uang in sorted_mata_uang:
        kurs = nilai_tukar_data[mata_uang]
        print(f"{mata_uang.ljust(9)} | IDR {kurs:,.2f}")
    print("----------------------------")
    print("Perhatian: Kurs ini adalah asumsi per 1 Agustus 2025 dan tidak real-time.")

def main_konverter_mata_uang_lanjutan():
    """Fungsi utama untuk menjalankan aplikasi konverter multi-mata uang."""
    while True:
        tampilkan_menu()
        pilihan = input("Pilih opsi (1-4): ").strip()

        if pilihan == '1':
            konversi_dari_rupiah(NILAI_TUKAR)
        elif pilihan == '2':
            konversi_ke_rupiah(NILAI_TUKAR)
        elif pilihan == '3':
            tampilkan_semua_nilai_tukar(NILAI_TUKAR)
        elif pilihan == '4':
            print("\nTerima kasih telah menggunakan Konverter Mata Uang Rupiah Multi-Mata Uang! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Jalankan aplikasi
if __name__ == "__main__":
    main_konverter_mata_uang_lanjutan()
