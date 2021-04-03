from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class Student(http.Controller):

    @http.route('/ppdb/registration', type="http", auth='public', website=True)
    def parent_webform(self, **kw):
        country = request.env['res.country'].search([])
        state = request.env['res.country.state'].search([('country_id','=',100)])
        school = request.env['school.school'].sudo().search([('com_name','ilike','SM')])
        # print('state :', state)
        return http.request.render('linggajati_school.registration', {
            'state' : state,
            'school' : school
        })

    @http.route('/ppdb/registration/create', type='http', auth='public', website=True, csrf=False)
    def create_student(self, **post):
        print('POST :', post)

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
        user = request.env['res.users'].create({
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
        student = request.env['student.student'].create({
            'user_id' : user['id'],
            'name': partner['name'],
            'email' : partner['email'],
            'gender' : post.get('gender'),
            'date_of_birth' : post.get('date'),
            'contact_phone' : post.get('number'),
            'school_id' : post.get('school'),
        })

        print("STUDENT")
        print("Student : ", student)
        print("Student : ", student['id'])

        return request.render('linggajati_school.thanks_page', {})
    