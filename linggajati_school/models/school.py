from odoo import api, fields, models


class StudentPreviousSchool(models.Model):
    _inherit = 'student.previous.school'

    admission_date = fields.Date('Start Date')
    course_id = fields.Many2one(string='Class')
