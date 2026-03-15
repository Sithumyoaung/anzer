from odoo import _, api, fields, models


class CLAccountTax(models.Model):
    _inherit = 'account.tax'

    anzer_tax_code = fields.Char(string="Anzer Tax Code", tracking=True)
