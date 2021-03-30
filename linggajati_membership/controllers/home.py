# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.http import request

class Home(http.Controller):
    @http.route('/member/home/', auth='user', website=True )
    def home(self, **kw):
        
        product_ids = request.env['product.product'].search([('categ_id', 'ilike', 'all')])
        values = {
            'content' : 'Hello Odoo',
            'product_ids' : product_ids
        }
        return request.render('linggajati_membership.home', values)
        # return request.render('module.template', values)
