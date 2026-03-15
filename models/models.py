# from odoo import models, fields, api


# class anzer_odoo_integration(models.Model):
#     _name = 'anzer_odoo_integration.anzer_odoo_integration'
#     _description = 'anzer_odoo_integration.anzer_odoo_integration'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

