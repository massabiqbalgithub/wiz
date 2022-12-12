# -*- coding: utf-8 -*-

{
    'name': "Remove Order Line(Promotion) In POS ",
    'summary': """
        Remove Individual Orderlines(Promotion) In Point Of Sale. """,
    'description': """
        Remove promotion lines of selected order line by simply clicking X button. 
    """,
    'author': "Fazal, Massab",
    'category': 'Point of Sale',
    'version': '15.0.1.0',
    'depends': ['base', 'point_of_sale'],
    'assets': {
        'web.assets_backend': [
            'pos_remove_line/static/src/js/clear_order_line.js',
        ],
        'web.assets_qweb': [
             'pos_remove_line/static/src/xml/clear_order_line.xml',
        ],
    },
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,

}
