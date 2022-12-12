odoo.define('pos_promo_select.ApplyPromoButton', function (require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const { useListener } = require('web.custom_hooks');
    const Registries = require('point_of_sale.Registries');

    class ApplyPromoButton extends PosComponent {
        constructor() {
            super(...arguments);
            useListener('click', this.onClick);
        }
        async onClick() {
            const selectionList = this.env.pos.promo_programs.map((program) => ({
                id: program.id,
                label: program.name,
                isSelected: false,
                item: {id:program.id,name:program.name},
            }));
            this.showPopup('SelectionPopup', {
                title: this.env._t('Apply Promotion Program'),
                list: selectionList,
            }).then(({ confirmed, payload: selectedProgram }) => {
                if (confirmed) {
                    const order = this.env.pos.get_order();
                    order.applyPromotion(selectedProgram.id);
                }
            });
        }
    }
    ApplyPromoButton.template = 'ApplyPromoButton';

    ProductScreen.addControlButton({
        component: ApplyPromoButton,
        condition: function () {
            return this.env.pos.config.use_coupon_programs;
        },
    });

    Registries.Component.add(ApplyPromoButton);

    return ApplyPromoButton;
});
