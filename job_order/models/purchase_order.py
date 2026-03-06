from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    state = fields.Selection(selection_add=[
        ('job', 'Job Order'),
    ], ondelete={'job': 'set default'})