# -*- coding: utf-8 -*-
from odoo import http

class LinggajatiMembership(http.Controller):
    @http.route('/linggajati_membership/linggajati_membership/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/linggajati_membership/linggajati_membership/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('linggajati_membership.listing', {
            'root': '/linggajati_membership/linggajati_membership',
            'objects': http.request.env['linggajati_membership.linggajati_membership'].search([]),
        })

    @http.route('/linggajati_membership/linggajati_membership/objects/<model("linggajati_membership.linggajati_membership"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('linggajati_membership.object', {
            'object': obj
        })