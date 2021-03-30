from odoo import api, fields, models


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    is_school = fields.Boolean(string='For School', default=False)