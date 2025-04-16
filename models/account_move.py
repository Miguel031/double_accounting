from odoo import api, fields, models, _
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = 'account.move'

    apply_double_accounting = fields.Boolean(
        string="Aplicar Doble Contabilidad",
        help="Marque para duplicar este asiento en la empresa fiscal."
    )
    fiscal_company_manual_id = fields.Many2one(
        'res.company',
        string="Empresa Fiscal Manual",
        help="Si se selecciona, el asiento se duplicará en esta empresa. De lo contrario, se usará la configurada en la compañía."
    )
    fiscal_origin_id = fields.Many2one(
        'account.move',
        string="Asiento Origen",
        readonly=True,
        help="Referencia al asiento original (para evitar duplicación recursiva)."
    )

    def action_post(self):
        res = super(AccountMove, self).action_post()
        for move in self:
            # Si el asiento ya es copia, no hacer duplicación para evitar bucles
            if move.fiscal_origin_id:
                continue

            # Determinar si se debe duplicar:
            # Se duplica si el usuario lo marca manualmente o si la compañía tiene la opción de duplicado automático activada
            if move.apply_double_accounting or move.company_id.auto_double_accounting:
                fiscal_company = move.fiscal_company_manual_id or move.company_id.fiscal_company_id
                if not fiscal_company:
                    raise UserError(_("No se ha configurado la empresa fiscal. Configure el campo 'Empresa Fiscal' en la compañía o seleccione una empresa en el asiento."))
                duplicate_vals = {
                    'company_id': fiscal_company.id,
                    'fiscal_origin_id': move.id,
                    'apply_double_accounting': False,  # Evitar duplicación en cadena
                    'fiscal_company_manual_id': False,
                }
                duplicate_move = move.with_company(fiscal_company).copy(duplicate_vals)
                duplicate_move.action_post()
        return res
