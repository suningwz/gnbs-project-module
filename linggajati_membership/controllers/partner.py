from odoo import http
from odoo.http import request


class PartnerForm(http.Controller):
    @http.route('/customer/form', type='http', auth='public', website=True)
    def partner_form(self, **kw):
        return request.render('linggajati_membership.tmp_customer_form', {})

    @http.route('/customer/form/submit', type='http', auth='public', website=True)
    def customer_form_submit(self, **post):
        partner =request.env['res.partner'].create({
            'name': post.get('name'),
            'email': post.get('email'),
        })
        vals = {
            'partner': partner,
        }
        return request.render('linggajati_membership.tmp_customer_form_success', vals)