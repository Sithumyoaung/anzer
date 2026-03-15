from odoo import _, api, fields, models


class CLDepartment(models.Model):
    _name = 'cl.department'
    _description = 'Cherry Land Asset Department'

    name = fields.Char(string="Name")
    color = fields.Integer(string="Color")
