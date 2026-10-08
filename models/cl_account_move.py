from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

class CLAccountMove(models.Model):
    _inherit = 'account.move'

    anzer_id = fields.Char(string="Anzer ID", tracking=True, index=True)
    vendor_ref = fields.Text(string="AZ Reference", tracking=True)
    anzer_bill_type = fields.Selection(
        selection=[('doctor', 'Doctor'), ('supplier', 'Supplier')], string="Anzer Bill Type", tracking=True)

    def _normalize_anzer_id(self, value):
        if isinstance(value, str):
            value = value.strip()
        return value or False

    def _raise_if_anzer_id_taken(self, anzer_id, exclude_ids=None):
        if not anzer_id:
            return
        domain = [("anzer_id", "=", anzer_id)]
        if exclude_ids:
            domain.append(("id", "not in", exclude_ids))
        duplicate = self.search(domain, limit=1)
        if duplicate:
            raise ValidationError(
                _("Anzer ID must be unique. Already used on %s.")
                % duplicate.display_name
            )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if "anzer_id" in vals:
                vals["anzer_id"] = self._normalize_anzer_id(vals.get("anzer_id"))
            self._raise_if_anzer_id_taken(vals.get("anzer_id"))
        return super().create(vals_list)

    def write(self, vals):
        if "anzer_id" in vals:
            vals["anzer_id"] = self._normalize_anzer_id(vals.get("anzer_id"))
            self._raise_if_anzer_id_taken(vals.get("anzer_id"), exclude_ids=self.ids)
        return super().write(vals)