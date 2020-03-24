# -*- coding: utf-8 -*-

from odoo import models, fields, api
import re
from odoo.exceptions import ValidationError


class Vehicle(models.Model):
    _name = 'garage.vehicle'
    _description = 'Registered vehicles'
    _order = 'brand asc, model desc'
    _sql_constraints = [
        ('unique_numberplate', 'unique(numberplate)', 'There are a car with that numberplate.')]

    name = fields.Char(string='Car', compute='_car_id', store=True)
    brand = fields.Selection(
        [('Abarth', 'Abarth'), ('Alfa Romeo', 'Alfa Romeo'), ('Aston Martin', 'Aston Martin'), ('Audi', 'Audi'),
         ('BMW', 'BMW'), ('Bugatti', 'Bugatti'), ('Citroën', 'Citroën'), ('CUPRA', 'CUPRA'), ('Dacia', 'Dacia'),
         ('DS', 'DS'), ('Ferrari', 'Ferrari'), ('Fiat', 'Fiat'), ('Ford', 'Ford'), ('Honda', 'Honda'),
         ('Hyundai', 'Hyundai'), ('Infiniti', 'Infinity'), ('Jaguar', 'Jaguar'), ('Jeep', 'Jeep'), ('KIA', 'KIA'),
         ('Koenisgsegg', 'Koenisgsegg'), ('Lamborghini', 'Lamborghini'), ('Land Rover', 'Land Rover'),
         ('Lexus', 'Lexus'), ('Lotus', 'Lotus'), ('Maserati', 'Maserati'), ('Mazda', 'Mazda'), ('McLaren', 'McLaren'),
         ('Mercedes-Benz', 'Mercedes-Benz'), ('MINI', 'MINI'), ('Mitsubishi', 'Mitsubishi'), ('Nissan', 'Nissan'),
         ('Opel', 'Opel'), ('Pagani', 'Pagani'), ('Peugot', 'Peugot'), ('Rolls-Royce', 'Rolls-Royce'), ('SEAT', 'SEAT'),
         ('Skoda', 'Skoda'), ('Smart', 'Smart'), ('Ssangyong', 'SsangYong'), ('Subaru', 'Subaru'), ('Suzuki', 'Suzuki'),
         ('Tesla', 'Tesla'), ('Toyota', 'Toyota'), ('Volkswagen', 'Volkswagen'), ('Volvo', 'Volvo')], string='Brand',
        required=True)
    model = fields.Char(size=20, string='Model', required=True)
    numberplate = fields.Char(size=7, string='Numberplate', required=True, help='0000AAA')
    registration_date = fields.Date(string='Registration date')
    picture = fields.Binary(string='Car picture')
    electric = fields.Boolean(string='Electric', default=False)

    repairs = fields.One2many('garage.repair', 'vehicle')

    @api.constrains('numberplate')
    def _constrain_registration(self):
        regex = re.compile('[0-9]{4}[A-Z]{3}')
        for vehicle in self:
            if not regex.match(vehicle.numberplate):
                raise ValidationError('Wrong numberplate, el formato tiene que ser 0000AAA')

    @api.constrains('registration_date')
    def _constrain_registration(self):
        for vehicle in self:
            if vehicle.registration_date > fields.Date.today():
                raise ValidationError(
                    'Invalid registration date.\nThe date cannot be higher than today: '
                    + fields.Date.today().strftime("%d/%m/%Y"))

    @api.depends('brand', 'model', 'numberplate')
    def _car_id(self):
        for car in self:
            car.name = ''
            if car.brand and car.model and car.numberplate:
                car.name = str(car.brand) + " - " + str(car.model) + ", " + str(car.numberplate)
