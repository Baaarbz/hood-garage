# -*- coding: utf-8 -*-

from odoo import models, fields


class Mechanic(models.Model):
    _name = 'garage.mechanic'
    _inherit = 'garage.user'
    _description = 'Hired mechanics in the garage'

    qualified = fields.Boolean(string='Qualified to work on electric cars', default=False)
