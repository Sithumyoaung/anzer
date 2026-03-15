from odoo import _, api, fields, models


class CLAccountIntegrationLine(models.Model):
    _name = 'cl.account.integration.line'
    _description = 'CL Account Integration Line'
    _rec_name = 'mapping_code_id'

    account_id = fields.Many2one(
        'account.account', string="Account Code")
    mapping_code_id = fields.Many2one(
        'cl.account.integration', string="Mapping Code")
    account_name_id = fields.Char(
        string="Account Name", related='account_id.name')
    mapping_name_id = fields.Char(
        string="Mapping Name", related='mapping_code_id.name')
