"""
Aplikasi Deteksi Gempa Terkini
Modularisasi dengan Function
Modularisasi dengan Package
"""

import deteksigempa

if __name__ == '__main__':
    gempa_di_indonesia = deteksigempa('https://bmkg.go.id')
    print(f'Aplikas utama menggunakan package yg memiliki deskripsi {deteksigempa.Description}')
    gempa_di_indonesia.tampilkan_keterangan()
    gempa_di_indonesia.run()
