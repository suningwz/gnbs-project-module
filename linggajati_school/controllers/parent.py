from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class Hospital(http.Controller):

    @http.route('/parent_webform', type="http", auth='public', website=True)
    def parent_webform(self, **kw):
        return http.request.render('linggajati_school.create_parent', {})
        # return http.request.render('om_hospital.create_patient', {'patient_name' : 'Odoo Mates Test 123'})

    @http.route('/create/parent', type='http', auth='public', website=True)
    def create_parent(self, **kw):
        print("Date Receiverd.....", kw)
        # doctol_val = {
        #     'name' : kw.get('patient_name')
        # }
        # request.env['hospital.doctor'].sudo().create(doctol_val)
        request.env['school.parent'].sudo().create(kw)
        return request.render('linggajati_school.thanks_page', {})