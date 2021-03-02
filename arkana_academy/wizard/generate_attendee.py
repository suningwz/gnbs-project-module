from odoo import api, fields, models


class SessionWizard(models.TransientModel):
    _name = 'session.wizard'
    _description = 'Popup untuk generate attendee'

    def _default_session(self):
        return self.env['arkana.session'].browse(self._context.get('active_id'))

    session_id = fields.Many2one(comodel_name='arkana.session', string='Sesi Kursus', 
        required=True, default=_default_session)
    student_ids = fields.Many2many(comodel_name='res.partner', string='Siswa', domain="[('is_student', '=', True)]")

    def gen_attendee(self):
        # debuging
        # import ipdb; ipdb.set_trace()
        # data_to_save = (0, 0, values)
        data_to_save = []
        if self.student_ids:
            data_to_save = [(0, 0, {'name': '1234', 'student_id': x.id,}) for x in self.student_ids]
        # create to attendee session
        if data_to_save:
            self.session_id.attendee_ids = data_to_save
        
        return {}