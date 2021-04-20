    @http.route('/web/login', type='http', auth="none", sitemap=False)
    def web_login(self, redirect=None, **kw):
    # So copy that function to your custom module controller and do as following code.

    @http.route('/web/login', type='http', auth="none", sitemap=False)
    def web_login(self, redirect=None, **kw):
        ensure_db()
        request.params['login_success'] = False
        if request.httprequest.method == 'GET' and redirect and request.session.uid:
            return http.redirect_with_hash(redirect)

        if not request.uid:
            request.uid = odoo.SUPERUSER_ID

        values = request.params.copy()
        try:
        values['databases'] = http.db_list()
        except odoo.exceptions.AccessDenied:
        values['databases'] = None

        if request.httprequest.method == 'POST':
        old_uid = request.uid
        try:
        uid = request.session.authenticate(request.session.db, request.params['login'], request.params['password'])
        request.params['login_success'] = True

        # You can redirect to any view from here
        url = '/web#id={0}&view_type={1}&model={2}'.format(1, 'form', 'res.partner')
        return werkzeug.utils.redirect(url)

        # return http.redirect_with_hash(self._login_redirect(uid, redirect=redirect))
        except odoo.exceptions.AccessDenied as e:
        request.uid = old_uid
        if e.args == odoo.exceptions.AccessDenied().args:
        values['error'] = _("Wrong login/password")
        else:
        values['error'] = e.args[0]
        else:
        if 'error' in request.params and request.params.get('error') == 'access':
        values['error'] = _('Only employee can access this database. Please contact the administrator.')

        if 'login' not in values and request.session.get('auth_login'):
        values['login'] = request.session.get('auth_login')

        if not odoo.tools.config['list_db']:
        values['disable_database_manager'] = True

        # otherwise no real way to test debug mode in template as ?debug =>
        # values['debug'] = '' but that's also the fallback value when
        # missing variables in qweb
        if 'debug' in values:
        values['debug'] = True

        response = request.render('web.login', values)
        response.headers['X-Frame-Options'] = 'DENY'
        return response