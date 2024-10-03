# Booking Ruangan Odoo Module
by Natanael Jansudin Siregar (https://www.natanaelsiregar.me/)

## Deskripsi
Modul **Booking Ruangan** dirancang untuk mengelola ruangan dan pemesanan di Odoo. Modul ini mencakup fitur:
- Pengelolaan master ruangan (Meeting Room Kecil, Meeting Room Besar, Aula).
- Pemesanan ruangan dengan nomor otomatis menggunakan sequence.
- Validasi untuk mencegah pemesanan duplikat pada ruangan dan tanggal yang sama.
- Tampilan grid dan list untuk manajemen ruangan dan pemesanan.

## Fitur Utama
- **Master Ruangan**: Mengelola ruangan dengan tipe, lokasi, kapasitas, dan foto.
- **Pemesanan Ruangan**: Pemesanan dengan validasi, status, dan catatan.
- **Nomor Pemesanan Otomatis**: Menggunakan sequence `PR/` dengan padding 4 digit.

## Prasyarat
- Odoo 18 atau versi lebih baru.
- Modul `base` harus sudah terinstal (otomatis tergantung oleh Odoo).

## Instalasi

### 1. Clone Repository ke Odoo Addons Directory
Clone modul ini ke dalam direktori addons Odoo Anda:
```bash
cd /path/to/odoo/addons
git clone https://github.com/natanaelsiregar/Sr_SE_Natanael-Jansudin-Siregar_Technical-Assessment_241003.git
cd /Technical Assessment II
```

### 2. Struktur Direktori
Setelah di-clone, pastikan struktur direktori sebagai berikut:
```bash
booking_ruangan/
│
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── master_ruangan.py
│   └── pemesanan_ruangan.py
├── views/
│   ├── master_ruangan_views.xml
│   └── pemesanan_ruangan_views.xml
└── data/
    └── sequence_data.xml
```

### 2. Restart Odoo
```bash
sudo systemctl restart odoo
```

Atau, jika Anda menjalankan Odoo secara manual:
```bash
./odoo-bin -c /etc/odoo.conf
```

### 4. Aktifkan Developer Mode di Odoo
* Login ke Odoo.
* Buka menu Settings.
* Scroll ke bawah dan klik Activate the Developer Mode.

### 5. Install Modul
* Pergi ke aplikasi Apps.
* Klik Update Apps List untuk memperbarui daftar aplikasi.
* Cari modul Booking Ruangan dan klik Install.

## Penggunaan
* Master Ruangan
* Masuk ke menu Ruangan di aplikasi yang baru terinstal.
* Tambahkan ruangan baru, isi semua kolom wajib seperti nama, tipe, lokasi, dan kapasitas.

### Pemesanan Ruangan
* Masuk ke menu Pemesanan Ruangan.
* Tambahkan pemesanan baru dengan memilih ruangan yang tersedia, nama pemesan, dan tanggal pemesanan.
* Pemesanan dengan status Draft dapat diproses menjadi On Going dan kemudian diselesaikan (Done).

### Validasi
Modul ini dilengkapi dengan beberapa validasi:

* Nama Pemesan Unik: Nama pemesan tidak boleh duplikat.
* Nama Ruangan Unik: Nama ruangan harus unik.
* Ruangan Tidak Bisa Dipesan di Tanggal yang Sama: Tidak bisa memesan ruangan pada tanggal yang sama lebih dari satu kali.