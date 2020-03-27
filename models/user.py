# -*- coding: utf-8 -*-

from odoo import models, fields, api
import re
from odoo.exceptions import ValidationError


class User(models.Model):
    _name = 'garage.user'
    _order = 'last_name desc'
    _sql_constraints = [
        ('unique_id_card', 'unique(id_card)', 'There are an user registered with the same ID Card.')]

    name = fields.Char(string='Name', required=True)
    last_name = fields.Char(string='Last name', required=True)
    id_card = fields.Char(string='ID Card', help='Valid formats: 00000000A or A0000000A', required=True, size=9)
    address = fields.Char(string='Address', required=True)
    zip_code = fields.Integer(string='ZIP Code', size=5)

    @api.constrains('id_card')
    def _constrain_id_card(self):
        letters_id_card = "TRWAGMYFPDXBNJZSQVHLCKE"
        letters_foreigner = "XYZ"
        replace_foreigner_letter = {'X': '0', 'Y': '1', 'Z': '2'}
        regex = re.compile('[0-9]{8}[A-Z]')

        for user in self:
            temp_id_card = str(user.id_card)
            if user.id_card[0] in letters_foreigner:
                temp_id_card = temp_id_card.replace(user.id_card[0], replace_foreigner_letter[user.id_card[0]])

            if not regex.match(temp_id_card):
                raise ValidationError('Wrong ID Card, the format must be 00000000A.')
            if not letters_id_card[int(temp_id_card[:8]) % 23] == temp_id_card[8]:
                raise ValidationError('Wrong ID Card letter.')
