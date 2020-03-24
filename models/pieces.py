# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Repair(models.Model):
    _name = 'garage.pieces'
    _description = 'Pieces used to repair vehicles'
    _order = 'date desc'

    name = fields.Char(string='Piece code')
    date = fields.Date(string='Date', default=lambda self: fields.Date.today())
    price = fields.Float(string='Unit price (€)', digits=(10, 2), required=True)
    piece = fields.Char(string='Piece', required=True)
    unit = fields.Integer(string='Units', required=True, default=1)
    provider = fields.Char(string='Provider', size=20)
    repair_code = fields.Many2one('garage.repair', 'repair_code')


