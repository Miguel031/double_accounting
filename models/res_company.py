from odoo import fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'

    fiscal_company_id = fields.Many2one(
        'res.company',
        string="Empresa Fiscal",
        help="Seleccione la empresa que actuará como contabilidad fiscal por defecto para la duplicación de asientos contables."
    )
    auto_double_accounting = fields.Boolean(
        string="Doble Contabilidad Automática",
        help="Si se activa, se duplicarán automáticamente todos los asientos generados (por compras, ventas, etc.) en la contabilidad fiscal."
    )
