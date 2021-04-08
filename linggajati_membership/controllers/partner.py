import odoo
 
from odoo import http, models, fields, _
from odoo.http import request
import json
import unicodedata
import base64


class PartnerForm(http.Controller):
    @http.route('/customer/form', type='http', auth='public', website=True)
    def partner_form(self, **kw):
        return request.render('linggajati_membership.tmp_customer_form', {})

    @http.route('/customer/form/submit', type='http', auth='public', website=True, csrf=False)
    def customer_form_submit(self, **post):
        # Post
        print("POST : ", post)
        photo = request.httprequest.files.getlist('photo')
        # photo = post.get('photo')
        print("photo :", photo)

        # Create Partner
        partner = request.env['res.partner'].create({
            'name': post.get('name'),
            'email': post.get('email'),
            'image' : base64.b64encode(photo[0].read())
        })
        print('Partner')
        print("partner : ", partner)
        print("name : ", partner['name'])
        print("id : ", partner['id'])
        print("user id : ", partner['user_id'])

        partner_id = partner['id']
        attachments = request.env['ir.attachment'].search([])
        print('attachments :', attachments)

        attachment_id = attachments.create({
            'name': photo[0].filename,
            'type': 'binary',
            'datas': base64.b64encode(photo[0].read()),
            'res_model': 'res.partner',
    	    'res_id': partner_id
        })
        print('attachment_id :', attachment_id)

        parent_grp_id = request.env['ir.model.data'].get_object('school', 'group_school_parent')
        emp_grp = request.env['ir.model.data'].get_object('base', 'group_user')
        parent_group_ids = [emp_grp.id, parent_grp_id.id]

        # Create user
        user = request.env['res.users'].create({
            'name': partner['name'],
            'login' : partner['email'],
            'email' : partner['email'],
            'partner_id' : partner['id'],
            'groups_id': [(6, 0, parent_group_ids)]
        })
        print('User')
        print("user : ", user)
        print("name : ", user['name'])
        print("id : ", user['id'])
        print("partner id : ", user['partner_id'])
        
        # Experiment Group
        parent_grp_id = request.env['ir.model.data'].get_object('school', 'group_school_parent')
        emp_grp = request.env['ir.model.data'].get_object('base', 'group_user')
        parent_group_ids = [emp_grp.id, parent_grp_id.id]

        print("parent_grp_id : ", parent_grp_id)
        print("emp_grp : ", emp_grp)
        print("parent_group_ids : ", parent_group_ids)

        return request.render('linggajati_membership.tmp_customer_form_success', {})
        # return request.render('linggajati_membership.tmp_customer_form_success', data)