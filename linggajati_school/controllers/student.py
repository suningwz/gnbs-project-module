from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class Hospital(http.Controller):

    @http.route('/student_webform', type="http", auth='public', website=True)
    def parent_webform(self, **kw):
        return http.request.render('linggajati_school.create_student', {})
        # return http.request.render('om_hospital.create_patient', {'patient_name' : 'Odoo Mates Test 123'})

    @http.route('/create/student', type='http', auth='public', website=True)
    def create_parent(self, **post):
        
        # Create Partner
        partner = request.env['res.partner'].create({
                'name': post.get('name'),
                'email': post.get('email'),
        })
        print('PARTNER')
        print("partner : ", partner)
        print("partner_id : ", partner['id'])

        # Create User
        admission_group = request.env['ir.model.data'].get_object('school', 'group_is_admission')
        emp_grp = request.env['ir.model.data'].get_object('base', 'group_user')
        group_list = [emp_grp.id, admission_group.id]
        user = request.env['res.users'].sudo().create({
            'name': partner['name'],
            'login' : partner['email'],
            'password' : '123',
            'email' : partner['email'],
            'partner_id' : partner['id'],
            'groups_id': [(6, 0, group_list)]
        })
        print('USER')
        print("user_id : ", user['partner_id'])

        # Create Student

        return request.render('linggajati_school.thanks_page', vals)
    