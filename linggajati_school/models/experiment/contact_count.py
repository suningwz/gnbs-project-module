from odoo import api, fields, models


class ModuleName(models.Model):
    _inherit = 'module.name'

    contracts_count = fields.Integer(compute='_compute_contracts_count', string='Contract Count')
    def _compute_contracts_count(self):
        # read_group as sudo, since contract count is displayed on form view
        contract_data = self.env['hr.contract'].sudo().read_group([('employee_id', 'in', self.ids)], ['employee_id'], ['employee_id'])
        result = dict((data['employee_id'][0], data['employee_id_count']) for data in contract_data)
        for employee in self:
            employee.contracts_count = result.get(employee.id, 0)

    contract_data = self.env['hr.contract'].
                    sudo().read_group(
                                [
                                    ('employee_id', 'in', self.ids)
                                ], 
                                [
                                    'employee_id'
                                ], 
                                [
                                    'employee_id'
                                ]
                            )
    
    result = dict(
                    (
                        data['employee_id'][0], 
                        data['employee_id_count']
                    ) 
                    for data in contract_data
                )