# -*- coding: utf-8 -*-

from odoo import fields, models


class CouponProgram(models.Model):
    _inherit = "coupon.program"

    lot_specific = fields.Boolean('Lot Specific',defult=False)
    specific_lot_ids = fields.Many2many('stock.production.lot', string='Specific Lots')