odoo.define('pos_lot_promo.models', function(require) {
    "use strict";

    var models = require('point_of_sale.models');

    models.load_fields("coupon.program", ["lot_specific", "specific_lot_ids"]);
});