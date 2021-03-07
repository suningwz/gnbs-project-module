from odoo import api, fields, models


class Student(models.Model):
    _inherit = 'student.student'

    # Rename Label Field
    admission_date = fields.Date(string='Register Date')
    standard_id = fields.Many2one(string='Class')
    date_of_birth = fields.Date(string='Date of Birth')

    # Add State
    state = fields.Selection([('draft', 'Draft'),
                              ('done', 'Student'),
                              ('terminate', 'Terminate'),
                              ('cancel', 'Cancel'),
                              ('alumni', 'Graduate')],
                             'Status', readonly=True, default="draft")