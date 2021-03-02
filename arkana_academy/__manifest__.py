# -*- coding: utf-8 -*-
{
    'name': "Arkana Academy",

    'summary': """
        Course Management""",

    'description': """
        Course Management
    """,

    'author': "Arkana,Aris",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/menu.xml',
        'views/category.xml',
        'views/course.xml',
        'views/partner.xml',
        'views/instructor.xml',
        'views/student.xml',
        'views/session.xml',
        'views/course_backup.xml',
        
        'wizard/generate_attendee.xml',

        'report/session.xml',

        'data/sequence.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
