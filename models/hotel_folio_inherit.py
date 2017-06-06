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

class hotel_folio_inherit(models.Model):

	_name = 'hotel.folio'

	_inherit = 'hotel.folio'


	''' 
		sobre escribimos el metodo name_get para agregar
		el numero de la habitacion, en la parte del folio
		para que no sea tan confuso al momento seleccionar
		cuando se necesita un folio.
	'''

	@api.multi
	def name_get(self):
		nombre = ''
		res = super(hotel_folio_inherit, self).name_get()
		for rec in self:
			numero_habitacion_id = self.env['hotel_reservation.line'].search([('line_id', '=', rec.reservation_id.id)])
			if numero_habitacion_id:
				for datos in self.env['hotel_reservation.line'].browse(numero_habitacion_id):
					nombre = 'Hab - '+datos.id.name+'-'+rec.name
					res.append((rec.id, nombre))
				
		return res