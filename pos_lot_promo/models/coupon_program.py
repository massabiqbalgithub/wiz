# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class CouponProgram(models.Model):
    _inherit = "coupon.program"

    lot_specific = fields.Boolean('Lot Specific',defult=False)
    specific_lot_ids = fields.Many2many('stock.production.lot', string='Specific Lots')

    @api.onchange('specific_lot_ids')
    def _onchange_specific_lot_ids(self):
        if self.lot_specific and self.specific_lot_ids:
            lot_product_domain = [('id','in',self.specific_lot_ids.mapped('product_id').ids)]
            return {'domain': {'discount_specific_product_ids': lot_product_domain}}