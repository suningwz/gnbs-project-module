from odoo import http
from odoo.http import request


class PartnerForm(http.Controller):
    @http.route('/customer/form', type='http', auth='public', website=True)
    def partner_form(self, **kw):
        return request.render('linggajati_membership.tmp_customer_form', {})

    @http.route('/customer/form/submit', type='http', auth='public', website=True, csrf=False)
    def customer_form_submit(self, **post):

        # Create Partner
        partner = request.env['res.partner'].create({
            'name': post.get('name'),
            'email': post.get('email'),
        })
        print('Partner')
        print("partner : ", partner)
        print("name : ", partner['name'])
        print("id : ", partner['id'])
        print("user id : ", partner['user_id'])

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
        # print("groups_id : ", user['groups_id'])
        
        # Experiment Group
        # parent_grp_id = self.env.ref('school.group_school_parent')
        parent_grp_id = request.env['ir.model.data'].get_object('school', 'group_school_parent')
        emp_grp = request.env['ir.model.data'].get_object('base', 'group_user')
        parent_group_ids = [emp_grp.id, parent_grp_id.id]
        # emp_grp = self.env.ref('base.group_user')
        # group_id = request.env['ir.model.data'].get_object('event', 'group_event_user')
        # group_id.write({'users': [(4, users.id)]})
        # 'groups_id': [(6, 0, parent_group_ids)]
        print("parent_grp_id : ", parent_grp_id)
        print("emp_grp : ", emp_grp)
        print("parent_group_ids : ", parent_group_ids)

        # Show Values on Table
        # group = request.env['res.groups'].sudo().search([])
        # print('Group')
        # print("group : ", group)
        # print("group - name : ", request.env['res.groups'].browse('name'))
        # print("group - name : ", request.env['res.groups']['name'])
        # group_name = request.env['res.groups']['name']
        # print("group : ", group_name['Student Parent'])

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