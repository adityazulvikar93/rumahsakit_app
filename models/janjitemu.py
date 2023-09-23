from odoo import api, fields, models
from odoo.exceptions import ValidationError
# from datetime import date, datetime

class JanjiTemuRumahSakit(models.Model):
    _name = "janjitemu.rumahsakit" #membuat tabel database janjitemu_rumahsakit di postgres
    _inherit = ["mail.activity.mixin", "mail.thread"] #mengambil model dari modul Mail
    _description = "Janji Temu Rumah Sakit" #deskripsi tabel
    _rec_name = "pasien_id" #menjadikan field yang dipilih sebagai tampilan breadcrumb

    pasien_id = fields.Many2one(comodel_name='pasien.rumahsakit', string='Pasien : ', tracking=True)
    waktu_janji = fields.Datetime(string='Waktu Janji Temu : ', default=fields.Datetime.now, tracking=True)
    tanggal_booking = fields.Date(string='Tanggal Booking : ', default=fields.Date.today, tracking=True)
    gender = fields.Selection([('pria', 'Pria'), ('wanita', 'Wanita')], string='Jenis Kelamin : ', related='pasien_id.gender')
    ref_id = fields.Char(string='ID Pasien : ', tracking=True, help="ID Referensi dari data Pasien")
    resep = fields.Html(string='Resep')
    klinik = fields.Html(string='Klinik')
    prioritas = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Rendah'),
        ('2', 'Tinggi'),
        ('3', 'Sangat Tinggi')], string='Prioritas')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('sedang_konsul', 'Sedang Konsultasi'),
        ('rawatinap', 'Rawat Inap'),
        ('selesai', 'Selesai'),
        ('batal', 'Dibatalkan')], default='draft', string='Status', required=True)
    dokter_id = fields.Many2one(string='Dokter : ', comodel_name='res.users')

    @api.onchange('pasien_id')
    def onchange_pasien_id(self):
        for rec in self:
            rec.ref_id = rec.pasien_id.ref_id

    def action_test(self):
        # raise ValidationError("Object Button Test")
        return{
            'effect':{
                'fadeout':'slow',
                'message':'Button Action Test Success',
                'type':'rainbow_man',
            }
        }