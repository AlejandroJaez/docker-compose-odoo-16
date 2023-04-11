# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Real Estate',
    'version': '1.8',
    'category': 'Sales/Real Estate',
    'sequence': 16,
    'summary': 'Track places',
    'website': 'https://www.example.com',
    'author': "Alejandro Hernandez",
    'depends': [
        'base_setup',
        'sales_team',
        'mail',
        'calendar',
        'resource',
        'utm',
        'web_tour',
        'web_kanban_gauge',
        'contacts',
        'digest',
        'phone_validation',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}