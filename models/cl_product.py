from odoo import _, api, fields, models


class CLProduct(models.Model):
    _inherit = 'product.template'

    asset_line_ids = fields.One2many(
        'cl.asset.line', 'product_id', string="Asset Information")
