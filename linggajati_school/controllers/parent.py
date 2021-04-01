from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class Parent(http.Controller):

    @http.route('/parent_webform', type="http", auth='public', website=True)
    def parent_webform(self, **kw):
        return http.request.render('linggajati_school.create_parent', {})

    @http.route('/create/parent', type='http', auth='public', website=True)
    def create_parent(self, **post):
        print("Date Receiverd.....", post)
        # request.env['hospital.doctor'].sudo().create(doctol_val)
        # emp_grp = request.env['base.group_user']
        emp_grp = request.env['base'].search([])
        parent_grp_id = http.request.env['school.group_school_parent']
        parent_grp_id = request.env['school.group_school_parent'].sudo().search([])
        parent_group_ids = [emp_grp.id, parent_grp_id.id]

        school_parent = {'name': post.get('name'),
                        'login': post.get('email'),
                        'email': post.get('email'),
                        # 'partner_id': parent_id.partner_id.id,
                        'groups_id': [(6, 0, parent_group_ids)]
                        }

        request.env['res.users'].sudo().create(user_vals)
        return request.render('linggajati_school.thanks_page', {})

        # def create(self, vals):
        # parent_id = super(SchoolParent, self).create(vals)
        # parent_grp_id = self.env.ref('school.group_school_parent')
        # emp_grp = self.env.ref('base.group_user')
        # parent_group_ids = [emp_grp.id, parent_grp_id.id]
        # if vals.get('parent_create_mng'):
        #     return parent_id
        # user_vals = {'name': parent_id.name,
        #              'login': parent_id.email,
        #              'email': parent_id.email,
        #              'partner_id': parent_id.partner_id.id,
        #              'groups_id': [(6, 0, parent_group_ids)]
        #              }
        # self.env['res.users'].create(user_vals)
        # return parent_id

class PartnerForm(http.Controller):
    #mention class name
    @http.route(['/customer/form'], type='http', auth="public", website=True)
    #mention a url for redirection.
    #define the type of controller which in this case is ‘http’.
    #mention the authentication to be either public or user.
    def partner_form(self, **post):
    #create method
    #this will load the form webpage
        return request.render("create_partner_by_website.tmp_customer_form", {})
    @http.route(['/customer/form/submit'], type='http', auth="public", website=True)
    #next controller with url for submitting data from the form#
    def customer_form_submit(self, **post):
        partner = request.env['res.partner'].create({
            'name': post.get('name'),
            'email': post.get('email'),
            'phone': post.get('phone')
        })
        vals = {
            'partner': partner,
        }
        #inherited the model to pass the values to the model from the form#
        return request.render("create_partner_by_website.tmp_customer_form_success", vals)
        #finally send a request to render the thank you page#