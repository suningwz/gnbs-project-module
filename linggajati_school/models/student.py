from odoo import api, fields, models


class Student(models.Model):
    _inherit = 'student.student'

    # Rename label field
    admission_date = fields.Date(string='Register Date')
    standard_id = fields.Many2one(string='Class')
    date_of_birth = fields.Date(string='Date of Birth')