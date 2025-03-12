from odoo import models

class IrUIView(models.Model):
    _inherit = 'ir.ui.view'

    @classmethod
    def _build_model(cls, registry):
        super()._build_model(registry)
        if not hasattr(cls, '_type_selection'):
            cls._type_selection = []
        cls._type_selection.append(('grid', 'Grid'))
