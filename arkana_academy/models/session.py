from odoo import api, fields, models, _
from odoo.exceptions import AccessError, UserError
# omod


class Session(models.Model):
    _name = 'arkana.session'
    _description = 'Sesi Kursus yang berjalan'
    _inherit = 'mail.thread'

    name = fields.Char(string='Nama Sesi', tracking=True,)
    course_id = fields.Many2one(comodel_name='arkana.course', string='Kursus',  tracking=True,)
    instructor_id = fields.Many2one(comodel_name='res.partner', string='Pengajar',  tracking=True,
                                    domain="[('is_instructor', '=', True)]")
    session_date = fields.Date(string='Tanggal', default=fields.Date.today,  tracking=True,)
    min_attendee = fields.Integer(string='Minimal', default=0, required=True,  tracking=True,)
    description = fields.Text(string='Deskripsi',  tracking=True,)
    attendee_ids = fields.One2many(comodel_name='arkana.session.attendee', 
                                   inverse_name='session_id', string='Data Peserta')
    state = fields.Selection(string='State', selection=[
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    ], default='draft', required=True, readonly=True,  tracking=True,)

    taken_seats = fields.Float(string='Jumlah Peserta Terdaftar', compute='_compute_taken_seats', store=True,  tracking=True,)
    email = fields.Char(string='Email Pengajar', related="instructor_id.email", store=True, )

    @api.onchange('min_attendee')
    def _onchange_min_attendee(self):
        # self.description = 'nilai baru'
        if self.min_attendee < 0:
            return {
                'warning': {
                    'title': "Tidak Valid!!!",
                    'message': "Minimal peserta tidak boleh minus.",
                },
            }
    
    

    @api.depends('min_attendee', 'attendee_ids')
    def _compute_taken_seats(self):
        for record in self:
            if not record.min_attendee:
                record.taken_seats = 0.0
            else:
                record.taken_seats = 100.0 * (len(record.attendee_ids) / record.min_attendee)
    

    def action_done(self):
        # validasi jika ada
        self.write({'state':'done'})
    
    def action_cancel(self):
        self.write({'state':'cancel'})

    def action_draft(self):
        self.write({'state':'draft'})
    
    def unlink(self):
        for record in self:
            if record.state != 'draft':
                raise UserError(_('Maaf data selain draft tidak boleh dihapus.'))
        return super(Session, self).unlink()


class SessionAttendee(models.Model):
    _name = 'arkana.session.attendee'
    _description = 'Peserta di sesi kursus'

    name = fields.Char(string='No Pendaftaran', required=True, default = 'New', readonly=True,)
    student_id = fields.Many2one(comodel_name='res.partner', string='Siswa',
                                 domain="[('is_student', '=', True)]", required=True,)
    description = fields.Text(string='Deskripsi')
    session_id = fields.Many2one(
        comodel_name='arkana.session', string='Sesi Kursus')

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):            
            vals['name'] = self.env['ir.sequence'].next_by_code('arkana.session.attendee') or _('New')

        result = super(SessionAttendee, self).create(vals)
        return result

