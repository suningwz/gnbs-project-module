from odoo import api, fields, models


class Category(models.Model):
    _name = 'arkana.course.category'
    _description = 'Data kategori kursus'

    name = fields.Char(string='Nama kategori')
    description = fields.Text(string='Deskripsi')
    active = fields.Boolean(string='Active', default=True,)
    # ofo2m
    course_ids = fields.One2many(comodel_name='arkana.course', inverse_name='category_id', string='Data Kursus')
    