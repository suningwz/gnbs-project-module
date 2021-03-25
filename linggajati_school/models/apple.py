class _service(models.Model):
    _name = 'se.service'
    _rec_name = "service_name"

    name = fields.Char(
        'Reference', copy=False, readonly=True, default=lambda x: _('New'))
    service_name = fields.Char("Service Name", required=True)
    service_department = fields.Many2one('hr.department', "Department Name", required=True, help="Department Name of employee")
    service_description = fields.Text("Description", required=True)
    service_remarks = fields.Text("Remarks")
    service_methodology = fields.Html(string="Methodology")
    service_id = fields.One2many('se.objective', 'service_id', string="Objectives", required=True)

    @api.model
    def create(self, valuees):
        if valuees.get('name', _('New')) == _('New'):
            valuees['name'] = self.env['ir.sequence'].next_by_code('se.service') or _('New')
        return super(_service, self).create(valuees)

    def _create_apple(self):
        inv_obj = self.env['se.apple']
        self.ensure_one()
        invoice = inv_obj.create({
            'apple_name': self.service_name,
            'apple_description': self.service_description,
            'apple_remarks': self.service_remarks
        })
        return invoice

    def create_apple(self):
        self._create_apple()

class _apple(models.Model):
    _name = 'se.apple'

    apple_name = fields.Char("Apple Name")
    apple_description = fields.Text("Remarks Apple")
    apple_remarks = fields.Text("Remarks Apple")

# def _create_apple(self):
#     inv_obj = self.env['se.apple']
#     self.ensure_one()
#     se = _service
#     invoice = inv_obj.create({
#         'apple_name': se.service_name,
#         'apple_description': se.service_description,
#         'apple_remarks': se.service_remarks
#     })
#     return invoice
