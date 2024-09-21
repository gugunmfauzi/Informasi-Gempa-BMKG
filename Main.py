"""
Aplikasi Informasi Gempa BMKG
Modularisasi dengan Function
"""


def ekstraksi_data():
    """
    Tanggal : 21 September 2024
    Waktu : 06:26:20 WIB
    Magnitudo : 4.8
    Kedalaman : 22 km
    Lokasi : LS=8.57 BT=115.32
    Pusat gempa : berada di darat 3 km baratdaya Gianyar
    Dirasakan : (Skala MMI): IV Gianyar, III Badung, III Denpasar, III Tabanan, III Karangasem, III Bangli, II Buleleng, II Mataram, II Lombok Barat
    :return:
    """
    hasil = dict()
    hasil['Tanggal'] = '21 September 2024'
    hasil['Waktu'] = '06:26:20 WIB'
    hasil['Magnitudo'] = 4.8
    hasil['Kedalaman'] = '22 km'
    hasil['Lokasi'] = {'LS': 8.57, 'BT': 115.32}
    hasil['Pusat gempa'] = 'berada di darat 3 km baratdaya Gianyar'
    hasil['Dirasakan'] = '(Skala MMI): IV Gianyar, III Badung, III Denpasar, III Tabanan, III Karangasem, III Bangli, II Buleleng, II Mataram, II Lombok Barat'

    return hasil

def tampilkan_data(result):
    print('Gempa Terkahir Berdasarkan BMKG')
    print(f"Tanggal {result['Tanggal']}")
    print(f"Waktu {result['Waktu']}")
    print(f"Magnitudo {result['Magnitudo']}")
    print(f"Kedalaman {result['Kedalaman']}")
    print(f"Lokasi: LS={result['Lokasi']['LS']}, BT={result['Lokasi']['BT']}")
    print(f"Pusat gempa {result['Pusat gempa']}")
    print(f"Dirasakan {result['Dirasakan']}")


if __name__ == '__main__':
    print('Aplikasi Utama')
    result = ekstraksi_data()
    tampilkan_data(result)