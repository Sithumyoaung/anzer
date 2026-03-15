from odoo import _, api, fields, models


class CLContact(models.Model):
    _inherit = 'res.partner'

    business_partner_code = fields.Char(
        string="Business Partner Code", tracking=True)
    business_partner_type = fields.Selection(
        selection=[('d', 'D'), ('s', 'S'), ('ad', 'AD'), ('m', 'M'), ('n', 'N'), ('pg', 'PG'), ('prc', 'PRC'), ('rd', 'RD')], string="Business Partner Type", tracking=True)
    business_partner_group = fields.Selection(
        selection=[('doctor', 'Doctor'), ('supplier', 'Supplier'), ('attending_doctor', 'Attending Doctor'), ('medical_supplier', 'Medical Supplier'), ('non_medical_supplier', 'Non-Medical Supplier'), ('pathologist_doctor', 'Pathologist Doctor'), ('radiologist_doctor', 'Radiologist Doctor'), ('refer_doctor', 'Refer Doctor')], string="Business Partner Group", tracking=True)