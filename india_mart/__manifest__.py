# -*- coding: utf-8 -*-
{
    'name': "IndiaMart Lead Import",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Shellkube",
    'website': "http://www.yourcompany.com",
    "license": "AGPL-3",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'crm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/wizard_view.xml',
        'views/views.xml',
        'data/lead_fetch.xml',
        'wizard/wizard.xml',
        'wizard/display_message.xml'
    ],
    # 'qweb': ['data/chatter_rename.xml'],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
