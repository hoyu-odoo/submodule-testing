from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    testing = fields.Float('Testing')
