from odoo import _, api, fields, models


class CLAsset(models.Model):
    _inherit = 'account.asset'

    asset_line_ids = fields.One2many(
        'cl.asset.line', 'asset_id', string="Asset Lines")
    department_info = fields.Many2many('cl.department', string="Department")
