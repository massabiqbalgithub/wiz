odoo.define('pos_promo_select.pos', function (require) {
    'use strict';
    const models = require('point_of_sale.models');
    const { Gui } = require('point_of_sale.Gui');
    

    var _order_super = models.Order.prototype;
    models.Order = models.Order.extend({
        applyPromotion: async function (program_id) {
            const promoProgram = this.pos.promo_programs.find(
                (program) => program.id == program_id);
                const order = this.pos.get_order();
                if (promoProgram) {
                    if (order.activePromoProgramIds.includes(program_id)){
                        Gui.showNotification('That promo code program has already been activated.');
                    }
                    else{
                        this.activePromoProgramIds.push(promoProgram.id);
                        this.trigger('update-rewards');
                    }
            }
        },
    })
})