# from odoo import http


# class CherryLandDevelopment(http.Controller):
#     @http.route('/anzer_odoo_integration/anzer_odoo_integration', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/anzer_odoo_integration/anzer_odoo_integration/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('anzer_odoo_integration.listing', {
#             'root': '/anzer_odoo_integration/anzer_odoo_integration',
#             'objects': http.request.env['anzer_odoo_integration.anzer_odoo_integration'].search([]),
#         })

#     @http.route('/anzer_odoo_integration/anzer_odoo_integration/objects/<model("anzer_odoo_integration.anzer_odoo_integration"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('anzer_odoo_integration.object', {
#             'object': obj
#         })

