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

class product_template_inherit(models.Model):

	_name = 'product.template'
	_inherit = 'product.template'


	@api.constrains('name')
	def validar_nombre_categorias(self):

		for datos in self.browse(self.ids):
			nombre=self.search( [('name', 'ilike', datos.name), ('id', '<>', datos.id)])
			_logger.info(nombre)
			if nombre:
				raise except_orm(_('Warning'), _('Esta habitacion ya existe'))

		return True