from odoo import models

class IrUIView(models.Model):
    _inherit = 'ir.ui.view'

    @classmethod
    def _build_model(cls, registry):
        super()._build_model(registry)
        cls._patch_method('type_selection', lambda self: super(IrUIView, self).type_selection() + [('grid', 'Grid')])
