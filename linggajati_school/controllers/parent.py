from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class Parent(http.Controller):

    @http.route('/parent_webform', type="http", auth='public', website=True)
    def parent_webform(self, **kw):
        return http.request.render('linggajati_school.create_parent', {})

    # Partner in Function
    @http.route('/create/parent', type='http', auth='public', website=True, csrf=False)
    def create_parent(self, **post):

        def create_partner(post):
            # Create Partner
            partner = request.env['res.partner'].create({
                'name': post.get('name'),
                'email': post.get('email'),
            })

            return {
                'name' : partner['name'],
                'email' : partner['email'],
                'partner_id' : partner['id'],
                'partner' : partner
            }
        
        partner = create_partner(post)
        partner_id_last = request.env['res.partner']
        print("partner_id_last : ", partner_id_last)


        print('CREATE PARTNER')
        print("partner : ", partner)
        print("partner_id : ", partner['partner_id'])
        partner_id_user = partner['partner_id']
        partner_id_parent = partner['partner_id']
        print("partner_id_user : ", partner_id_user)
        print("partner_id_parent : ", partner_id_parent)

        # Create user
        # parent_grp_id = request.env['ir.model.data'].get_object('school', 'group_school_parent')
        # emp_grp = request.env['ir.model.data'].get_object('base', 'group_user')
        # parent_group_ids = [emp_grp.id, parent_grp_id.id]
        # user = request.env['res.users'].sudo().create({
        #     'name': partner['name'],
        #     'login' : partner['email'],
        #     'email' : partner['email'],
        #     'partner_id' : partner_id_user,
        #     'groups_id': [(6, 0, parent_group_ids)]
        # })

        # print('USER')
        # print("user_id : ", user['partner_id'])

        # Create Parent
        parent = request.env['school.parent'].create({
            'partner_id' : partner_id_parent,
        })

        print("PARENT")
        print("parent : ", parent)
        print("partner_id : ", parent['partner_id'])

        # Values
        vals = {
            'partner' : partner,
            # 'user' : user,
            'parent' : parent
        }

        return request.render('linggajati_school.thanks_page', vals)

    # @http.route('/create/parent', type='http', auth='public', website=True, csrf=False)
    # def create_parent(self, **post):

    #     # Create Partner
    #     partner = request.env['res.partner'].create({
    #         'name': post.get('name'),
    #         'email': post.get('email'),
    #     })

    #     print('PARTNER')
    #     print("partner_id : ", partner['id'])
    #     partner_id_user = partner['id']
    #     partner_id_parent = partner['id']
    #     # print("partner_id_user : ", partner_id_user.__dict__)
    #     # print("partner_id_parent : ", partner_id_parent.__dict__)
        
    #     # group = request.env['res.partner'].search(['id','=',partner['id'][0]])
    #     # print('group :', group)

    #     # Create Parent
    #     parent = request.env['school.parent'].create({
    #         # 'id' : 4,
    #         # 'partner_id' : user['partner_id']
    #         # 'partner_id' : partner_id,
    #         # 'partner_id' : partner['id'],
    #         'partner_id' : partner_id_parent,
    #     })

    #     print("PARENT")
    #     print("partner_id : ", parent['partner_id'])
    #     print("parent : ", parent)

    #     def create_user(partner):
    #         # # Create user
    #         parent_grp_id = request.env['ir.model.data'].get_object('school', 'group_school_parent')
    #         emp_grp = request.env['ir.model.data'].get_object('base', 'group_user')
    #         parent_group_ids = [emp_grp.id, parent_grp_id.id]
    #         user = request.env['res.users'].create({
    #             'name': partner['name'],
    #             'login' : partner['email'],
    #             'email' : partner['email'],
    #             'partner_id' : partner['id'],
    #             # 'partner_id' : parent['parent_id'],
    #             # 'partner_id' : partner_id_user,
    #             # 'partner_id' : partner,
    #             'groups_id': [(6, 0, parent_group_ids)]
    #         })

    #         print('USER')
    #         print("user_id : ", user['partner_id'])

    #         return user

    #     # Values
    #     vals = {
    #         'partner' : partner,
    #         'user' : create_user(partner),
    #         'parent' : parent
    #     }

    #     return request.render('linggajati_school.thanks_page', vals)