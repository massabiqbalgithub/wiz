# -*- coding: utf-8 -*-

{
    "name": "POS Promotion Lot Specific",
    "version": "1.2",
    "summary": "This module allows user to set promotion based on Product Lot in Point of sale.| POS Promotion Lot Specific",
    'description': """
POS Promotion Lot Specific Selection
==============================================
    =>Usually Default odoo doesn't provide a feature of promotion based on lot in point of sale.
    """,
    'license': 'OPL-1',
    "category": "Sales/Point Of Sale",
    "website": "https://www",
    'author': 'Fazal, Massab',
    "depends": ['point_of_sale','pos_promo_select'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/coupon_program.xml',
        # 'views/templates.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            "pos_lot_promo/static/src/js/order.js",
            "pos_lot_promo/static/src/js/models.js",
        ],
    # 'web.assets_qweb': [
        #     'pos_promo_select/static/src/xml/ControlButtons/ApplyPromoButton.xml',
        # ],
     },
    "application": False,
    "installable": True,
}
