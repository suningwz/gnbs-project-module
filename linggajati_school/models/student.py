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

    fees_receipt_ids = fields.One2many(comodel_name='student.payslip', inverse_name='student_id', string='Fees Receipt')
    
    # Bikin error Contacts require a name
    # name = fields.Char('Description')
    
    # number = fields.Char('Number', readonly=True,
    #                      default=lambda self: _('/'))
    # fees_receipt_ids one2many
    # llu isi di view dengn fee receipt ids ini, lalu upgrade, coba lihat muncul atau tidak, kalau tidak muncul berarti perlu ditambahkan field description dll di model ini