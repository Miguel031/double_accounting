{
    'name': "Doble Contabilidad",
    'summary': "Duplica asientos en una empresa fiscal seleccionada (automático o manual)",
    'description': """
        Este módulo para Odoo 17 Community permite duplicar asientos contables en una empresa fiscal.
        Se puede definir la empresa fiscal por defecto en la configuración de la compañía o, de forma manual,
        en el documento contable.
    """,
    'author': "Ribentek",
    'website': "",
    'category': 'Accounting',
    'version': "17.0.1.0.1",
    'depends': ['base', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_company_view.xml',
        'views/account_move_view.xml',
    ],
    'installable': True,
    'application': False,
}
