# -*- coding: utf-8 -*-
from odoo import http

# class LinggajatiShcool(http.Controller):
#     @http.route('/linggajati_shcool/linggajati_shcool/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/linggajati_shcool/linggajati_shcool/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('linggajati_shcool.listing', {
#             'root': '/linggajati_shcool/linggajati_shcool',
#             'objects': http.request.env['linggajati_shcool.linggajati_shcool'].search([]),
#         })

#     @http.route('/linggajati_shcool/linggajati_shcool/objects/<model("linggajati_shcool.linggajati_shcool"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('linggajati_shcool.object', {
#             'object': obj
#         })