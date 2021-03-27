from odoo import api, fields, models
from datetime import datetime, date
from dateutil.relativedelta import relativedelta


class StudentPayslip(models.Model):
    _inherit = 'student.payslip'

    date = fields.Date('Date', readonly=True,
                       help="Current Date of payslip",
                       default=lambda * a: date.today())
    
class StudentFeesStructure(models.Model):
    _inherit = 'student.fees.structure'

    # is_registration = fields.Boolean(string='For Registration', default=False)
    # is_generate = fields.Boolean(string='For Monthly', default=False)

    structure_for = fields.Selection([  ('registration', 'Registration'),
                                        ('monthly', 'Monthly')],
                                        'Structure For')

