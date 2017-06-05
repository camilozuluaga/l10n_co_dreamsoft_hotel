# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012-Today Serpent Consulting Services PVT. LTD.
#    (<http://www.serpentcs.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
# ---------------------------------------------------------------------------

import time
import datetime
import urllib2
from odoo.exceptions import except_orm, ValidationError
from odoo.tools import misc, DEFAULT_SERVER_DATETIME_FORMAT
from odoo import models, fields, api, _
from odoo import workflow
from decimal import Decimal
import logging
_logger = logging.getLogger(__name__)

class hotel_room(models.Model):

	_name = 'hotel.room'
	_inherit = 'hotel.room'


	additional_people = fields.Boolean('Permitir Personas Adicionales')
	maximum_people= fields.Integer('Cantidad Personas Adicionales')
	value_person= fields.Integer('Valor por Persona')
	

	@api.constrains('capacity')
	def verificar_capacidad(self):

		if self.capacity<=0:
			raise except_orm(_('Warning'), _('La capacidad debe ser mayor a cero(0)'))




	"""
	@api.onchange('cname')
	def onchange_partner_id(self):
		'''
		When Customer name is changed respective adress will display
		in Adress field
		@param self: object pointer
		'''
		if not self.cname:
			self.partner_address_id = False
		else:
			addr = self.cname.address_get(['default'])
			self.partner_address_id = addr['default']

	"""


