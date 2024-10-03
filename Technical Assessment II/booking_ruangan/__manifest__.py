{
    'name': 'Booking Ruangan',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Modul untuk Pemesanan Ruangan',
    'description': """
        Modul untuk mengelola pemesanan ruangan, seperti meeting room atau aula.
    """,
    'author': 'Natanael Jansudin Siregar',
    'website': 'https://www.natanaelsiregar.me/',
    'depends': ['base'],
    'data': [
        'views/master_ruangan_views.xml',
        'views/pemesanan_ruangan_views.xml',
        'data/sequence_data.xml',
    ],
    'installable': True,
    'application': True,
}
