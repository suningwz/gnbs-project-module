# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class BaseWebsite(http.Controller):
    @http.route('/member/home/', auth='user', website=True )
    def home(self, **kw):
        values = {
            'content' : 'content'
        }
        return request.render('linggajati_membership.home', values)

# class BaseWebsite(http.Controller):
#     @http.route('/member/home', type='http', auth='user', website=True )
#     def home(self, **kw):
#         return "Hello, world"