# -*- coding: utf-8 -*-
{
    'name': "EduardoBarbosaTarrio",

    'summary': """
        Módulo para la asignatura de SXE.""",

    'description': """
        El módulo servirá para la gestión de un taller en el que tendremos registrados clientes, vehículos etc
    """,

    'author': "Eduardo Barbosa Tarrío",
    'website': "https://github.com/Baaarbz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'account'],

    # always loaded
    'data': [
        'views/vehicle.xml',
        'views/repair.xml',
        'views/pieces.xml',
        'views/templates.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'license': 'AGPL-3',
    'installable': True,
    'application': True,
}
