from odoo import _, api, fields, models


class CLAccountJournal(models.Model):
    _inherit = 'account.journal'

    anzer_id = fields.Char(string="Anzer ID", tracking=True)
