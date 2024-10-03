from odoo import models, fields, api

class PemesananRuangan(models.Model):
    _name = 'pemesanan.ruangan'
    _description = 'Pemesanan Ruangan'

    name = fields.Char(string='Nomor Pemesanan', required=True, copy=False, readonly=True, index=True, default=lambda self: ('New'))
    ruangan_id = fields.Many2one('master.ruangan', string='Ruangan', required=True)
    nama_pemesan = fields.Char(string='Nama Pemesan', required=True)
    tanggal_pemesan = fields.Date(string='Tanggal Pemesanan', required=True)
    status_pemesan = fields.Selection([
        ('draft', 'Draft'),
        ('on_going', 'On Going'),
        ('done', 'Done')],
        string='Status Pemesanan', default='draft'
    )
    catatan_pemesan = fields.Text(string='Catatan Pemesanan')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('pemesanan.ruangan') or 'New'
        return super(PemesananRuangan, self).create(vals)