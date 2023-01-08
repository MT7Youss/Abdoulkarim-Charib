# -*- coding: utf-8 -*-
{
    'name': "helb_project",
    'summary': """Project for HELB Student""",
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '15.0.0.1',
    'depends': ['base', 'sale_management', 'sale', 'calendar', 'hr' , 'res_groups'],
    #update data liste 
    'data': [["views/res_groups.xml","views/res_partner.xml","views/sale_order.xml"]
    ]
}
