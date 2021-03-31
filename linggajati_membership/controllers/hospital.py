from odoo import http, _
from odoo.http import request


class Hospital(http.Controller):

    # Sample Controller Created
    @http.route('/hospital/doctor/', website=True, auth='user')
    def patient_page(self, **kw):
        # return "Hello World"
        student = request.env['student.student'].search([])
        # print("student---", student)
        return request.render('linggajati_membership.patient_page', {
            'student' : student
        })