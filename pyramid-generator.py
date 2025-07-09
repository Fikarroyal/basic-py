def tampilkan_intro():
    """Menampilkan pesan pengantar untuk program."""
    print("=" * 60)
    print("               Generator Bintang Piramida.             ")
    print("=" * 60)
    print("Program ini akan membuat piramida bintang di konsol.")
    print("Anda hanya perlu memasukkan tinggi piramida yang diinginkan.")
    print("-" * 60)

def gambar_piramida(tinggi):
    """Menggambar pola piramida bintang."""
    print(f"\n-------------------- Piramida Tinggi {tinggi} --------------------")
    for i in range(1, tinggi + 1):
        # Cetak spasi sebelum bintang (untuk memusatkan piramida)
        # Jumlah spasi = tinggi - nomor baris
        print(" " * (tinggi - i), end="")
        
        # Cetak bintang
        # Jumlah bintang = (2 * nomor baris) - 1
        print("*" * (2 * i - 1))
    print("-" * 60)

def main_generator_piramida():
    """Fungsi utama untuk menjalankan generator piramida."""
    tampilkan_intro()

    while True:
        try:
            input_tinggi = input("Masukkan tinggi piramida (bilangan bulat positif) atau 'keluar': ").strip()
            
            if input_tinggi.lower() == 'keluar':
                print("\nTerima kasih telah menggunakan Generator Pola Piramida Bintang! Sampai jumpa.")
                break

            tinggi = int(input_tinggi)

            if tinggi <= 0:
                print("Tinggi piramida harus bilangan bulat positif. Coba lagi.")
            else:
                gambar_piramida(tinggi)
                lanjut = input("Ingin membuat piramida lain? (ya/tidak): ").lower().strip()
                if lanjut != 'ya':
                    print("\nTerima kasih telah menggunakan Generator Pola Piramida Bintang! Sampai jumpa.")
                    break

        except ValueError:
            print("Input tidak valid! Masukkan bilangan bulat untuk tinggi.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

# Jalankan program
if __name__ == "__main__":
    main_generator_piramida()
