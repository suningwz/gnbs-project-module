from odoo import api, fields, models
# omodi

class Partner(models.Model):
    _inherit = 'res.partner'

    is_instructor = fields.Boolean(string='Pengajar', default=False,)
    is_student = fields.Boolean(string='Siswa', default=False,)