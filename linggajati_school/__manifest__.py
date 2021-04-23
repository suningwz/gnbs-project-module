# -*- coding: utf-8 -*-
{
    'name': "GNBS",

    'summary': """
        Customizing School Module
    """,

    'description': """
        Module for customizing module school (Rename Menu)
    """,

    'author': "Abu Abdirohman",
    'website': "http://www.linggajati.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','school','school_fees','account', 'mail', 'website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',

        # Back-End
        'views/account.xml',
        'views/menu.xml',
        'views/school_fees_view.xml',
        'views/school_view.xml',
        'views/student_view.xml',
        
        # Front-End
        'views/frontend/form_student.xml',
        # 'views/frontend/menu.xml',
        # 'views/frontend/form_parent.xml',
        'views/frontend/style_css.xml',
        'views/frontend/template.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
