# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class Home(http.Controller):
    @http.route('/member/home/', auth='user', website=True )
    def home(self, **kw):
        values = {
            'content' : 'Hello Odoo'
        }
        return request.render('linggajati_membership.home', values)
        # return request.render('module.template', values)

# class BaseWebsite(http.Controller):
#     @http.route('/member/home', type='http', auth='user', website=True )
#     def home(self, **kw):
#         return "Hello, world"

