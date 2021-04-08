# -*- coding: utf-8 -*-
import odoo
 
from odoo import http, models, fields, _
from odoo.http import request
import json
import unicodedata
import base64
 
class LatihanControllerTiga(http.Controller):
 
    @http.route('/upload', type='http', website=True)
    def render_upload_form(self, **kwargs):
 
        return request.render('linggajati_membership.upload_form')

    @http.route('/process/upload', type='http', website=True)
    def process_upload_form(self, **kwargs):
        data = {
            'message': 'Thank you !! We will prosess your Sale Order soon'
        }
    
        # mendapatkan sale order, berdasarkan input user dengan input name so_id 
        order = request.env['sale.order'].sudo().search([('name','=', kwargs['so_id'])], limit=1)
    
        # mendapatkan daftar file yang diupload oleh user dengan input name so_file
        files = request.httprequest.files.getlist('so_file')    
        print("files :", files)    
    
        # jika sale order tidak ada karena user memasukkan nomor dokumen yang salah tampilkan pesan
        if not order:
            data['message'] = 'Please input your valid Sale Order number !!!'
    
        # jika user tidak upload file tampilkan pesan
        if not files:
            data['message'] = 'Please upload your payment form'
    
        # jika sale order valid dan ada file, simpan file tersebut kedalam model attachment
        # jika res_model dan res_id di isi file yang baru diupload akan tampil di form yang sesuai
    
        if order and files:
            for ufile in files:
                filename = ufile.filename
                print('filename :',)
                if request.httprequest.user_agent.browser == 'safari':
                    filename = unicodedata.normalize('NFD', ufile.filename)
    

                error
                try:
                    attachment = request.env['ir.attachment'].sudo().create({
                        'name': filename,
                        'datas': base64.encodestring(ufile.read()),
                        'datas_fname': filename,
                        'res_model': 'sale.order',
                        'res_id': order.id
                    })
                except Exception:
                    data['message'] = 'Sorry something bad happen. Please try again !!!'
    
        return request.render('linggajati_membership.upload_message', data)