# -*- coding: utf-8 -*-

from odoo import models,fields,api
from datetime import datetime, timedelta,date

class PosOrder(models.Model):
	_inherit = 'pos.order'

	@api.model
	def get_user_group(self,user_id):
		print("--\n\n\n\n------user")
		user_id = self.env['res.users'].browse(user_id)
		print("\n\n\n-------user_id.user_has_groups('pos_restrict_del.group_pos_admin_line_remove')-->>>>>>>",user_id.user_has_groups('pos_restrict_del.group_pos_admin_line_remove'))
		if user_id and user_id.user_has_groups('pos_restrict_del.group_pos_admin_line_remove'):
			return True
		return False