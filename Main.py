"""
Aplikasi Informasi Gempa BMKG
Modularisasi dengan Function
Modularisasi dengan Package
"""

import deteksigempa

if __name__ == '__main__':
    gempa_di_indonesia = deteksigempa.deteksigempa('https://bmkg.go.id')
    print(f'Aplikasi utama menggunakan package yg memiliki deskripsi {gempa_di_indonesia.Description}')
    gempa_di_indonesia.tampilkan_keterangan()
    gempa_di_indonesia.run()
