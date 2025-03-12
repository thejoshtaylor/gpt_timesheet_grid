from odoo import models, fields

class HrTimesheet(models.Model):
    _inherit = 'account.analytic.line'

    project_id = fields.Many2one('project.project', string='Project')
    task_id = fields.Many2one('project.task', string='Task')
    date = fields.Date(string='Date')
    unit_amount = fields.Float(string='Hours Spent')
