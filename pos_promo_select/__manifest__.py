# -*- coding: utf-8 -*-

{
    "name": "POS Promotion Selection",
    "version": "1.2",
    "summary": "This module allows user to select promotion based on Product in Point of sale.| POS Promotion Selection",
    'description': """
POS Promtion Selection
==============================================
    =>Usually Default odoo doesn't provide a feature of promotion selection in point of sale.
    """,
    'license': 'OPL-1',
    "category": "Sales/Point Of Sale",
    "website": "https://www",
    'author': 'Fazal, Massab',
    "depends": ['point_of_sale'],
    'assets': {
        'point_of_sale.assets': [
            "pos_promo_select/static/src/js/order.js",
            "pos_promo_select/static/src/js/ControlButtons/ApplyPromoButton.js",
        ],
        'web.assets_qweb': [
            'pos_promo_select/static/src/xml/ControlButtons/ApplyPromoButton.xml',
        ],
     },
    "application": False,
    "installable": True,
}
