from odoo import _, api, fields, models


class CLAccountIntegration(models.Model):
    _name = 'cl.account.integration'
    _description = 'Cherry Land Account Code Integration'
    _rec_name = 'code'

    name = fields.Char(string="Operation Name")
    code = fields.Char(string="Code")
    anzer_account_ids = fields.One2many(
        'cl.account.integration.line', 'mapping_code_id', string="Account Code Lines")
