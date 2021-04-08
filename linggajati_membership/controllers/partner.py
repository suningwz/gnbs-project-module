from odoo import http
from odoo.http import request
import base64


class PartnerForm(http.Controller):
    @http.route('/customer/form', type='http', auth='public', website=True)
    def partner_form(self, **kw):
        return request.render('linggajati_membership.tmp_customer_form', {})

    @http.route('/customer/form/submit', type='http', auth='public', website=True, csrf=False)
    def customer_form_submit(self, **post):
        # Message
        # data = {
        #     'message': 'Thank you !! We will prosess your Sale Order soon'
        # }

        # Post
        print("POST : ", post)
        # Cara 1
        photo = request.httprequest.files.getlist('photo')
        # photo = post.get('photo')
        print("photo :", photo)
        # print('filename :',photo.filename)
        # photo = base64.encodestring

        # Cara 2
        # img = open(post.get('photo'), 'rb').read()
        # photo = base64.b64encode(img)
        # print("photo : ", photo)

        # Cara 3
        # files = request.httprequest.files.getlist('photo') 
        # print("FILES : ", files)
        # filename = files.filename
        # print("filename : ", filename)

        # Cara 4
        # partner = request.env.user.partner_id
        # print('partner', partner)
        # Attachments = request.env['ir.attachment']
        # photo = post.get('photo').filename
        # files = post.get('photo')
        # attachment_id = Attachments.create({
        #     'name': photo,
        #     'type': 'binary',
        #     # 'datas': base64.b64encode(files.read()),
        #     'datas': photo.encode('base64'),
        #     'res_model': 'res.partner'',
        #     'res_id': partner['id']
        # })
        # print('attachment_id'. attachemnt_id)

        # Cara 5
        # photo = post.get('photo')
        # print("Photo : ", photo)
        # print('cek',photo.encode('base64'))
        # print('cek',base64.encode(photo))

        # Cara 6
        # photo = post.get('photo')
        # photo_bytes = photo.encode("ascii")
        # base64_bytes = base64.b64encode(photo_bytes)
        # base64_string = base64_bytes.decode("ascii")
        # print('base64_string :', base64_string)
        
        # post.update({
        #     'free_member': True,
        #     # 'photo': base64.encodestring(photo.read()) if photo else False
        # })
        # print("POST : ", post)



        # Create Partner
        partner = request.env['res.partner'].create({
            'name': post.get('name'),
            'email': post.get('email'),
            # 'images': base64_string,
        })
        print('Partner')
        print("partner : ", partner)
        print("name : ", partner['name'])
        print("id : ", partner['id'])
        print("user id : ", partner['user_id'])
        partner_id = partner['id']

        # print('partner', partner)
        # Attachments = request.env['ir.attachment'].search([{'res_name','=',partner['name']}])
        # Attachments = request.env['ir.attachment'].search([('res_id','=',partner_id)],limit=1)
        attachments = request.env['ir.attachment'].search([('res_id','=',partner_id),('name','=','image'),('res_field','=','image')])
        print('attachments :', attachments)
        # photo = post.get('photo').filename
        files = post.get('photo')
        files_bytes = files.encode("ascii")
        base64_bytes = base64.b64encode(files_bytes)
        base64_string = base64_bytes.decode("ascii")

        attachments.write({
            'datas': base64_string,
            'mimetype' : 'image/png',
            'index_content' : 'image'
        })

        # encode = base64.encodestring(files)
        # attachment_id = Attachments.write({
        #     'name': 'sembarang',
        #     'type': 'binary',
        #     # 'datas': base64.b64encode(files.read()),
        #     # 'datas': base64.b64encode(files),
        #     'datas': base64_string,
        #     # 'datas': photo.encode('base64'),
        #     # 'datas': files.encode('base64'),
        #     # 'datas': encode,
        #     'res_model': 'res.partner',
        #     'res_id': partner['id']
        # })
        # print('attachment_id', attachment_id)
        # error

        parent_grp_id = request.env['ir.model.data'].get_object('school', 'group_school_parent')
        emp_grp = request.env['ir.model.data'].get_object('base', 'group_user')
        parent_group_ids = [emp_grp.id, parent_grp_id.id]

        # Create user
        user = request.env['res.users'].create({
            'name': partner['name'],
            'login' : partner['email'],
            'email' : partner['email'],
            'partner_id' : partner['id'],
            'groups_id': [(6, 0, parent_group_ids)]
        })
        print('User')
        print("user : ", user)
        print("name : ", user['name'])
        print("id : ", user['id'])
        print("partner id : ", user['partner_id'])
        # print("groups_id : ", user['groups_id'])
        
        # Experiment Group
        # parent_grp_id = self.env.ref('school.group_school_parent')
        parent_grp_id = request.env['ir.model.data'].get_object('school', 'group_school_parent')
        emp_grp = request.env['ir.model.data'].get_object('base', 'group_user')
        parent_group_ids = [emp_grp.id, parent_grp_id.id]
        # emp_grp = self.env.ref('base.group_user')
        # group_id = request.env['ir.model.data'].get_object('event', 'group_event_user')
        # group_id.write({'users': [(4, users.id)]})
        # 'groups_id': [(6, 0, parent_group_ids)]
        print("parent_grp_id : ", parent_grp_id)
        print("emp_grp : ", emp_grp)
        print("parent_group_ids : ", parent_group_ids)

        # Show Values on Table
        # group = request.env['res.groups'].sudo().search([])
        # print('Group')
        # print("group : ", group)
        # print("group - name : ", request.env['res.groups'].browse('name'))
        # print("group - name : ", request.env['res.groups']['name'])
        # group_name = request.env['res.groups']['name']
        # print("group : ", group_name['Student Parent'])

        # Values
        # vals = {
        #     'partner' : partner,
        #     'user' : user
        # }
        # print('Values')
        # print("vals - partner : ", vals['partner'])
        # print("vals - partner id : ", vals['partner']['id'])
        # print("vals - user : ", vals['user'])

        return request.render('linggajati_membership.tmp_customer_form_success', {})
        # return request.render('linggajati_membership.tmp_customer_form_success', data)