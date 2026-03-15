from odoo import _, api, fields, models


class CLAccountMove(models.Model):
    _inherit = 'account.move'

    anzer_id = fields.Char(string="Anzer ID", tracking=True)
    vendor_ref = fields.Text(string="Reference", tracking=True)
    anzer_bill_type = fields.Selection(
        selection=[('doctor', 'Doctor'), ('supplier', 'Supplier')], string="Anzer Bill Type", tracking=True)
