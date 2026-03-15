from odoo import _, api, fields, models


class CLAssetLine(models.Model):
    _name = 'cl.asset.line'
    _description = 'CL Asset Lines'

    asset_id = fields.Many2one(
        'account.asset', string="Asset")
    product_id = fields.Many2one(
        'product.template', string="Accessory Name")
    product_code_id = fields.Char(
        string="Reference Code", related='product_id.default_code')
    product_bar_code_id = fields.Char(
        string="Barcode", related='product_id.barcode')
    product_qty = fields.Integer(string="Qty")
    product_cost_id = fields.Float(
        string="Cost", related='product_id.standard_price')
