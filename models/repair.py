# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Repair(models.Model):
    _name = 'workshop.repair'
    _description = 'History repairs'
    _order = 'repair_date asc'

    name = fields.Char(string='Repair code', compute='_repair_id', store=True)
    repair_date = fields.Date(string='Date', default=lambda self: fields.Date.today())
    time_required = fields.Integer(string='Time required (mins)',
                                   help='Time required to repair de vehicle in minutes', required=True)
    workforce_price = fields.Float(string='Price workforce (€/h)', digits=(5, 2), default=37.5, required=True)
    total_price = fields.Float(string='Total (€)', digits=(10, 2), compute='_total_price', store=True)
    vehicle = fields.Many2one('workshop.vehicle', 'vehicle')
    failure = fields.Text(string='Failure', required=True)
    paid = fields.Boolean(string="Paid", default=False)

    pieces = fields.One2many('workshop.pieces')

    @api.depends('repair_date', 'vehicle')
    def _repair_id(self):
        for repair in self:
            repair.name = ''
            if repair.vehicle:
                repair.name = repair.repair_date.strftime("%d/%m/%Y") + "-" + str(repair.vehicle.name)

    @api.depends('workforce_price', 'time_required', 'pieces')
    def _total_price(self):
        for price in self:
            price.total_price = 0
            if price.workforce_price and price.time_required:

