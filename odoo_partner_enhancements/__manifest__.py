{
    'name': 'Odoo Partner Enhancements',
    'version': '1.0',
    'summary': 'Displays current sales orders for each partner and enables customer creation and order retrieval via API.',
    'author': 'Jacob Craig',
    'website': '',
    'category': 'CRM',
    'depends': ['base', 'sale', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_inherit_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}