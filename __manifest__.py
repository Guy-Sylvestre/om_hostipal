# -*- coding: utf-8 -*-
{
    'name': "hospital_management",
    'summary': """Hospîtal Management Software""",
    'description': """Hospîtal Management Software""",
    'author': "Danho Guy Sylvestre KRAKOU",
    'website': "http://www.yourcompany.com",
    'category': 'Productivity',
    'version': '1.0',
    'licence': 'LGPL-3',
    'depends': ['sale',
                'website_slides',
                'mail',
                'hr'    
            ],
    'data': [
        'security/ir.model.access.csv',
        'views/patient.xml',
        'views/sale.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
