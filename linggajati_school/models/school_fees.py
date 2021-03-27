from odoo import api, fields, models
from datetime import datetime, date
from dateutil.relativedelta import relativedelta


class StudentPayslip(models.Model):
    _inherit = 'student.payslip'

    date = fields.Date('Date', readonly=True,
                       help="Current Date of payslip",
                       default=lambda * a: date.today())
