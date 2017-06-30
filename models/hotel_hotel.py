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

''' 
	modelo donde se van a crear los metodos que se
	comparten entre los diferentes modelos con el 
	fin de evitar duplicar codigo.

'''

import pytz
import time
import datetime
from dateutil.relativedelta import relativedelta
import urllib2
from odoo.exceptions import except_orm, ValidationError
from odoo.tools import misc, DEFAULT_SERVER_DATE_FORMAT,DEFAULT_SERVER_DATETIME_FORMAT
from odoo import models, fields, api, _
from odoo import workflow
from decimal import Decimal
import logging
_logger = logging.getLogger(__name__)

class hotel_hotel(models.Model):


	_name = 'dreamsofft.hotel_config'


	name = fields.Char('Test')



	def fecha_UTC(self,fecha_usuario):

		if  self._context is None:
			self._context = {}

		#Obtener TimeZone Usuario
		tz = self._context.get('tz','America/Bogota')
		if not tz:
			tz = 'America/Bogota'

		fecha_sin_tz = datetime.datetime.strptime(fecha_usuario, DEFAULT_SERVER_DATETIME_FORMAT)
		tz_usuario = pytz.timezone(tz)
		fecha_tz = tz_usuario.localize(fecha_sin_tz)
		fecha_con_utc = fecha_tz.astimezone(pytz.utc)
		fecha_utc = fecha_con_utc.strftime(DEFAULT_SERVER_DATETIME_FORMAT)

		return fecha_utc 





	def calcular_edad(self,fecha_nacimiento):
		current_date = datetime.datetime.now()
		st_birth_date = datetime.datetime.strptime(fecha_nacimiento, DEFAULT_SERVER_DATE_FORMAT)
		re = current_date - st_birth_date
		dif_days = re.days
		age = dif_days
		age_unit = ''
		if age < 30:
			age_unit = '3'

		elif age > 30 and age < 365:
			age = age / 30
			age = int(age)
			age_unit = '2'

		elif age >= 365:
			age = int((current_date.year-st_birth_date.year-1) + (1 if (current_date.month, current_date.day) >= (st_birth_date.month, st_birth_date.day) else 0))
			age_unit = '1'
		
		retorno = {'edad': age, 'unidad_edad': age_unit}

		return retorno





