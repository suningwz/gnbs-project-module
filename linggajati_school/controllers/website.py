from odoo import http
from odoo.http import request
from odoo.addons.website.controllers.main import Website

class Website(Website):
    @http.route(website=True, auth="public")
    def web_login(self, redirect=None, *args, **kw):
        response = super(Website, self).web_login(redirect=redirect, *args, **kw)
        if not redirect and request.params['login_success']:
            if request.env['res.users'].browse(request.uid).has_group('base.group_user'):
                # redirect = b'/web?' + request.httprequest.query_string
                # print("Cek Web : Berhasil")
                redirect = '/'

            else:
                print("Cek Web : Else")
                redirect = '/my'
            return http.redirect_with_hash(redirect)
        return response