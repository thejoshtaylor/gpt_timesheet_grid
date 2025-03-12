from odoo import models, fields, api

class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    validated = fields.Boolean(string="Validated", default=False)

    def action_validate(self):
        for record in self:
            record.write({'validated': True})
