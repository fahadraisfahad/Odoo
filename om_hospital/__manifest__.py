# -*- coding: utf-8 -*-

{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': 'Hospital',
    'sequence': -100,
    'summary': 'Hospital Management System',
    'description': """Hospital Management System""",
    'depends': ['mail'],              
    # 'depends': ['mail'],     for chatter
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
    ],
    'demo':[],
    'application':'True',
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3'
}
