from odoo import api, fields, models
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
import time

class Student(models.Model):
    _inherit = 'student.student'

    # Rename Label Field
    admission_date = fields.Date(string='Register Date')
    standard_id = fields.Many2one(string='Class')
    date_of_birth = fields.Date(string='Date of Birth')
    previous_school_ids = fields.One2many(string='School History Details')
    student_code = fields.Char('Student ID')

    # Change Field Name Format
    middle = fields.Char(required=False)
    last = fields.Char(required=False)

    # Add State
    state = fields.Selection([('draft', 'Draft'),
                              ('done', 'Student'),
                              ('terminate', 'Terminate'),
                              ('cancel', 'Cancel'),
                              ('alumni', 'Graduate')],
                             'Status', readonly=True, default="draft")

    fees_receipt_ids = fields.One2many(comodel_name='student.payslip', inverse_name='student_id', string='Fees Receipt')
    invoice_count = fields.Integer(compute="_compute_invoice_count")
    
    # Invoice Count
    def _compute_invoice_count(self):
        for record in self:
            record.invoice_count = len(record.fees_receipt_ids)
            
    # Auto Indonesia
    @api.model
    def _get_default_country(self):
        country = self.env['res.country'].search([('code', '=', 'ID')])
        return country

    country_id_custom = fields.Many2one(comodel_name='res.country', string='Country', default=_get_default_country, store=True)

    # Modify ID Student
    @api.multi
    def admission_done(self):
        record = super(Student, self).admission_done()
        '''Method to confirm admission'''
        school_standard_obj = self.env['school.standard']
        ir_sequence = self.env['ir.sequence']
        student_group = self.env.ref('school.group_school_student')
        emp_group = self.env.ref('base.group_user')
        for rec in self:
            if not rec.standard_id:
                raise ValidationError(_('''Please select class!'''))
            if rec.standard_id.remaining_seats <= 0:
                raise ValidationError(_('Seats of class %s are full'
                                        ) % rec.standard_id.standard_id.name)
            domain = [('school_id', '=', rec.school_id.id)]
            # Checks the standard if not defined raise error
            if not school_standard_obj.search(domain):
                raise except_orm(_('Warning'),
                                 _('''The standard is not defined in
                                     school'''))
            # Assign group to student
            rec.user_id.write({'groups_id': [(6, 0, [emp_group.id,
                                                     student_group.id])]})
            # Assign roll no to student
            number = 1
            for rec_std in rec.search(domain):
                rec_std.roll_no = number
                number += 1
            # Assign registration code to student
            reg_code = ir_sequence.next_by_code('student.registration')
            registation_code = (str(rec.school_id.state_id.name) + str('/') +
                                str(rec.school_id.city) + str('/') +
                                str(rec.school_id.name) + str('/') +
                                str(reg_code))
            stu_code = ir_sequence.next_by_code('student.code')
            student_code = (str('STD') + str(rec.year.code) +
                            str(rec.school_id.code) +
                            str(stu_code))
            rec.write({'state': 'done',
                       'admission_date': time.strftime('%Y-%m-%d'),
                       'student_code': student_code,
                       'reg_code': registation_code})

        # # Create Invoice
        self.create_invoice()

        return record

    # Method for create invoice on registration
    def create_invoice(self):
        name = "Invoice Biaya Pendaftaran"
        fees_structure_id = 3
        journal_id = 1
        self._create_invoice(name, fees_structure_id, journal_id, date.today())

    # Overriding Invoice
    @api.multi
    def _create_invoice(self, name, fees_structure_id, journal_id, date):
        std_payslip = self.env['student.payslip']
        self.ensure_one()
        # Define student.payslip
        payslip =   {
                        'student_id': self.id,
                        'name': name,
                        'fees_structure_id': fees_structure_id,
                        'journal_id': journal_id,
                        'date' : date,
                    }

        # Define student.payslip.line
        std_fees_structure = self.env['student.fees.structure'].search([('id', '=', fees_structure_id)])
        lines = []
        for data in std_fees_structure.line_ids or []:
            line_vals = {'slip_id': self.id,
                            'name': data.name,
                            'code': data.code,
                            'type': data.type,
                            'account_id': data.account_id.id,
                            'amount': data.amount,
                            'currency_id': data.currency_id.id or False,
                            'currency_symbol': data.currency_symbol or False}
            lines.append((0, 0, line_vals))
        payslip['line_ids'] = lines
        # Compute amount
        amount = 0
        for data in std_fees_structure.line_ids:
        # for data in std_payslip.line_ids:
            amount += data.amount
        std_payslip.register_id.write({'total_amount': std_payslip.total})
                
                # Fix state is confirm, for develop change to draft
        payslip_total = {'total': amount,
                        #  'state': 'confirm',
                         'due_amount': amount,
                         'currency_id': std_payslip.company_id.currency_id.id or False
                        }
        # Merge
        payslip.update(payslip_total)

        return std_payslip.create(payslip)

    # Method for generate invoice
    def generate_invoice(self):
        self._generate_invoice()

    @api.multi
    def _generate_invoice(self):

        # Define
        name = "Invoice Biaya Bulanan"
        fees_structure_id = 3
        journal_id = 1
        interval = 1

        # Loop for generate
        while interval <= 12:
            date_payslip = date.today()+relativedelta(months=interval, day=1)
            self._create_invoice(name, fees_structure_id, journal_id, date_payslip)
            interval += 1