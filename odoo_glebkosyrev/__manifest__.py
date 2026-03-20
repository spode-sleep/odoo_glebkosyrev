{
    'name': 'odoo_glebkosyrev',
    'version': '18.0.1.0.0',
    'summary': 'Extends Sale Order with new fields',
    'author': 'Gleb Kosyrev',
    'category': 'Sales',
    'depends': ['sale', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_view.xml',
        'report/sale_report.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}