# -*- coding: utf-8 -*-
#################################################################################

#################################################################################

{
    "name": "POS Lot Selection",
    "version": "1.0",
    "summary": "This module allows user to select Lot/Serial based on Product in Point of sale from current location along with providing an unique design for lot and serial selection individually.| POS Lot Selection | POS Lots | POS Serial Selection | POS Serial | Point of Sale Lots | Point of Sale Serial | Existing Lots from System | Select Lots | Select Serial | Existing Lots | Existing Serial",
    'description': """
POS Lot Selection
==============================================
    =>Usually Default odoo doesn't provide a feature of lot selection in point of sale, to be specific there are not lot or serial masters being loaded to point of sale, it performs reverse process of creating new lot based on value received from pos order.
    =>This module will be helpful for users to cross-check items available in stock for specific lot to deduct items from specific lot.

    """,
    'license': 'OPL-1',
    "category": "Sales/Point Of Sale",
    "website": "https://www",
    'author': 'Aut',
    "depends": ['point_of_sale'],
    'assets': {
        'point_of_sale.assets': [
            "pos_lot_selection_knk/static/src/js/models.js",
            "pos_lot_selection_knk/static/src/js/ProductLotPopup.js",
            "pos_lot_selection_knk/static/src/js/OrderWidget.js",
            "pos_lot_selection_knk/static/src/js/ProductScreen.js",
        ],
        'web.assets_qweb': [
            'pos_lot_selection_knk/static/src/xml/ProductLotPopup.xml',
            'pos_lot_selection_knk/static/src/xml/Orderline.xml',
        ],
     },
    'images': ['static/description/banner.gif'],
    'sequence': 1000,
    "application": False,
    "installable": True,
}
