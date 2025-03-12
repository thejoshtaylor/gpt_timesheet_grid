from odoo import fields, models, _

class View(models.Model):
    _inherit = 'ir.ui.view'

    type = fields.Selection(selection_add=[('grid', "Grid")])

    def _get_view_info(self):
        _logger.info("Registering grid view in _get_view_info")
        return {
            'grid': {'icon': 'fa fa-th'}
        } | super()._get_view_info()
