# -*- coding: utf-8 -*-
from odoo import http

# class EduardoBarbosaTarrio(http.Controller):
#     @http.route('/eduardo_barbosa_tarrio/eduardo_barbosa_tarrio/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/eduardo_barbosa_tarrio/eduardo_barbosa_tarrio/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('eduardo_barbosa_tarrio.listing', {
#             'root': '/eduardo_barbosa_tarrio/eduardo_barbosa_tarrio',
#             'objects': http.request.env['eduardo_barbosa_tarrio.eduardo_barbosa_tarrio'].search([]),
#         })

#     @http.route('/eduardo_barbosa_tarrio/eduardo_barbosa_tarrio/objects/<model("eduardo_barbosa_tarrio.eduardo_barbosa_tarrio"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('eduardo_barbosa_tarrio.object', {
#             'object': obj
#         })
