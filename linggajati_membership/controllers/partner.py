from odoo import http
from odoo.http import request


class PartnerForm(http.Controller):
    @http.route('/customer/form', type='http', auth='public', website=True)
    def partner_form(self, **kw):
        return request.render('linggajati_membership.tmp_customer_form', {})

    @http.route('/customer/form/submit', type='http', auth='public', website=True, csrf=False)
    def customer_form_submit(self, **post):

        # Create Partner
        partner_before = request.env['res.partner'].search([])
        print('Partner Before Create')
        print("partner : ", partner_before)
        partner = request.env['res.partner'].create({
            'name': post.get('name'),
            'email': post.get('email'),
        })
        print('Partner After Create')
        print("name : ", partner['name'])
        print("id : ", partner['id'])
        print("user id : ", partner['user_id'])
        print("partner : ", partner)

        # Create user
        user = request.env['res.users'].create({
            'name': partner['name'],
            'login' : partner['email'],
            'email' : partner['email'],
            'partner_id' : partner['id'],
        })
        print('User')
        print("name : ", user['name'])
        print("id : ", user['id'])
        # print("partner id : ", partner['partner_id'])
        print("user : ", user)

        # user = request.env['res.users'].sudo().search([])
        # print('User')
        # print("user : ", user)

        # Values
        vals = {
            'partner' : partner,
            'user' : user
        }
        print('Values')
        print("vals - partner : ", vals['partner'])
        print("vals - partner id : ", vals['partner']['id'])
        print("vals - user : ", vals['user'])

        return request.render('linggajati_membership.tmp_customer_form_success', vals)