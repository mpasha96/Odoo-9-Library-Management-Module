# -*- coding: utf-8 -*-
{
    'name': "library Management System",

    'summary': """
        Library Management""",

    'description': """
        Library Management Module :
            - Can add variety of books
            - Issue the books to student and teachers
            - Keep track of the books
    """,

    'author': "Mukarram Pasha",
    'website': "http://www.noweb.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views.xml',
        'templates.xml',
        'librarymanagement.xml',
        'partner.xml',
        'xpathexample.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}