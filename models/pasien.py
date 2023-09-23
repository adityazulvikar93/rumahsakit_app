from odoo import api, fields, models
from datetime import datetime, date

class PasienRumahSakit(models.Model):
    _name = "pasien.rumahsakit" #membuat tabel database pasien_rumahsakit di postgres
    _inherit = ["mail.activity.mixin", "mail.thread"] #messanger pada form, mengambil model dari modul Mail
    _description = "Pasien Rumah Sakit" #deskripsi tabel

    name = fields.Char(string='Nama : ', tracking=True) #tracking akan terlihat jika ada discuss pada form
    ref_id = fields.Char(string='ID Pasien : ', tracking=True)
    tgl_lahir = fields.Date(string='Tanggal Lahir : ', tracking=True)
    age = fields.Integer(string='Usia : ', tracking=True, compute='_hitung_usia')
    gender = fields.Selection([('pria', 'Pria'), ('wanita', 'Wanita')], string='Jenis Kelamin : ', tracking=True)
    active = fields.Boolean(string='Active', default=True, tracking=True)

    @api.depends('tgl_lahir')
    def _hitung_usia(self):
        for rec in self:
            hari_ini = date.today()
            if rec.tgl_lahir:
                rec.age = hari_ini.year - rec.tgl_lahir.year
            else:
                rec.age = 0