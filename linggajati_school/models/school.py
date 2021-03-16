from odoo import api, fields, models


class StudentPreviousSchool(models.Model):
    _inherit = 'student.previous.school'

    # Rename
    admission_date = fields.Date('Start Date')
    course_id = fields.Many2one(string='Class')

class StudentFamilyContact(models.Model):
    _inherit = 'student.family.contact'

    # Rename
    relation = fields.Many2one(string='Family Status')

class SchoolStandard(models.Model):
    _inherit = 'school.standard'

    # Rename
    name = fields.Char(string='Name')
    standard_id = fields.Many2one(string='Level')

    # Modify
    medium_id = fields.Many2one(required=False)
    

class StandardStandard(models.Model):
    _inherit = 'standard.standard'

    # Modify
    code = fields.Char(required=False)

class StandardDivision(models.Model):
    _inherit = 'standard.division'

    # Modify
    code = fields.Char(required=False)
    