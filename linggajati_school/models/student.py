from odoo import api, fields, models
import time
# import ipdb

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

    country_id_custom = fields.Many2one(comodel_name='res.country', string='Country', default=_get_default_country)

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

         # Overriding Invoice
        inv_obj = self.env['student.payslip']
        self.ensure_one()
        invoice = inv_obj.create({
            'name': 'Invoice Biaya Pendaftaran',
            'journal_id': 1,
            # 'state': 'draft',
            'fees_structure_id': 3,
            'student_id': self.id
        })

        return invoice, record

    # Overriding Invoice
    # def _create_invoice(self):
    #     inv_obj = self.env['student.payslip']
    #     self.ensure_one()
    #     invoice = inv_obj.create({
    #         'name': 'Invoice Biaya Pendaftaran',
    #         'journal_id': 1,
    #         # 'state': 'draft',
    #         'fees_structure_id': 3,
    #         'student_id': self.id
    #     })

    #     return invoice

    # def create_invoice(self):
    #     self._create_invoice()