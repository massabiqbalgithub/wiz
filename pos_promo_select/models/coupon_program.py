# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
import random


class CouponProgram(models.Model):
    _inherit = "coupon.program"


    @api.model
    def create(self, vals):
        if not vals.get('promo_code'):
            vals.update({
                'promo_code': random.randint(0,9999)
            })
        return super(CouponProgram,self).create(vals)