from odoo import api, fields, models


class StudentPayslip(models.Model):
    _inherit = 'student.payslip'

    invoiced_count = fields.Integer(string='Sum of Invoiced', compute="_compute_invoiced_count")
    
    def _compute_invoiced_count(self):
        