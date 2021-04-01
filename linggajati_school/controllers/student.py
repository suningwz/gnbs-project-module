from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class Hospital(http.Controller):

    @http.route('/student_webform', type="http", auth='public', website=True)
    def parent_webform(self, **kw):
        return http.request.render('linggajati_school.create_student', {})
        # return http.request.render('om_hospital.create_patient', {'patient_name' : 'Odoo Mates Test 123'})

    @http.route('/create/student', type='http', auth='public', website=True)
    def create_parent(self, **kw):
        print("Date Receiverd.....", kw)
        # user_vals = {'name': kw.get('name'),
        #              'login': kw.get('email'),
        #              'email': kw.get('email'),
        #             #  'partner_id': parent_id.partner_id.id,
        #             #  'groups_id': [(6, 0, parent_group_ids)]
        #              }

        request.env['student.student'].sudo().create(kw)
        return request.render('linggajati_school.thanks_page', {})

    
    
    # student_name = fields.Char('Student Name', related='user_id.name',
    #                            store=True, readonly=True)
    # gender = fields.Selection([('male', 'Male'), ('female', 'Female')],
    #                           'Gender', states={'done': [('readonly', True)]})
    # date_of_birth = fields.Date('BirthDate', required=True,
    #                             states={'done': [('readonly', True)]})
    