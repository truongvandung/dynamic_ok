{
    'name': 'Dynamic ListView Odoo 10 Advance',
    'summary': 'Dynamic ListView Odoo 10 Advance',
    'version': '1.0',
    'category': 'Web',
    'description': """
       Dynamic ListView Odoo 10 Supper Advance
    """,
    'author': "startup",
    'depends': ['web'],
    'data': [
        'views/templates.xml',
        'security/show_fields_security.xml',
        'security/ir.model.access.csv',
    ],
    'qweb': [
        'static/src/xml/base.xml',
    ],
    'images': ['images/main_screen.jpg'],
    'price': 99,
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
    'application': False,
    'images': [
        'static/description/module_image.png',
    ],
}
