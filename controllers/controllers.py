# -*- coding: utf-8 -*-
from odoo import http

# class MethodPorRestringeEliminarLinea(http.Controller):
#     @http.route('/method_por_restringe_eliminar_linea/method_por_restringe_eliminar_linea/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_por_restringe_eliminar_linea/method_por_restringe_eliminar_linea/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_por_restringe_eliminar_linea.listing', {
#             'root': '/method_por_restringe_eliminar_linea/method_por_restringe_eliminar_linea',
#             'objects': http.request.env['method_por_restringe_eliminar_linea.method_por_restringe_eliminar_linea'].search([]),
#         })

#     @http.route('/method_por_restringe_eliminar_linea/method_por_restringe_eliminar_linea/objects/<model("method_por_restringe_eliminar_linea.method_por_restringe_eliminar_linea"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_por_restringe_eliminar_linea.object', {
#             'object': obj
#         })