odoo.define('pos_lot_promo.pos', function (require) {
    'use strict';
    const models = require('point_of_sale.models');

    models.Order = models.Order.extend({
        _getSpecificDiscount: function (program, coupon_id, productRewards) {
            const productIdsToAccount = new Set();
            const amountsToDiscount = {};
            
            var self = this
            for (let line of this._getRegularOrderlines()) {
                // Lot Specific Logic
                if (program.lot_specific){
                    if (line.has_product_lot){
                        var lot_name = line.get_lot_lines()[0].attributes['lot_name']
                        var lot_id = this.pos.production_lots.find(lot => lot.name == lot_name)
                        if (program.specific_lot_ids.includes(lot_id.id)){
                            const key = self._getGroupKey(line);
                            if (!(key in amountsToDiscount)) {
                                amountsToDiscount[key] = line.get_quantity() * line.price;
                            } else {
                                amountsToDiscount[key] += line.get_quantity() * line.price;
                            }
                            productIdsToAccount.add(line.get_product().id);
                        } 
                    }    
                } 
                if (!(program.lot_specific) && program.discount_specific_product_ids.has(line.get_product().id)) {
                    // Odoo promotion code (not lot specific)
                    const key = this._getGroupKey(line);
                    if (!(key in amountsToDiscount)) {
                        amountsToDiscount[key] = line.get_quantity() * line.price;
                    } 
                    else {
                        amountsToDiscount[key] += line.get_quantity() * line.price;
                    }
                    productIdsToAccount.add(line.get_product().id);
                }
            }
            this._considerProductRewards(amountsToDiscount, productIdsToAccount, productRewards);
            return this._createDiscountRewards(program, coupon_id, amountsToDiscount);
        },
    })

})