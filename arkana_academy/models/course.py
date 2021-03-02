from odoo import api, fields, models


class Course(models.Model):
    _name = 'arkana.course'
    _description = 'Data Kursus'

    name = fields.Char(string='Nama Kursus')
    description = fields.Text(string='Deskripsi')
    active = fields.Boolean(string='Active', default=True,)
    category_id = fields.Many2one(comodel_name='arkana.course.category', string='Kategori')

    @api.model
    def create(self, vals):
        result = super(Course, self).create(vals)
        # do something
        if result:
            self.env['arkana.course.backup'].create(vals)
        return result

# testing only
class CourseBackup(models.Model):
    _name = 'arkana.course.backup'
    _description = 'Data Kursus Backup'

    name = fields.Char(string='Nama Kursus')
    description = fields.Text(string='Deskripsi')
    active = fields.Boolean(string='Active', default=True,)
    category_id = fields.Many2one(comodel_name='arkana.course.category', string='Kategori')