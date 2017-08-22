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

class hotel_folio_line_inherit(models.Model):

	_name = 'hotel.folio.line'

	_inherit = 'hotel.folio.line'


	@api.constrains('checkin_date', 'checkout_date')
	def check_dates(self):
		'''
		This method is used to validate the checkin_date and checkout_date.
		-------------------------------------------------------------------
		@param self: object pointer
		@return: raise warning depending on the validation
		'''
		if self.checkin_date >= self.checkout_date:
				raise ValidationError(_('Room line Check In Date Should be \
				less than the Check Out Date!'))
		if self.folio_id.date_order and self.checkin_date:
			if self.checkin_date[0:10] < self.folio_id.date_order[0:10]:
				raise ValidationError(_('Room line check in date should be \
				greater than the current date.'))