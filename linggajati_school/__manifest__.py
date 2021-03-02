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
    'depends': ['base','school'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/student.xml',
        'views/menu.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}