odoo.define('pos_lot_promo.pos', function (require) {
    'use strict';
    const models = require('point_of_sale.models');
    var rpc = require('web.rpc');

    var _order_super = models.Order.prototype;
    models.Order = models.Order.extend({
        applyPromotion: async function (program_id) {
            var self = this;
            const promoProgram = this.pos.promo_programs.find(
                (program) => program.id == program_id);
            const order = this.pos.get_order();
            let selectedLine = order.get_selected_orderline()
            if (promoProgram.lot_specific && selectedLine.has_product_lot){
                var order_line_lots = selectedLine.get_lot_lines().map((line) =>(line.attributes['lot_name']))
                order_line_lots.forEach(function(lot_name){
                    var lot_domain = [['name', '=', lot_name]]
                    rpc.query({
                        model: 'stock.production.lot',
                        method: 'search_read',
                        args: [lot_domain, ['id']],
                        kwargs: {
                            limit: 1,
                        }
                    }).then(function (lot_id) {
                        if (promoProgram.specific_lot_ids.includes(lot_id[0].id)){
                            _order_super.applyPromotion.call(self, program_id);
                        }
                    })
                })
            }
                // if ( promoProgram && !(order.activePromoProgramIds.includes(program_id))) {
                //     this.activePromoProgramIds.push(promoProgram.id);
                //     this.trigger('update-rewards');
                // }
        },
    })
})