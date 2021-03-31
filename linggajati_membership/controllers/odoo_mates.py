from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale



class AppintmentController(http.Controller):

    @route('/om_hospital', type='json', auth='user')
    def appointment_banner(self):
        return {
            'html' : <div>
                        <link>
                            <center><h1><font color="red">Hello World!</font></h1></center>
                            <center>
                                <p>
                                    <font color="blue">
                                        <a href="http://www.google.com">
                                            Go to Goole
                                        </a>
                                    </font>
                                </p>
                            </center>
                        </link>
                    </div>
                }


class WebsiteSaleInherit(WebsiteSale):

    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category", "[('website_id', 'in', (False, current_website_id))]"):category>''',
        '''/shop/category/<model("product.public.category", "[('website_id', 'in', (False, current_website_id))]"):category>/page/<int:page>'''
    ], type='http', auth="public", website=True)
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        res = super(WebsiteSaleInherit, self).shop(page=0, category=None, search='', ppg=False, **post)
        print("Inherited Odoo Mates ....", res)
        return res


class Hospital(http.Controller):

    @http.route('/patient_webform', type="http", auth='public', website=True)
    def patient_webform(self, **kw):
        return http.request.render('om_hospital.create_patient', {})
        # return http.request.render('om_hospital.create_patient', {'patient_name' : 'Odoo Mates Test 123'})

    @http.route('/create/webpatient', type='http', auth='public', website=True)
    def create_webpatient(self, **kw):
        # print("Date Receiverd.....", kw)
        # request.env['hospital.patient'].sudo().create(kw)
        # doctol_val = {
        #     'name' : kw.get('patient_name')
        # }
        # request.env['hospital.doctor'].sudo().create(doctol_val)
        return request.render('om_hospital.patient_thanks', {})
