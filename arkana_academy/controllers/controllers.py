# -*- coding: utf-8 -*-
# from odoo import http


# class ArkanaAcademy(http.Controller):
#     @http.route('/arkana_academy/arkana_academy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/arkana_academy/arkana_academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('arkana_academy.listing', {
#             'root': '/arkana_academy/arkana_academy',
#             'objects': http.request.env['arkana_academy.arkana_academy'].search([]),
#         })

#     @http.route('/arkana_academy/arkana_academy/objects/<model("arkana_academy.arkana_academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('arkana_academy.object', {
#             'object': obj
#         })
