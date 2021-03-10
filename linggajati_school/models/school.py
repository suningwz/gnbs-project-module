from odoo import api, fields, models


class StudentPreviousSchool(models.Model):
    _inherit = 'student.previous.school'

    admission_date = fields.Date('Start Date')
    course_id = fields.Many2one(string='Class')

class StudentFamilyContact(models.Model):
    _inherit = 'student.family.contact'

    relation = fields.Many2one(string='Family Status')
    
from odoo import api, fields, models


class SchoolStandard(models.Model):
    _inherit = 'school.standard'

    name = fields.Char(string='Name')

    standard_id = fields.Many2one(string='Level')
    