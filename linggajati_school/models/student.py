from odoo import api, fields, models


class Student(models.Model):
    _inherit = 'student.student'

    # Rename Label Field
    admission_date = fields.Date(string='Register Date')
    standard_id = fields.Many2one(string='Class')
    date_of_birth = fields.Date(string='Date of Birth')
    previous_school_ids = fields.One2many(string='School History Details')

    # Add State
    state = fields.Selection([('draft', 'Draft'),
                              ('done', 'Student'),
                              ('terminate', 'Terminate'),
                              ('cancel', 'Cancel'),
                              ('alumni', 'Graduate')],
                             'Status', readonly=True, default="draft")

    fees_receipt_ids = fields.One2many(comodel_name='student.payslip', inverse_name='student_id', string='Fees Receipt')
    invoice_count = fields.Integer(string=' ini invoices coy', compute="_compute_invoice_count")
    
    def _compute_invoice_count(self):
        for record in self:
            record.invoice_count = len(record.fees_receipt_ids)

        
    # @api.model
    # def _get_default_country(self):
    #     country = self.env['res.country'].search([('code', '=', 'ID')], limit=1)
    #     return country

    # country_id = fields.Many2one(default=_get_default_country)
    # country_id = fields.Text(default=_get_default_country)
    # country_id = fields.Many2many(default=_get_default_country)
    # country_id = fields.One2many(default=_get_default_country)

    # Bikin error Contacts require a name
    # name = fields.Char('Description')
    
    # number = fields.Char('Number', readonly=True,
    #                      default=lambda self: _('/'))
    # fees_receipt_ids one2many
    # llu isi di view dengn fee receipt ids ini, lalu upgrade, coba lihat muncul atau tidak, kalau tidak muncul berarti perlu ditambahkan field description dll di model ini

    # @api.multi
    # def _compute_taken_seats(self):
    #     for record in self:
    #         if not record.min_attendee:
    #             record.taken_seats = 0.0
    #         else:
    #             record.taken_seats = 100.0 * (len(record.attendee_ids) / record.min_attendee)

    # @api.multi
    # def _compute_count_invoiced(self):
    #  for invoiced in self:
    #      invoiced.associate_count = len(invoiced.associate_ids)