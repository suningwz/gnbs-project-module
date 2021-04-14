from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale
import base64


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

        # Photo
        photo = request.httprequest.files.getlist('photo')
        photo = base64.b64encode(photo[0].read())

        # Create Partner
        partner = request.env['res.partner'].create({
                'name': post.get('name'),
                'email': post.get('email'),
                'image' : photo,
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
            # 'user_login' : partner['email'],
            'login' : partner['email'],
            'password' : '123',
            'new_passwd' : '123',
            'partner_id' : partner['id'],
            'groups_id': [(6, 0, group_list)]
        })
        print('USER')
        print("user_id : ", user['partner_id'])
        print("user_login : ", user['login'])
        # error
        # request.env['res.users'].sudo().write({
        #     'login' : partner['email'],
        #     'password' : '123',
        #     'new_passwd' : '123'
        # })


        # Create Student
        student = request.env['student.student'].create({
            'user_id' : user['id'],
            'login' : partner['email'],
            'name': partner['name'],
            'email' : partner['email'],
            'gender' : post.get('gender'),
            'date_of_birth' : post.get('date'),
            'contact_phone' : post.get('number'),
            'school_id' : post.get('school'),
            'photo' : photo,
        })
        print("STUDENT")
        print("Student : ", student)
        print("Student : ", student['id'])

        return request.render('linggajati_school.thanks_page', {})
    