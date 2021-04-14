from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def get_all_data(self):
        result = []
        res_partner = self.env['res.partner'].search([])
        for data in res_partner:
            result.append(data.email)
        return(result)