# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class method_por_restringe_eliminar_linea(models.Model):
#     _name = 'method_por_restringe_eliminar_linea.method_por_restringe_eliminar_linea'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100