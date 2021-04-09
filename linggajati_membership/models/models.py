from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def get_all_data(self):
        # result = {}
        result = []
        res_partner = self.env['res.partner'].search([])
        # print('rest partner :', res_partner)
        # print('email :', res_partner['id'])
        
        # Dictionary
        # i = -1
        # for data in res_partner:
        #     i += 1
        #     result['email'].appenddata.email
        #     result['id'] = data.id
        #     print('result ',i,' : ',result['email'])
        #     print('result ',i,' : ',result['id'])

        # print(result)
        # i = -1
        for data in res_partner:
            # i += 1
            result.append(data.email)
            # print('email ',i,' : ',result[i])

        # print('result :',result)

        return(result)