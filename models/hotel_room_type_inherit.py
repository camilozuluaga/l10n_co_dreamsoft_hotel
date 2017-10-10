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


class HotelRoomType(models.Model):

	_name = "hotel.room.type"
	_inherit = "hotel.room.type"
	_description = "Room Type"


	@api.model
	def create(self, vals, check=True):
		"""
		sobreescribimos el metodo create para que los 
		usuarios no puedan sino crear un solo registro 
		para la configuracion de los horarios.
		
		@param self: The object pointer
		@param vals: dictionary of fields value.
		@return: new record set for hotel folio.
		"""
		guardo = super(HotelRoomType, self).create(vals) 
		
		if guardo:
			nombre_producto = ('Persona adicional {0}'.format(vals['name']))
			vals_producto = {'name' : nombre_producto, 'sale_ok' : True, 'purchase_ok' : False, 'type' : 'service',
								'isservice': True}
			self.env['product.product'].create(vals_producto)


		return guardo

