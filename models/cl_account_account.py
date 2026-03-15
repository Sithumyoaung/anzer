from odoo import _, api, fields, models


class CLAccount(models.Model):
    _inherit = 'account.account'

    anzer_account_code = fields.Many2many(
        'cl.account.integration', string="Mapping Account Codes", tracking=True)
    anzer_mapping_ids = fields.One2many(
        'cl.account.integration.line', 'account_id', string="Mapping Code Lines")
    anzer_analytic_account = fields.Many2one('account.analytic.account', string="Analytic Account")
