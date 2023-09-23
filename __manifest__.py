{
    'name': 'Sistem Management Rumah Sakit',

    'summary': """
        Module Sistem Manajemen Rumah Sakit""",

    'description': """
        Manajemen Rumah Sakit
    """,
    'sequence': -50,
    'author': "Nama kamu",
    'website': "Kosong",

    'depends': [
        'mail',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/pasien_view.xml',
        'views/pasien_wanita_view.xml',
        'views/pasien_pria_view.xml',
        'views/janjitemu_view.xml',
    ],

    'category': 'Uncategorized',
    'version': '0.1',

    'installable': True,
    'application': True,    
    'auto_install': False,
    
    'license': 'LGPL-3',
}