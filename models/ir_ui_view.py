from odoo import models

class IrUIView(models.Model):
    _inherit = 'ir.ui.view'

    _type_selection = models.Model._type_selection + [('grid', 'Grid')]
