from odoo import models, fields, api

class Timesheet(models.Model):
    _inherit = 'account.analytic.line'

    approval_state = fields.Selection([
        ('draft', 'Draft'),
        ('manager_approved', 'Manager Approved'),
        ('rejected', 'Rejected'),
    ], default='draft', string='Approval State')

    def action_manager_approve(self):
        self.write({'approval_state': 'manager_approved'})

    def action_reject(self):
        self.write({'approval_state': 'rejected'})
