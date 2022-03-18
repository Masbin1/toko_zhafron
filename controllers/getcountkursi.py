import imp
from odoo import http, fields, models
from odoo.http import request
import json

class KursiTamuCount(http.Controller):
    @http.route('/kursitamu', auth='public', methods=['GET'])
    def getKursiTamu(self, **kwargs):
        kursi = request.env['toko.kursi_tamu'].search([])
        value = []
        for k in kursi:
            value.append({"nama" : k.name,
                         "tipe" : k.tipe,
                         "stok" : k.stok,
                         "harga" : k.harga})
        return json.dumps(value)
