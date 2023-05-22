from odoo import models, fields, api

class ProductInfo(models.Model):
    _name = 'product.info'
    _description = 'product_info'
    _rec_name = 'name'

    name = fields.Char(string='Product Name')
    description = fields.Char(string='Product Description')

class SalesInfo(models.Model):
    _name = 'sales.info'
    _description = 'sales_info'

    invoice_number = fields.Char(string='Invoice no.', required=True)
    invoice_date = fields.Date(string='Invoice Date', required=True, default=lambda self: fields.Date.today())
    customer = fields.Many2one('res.partner')
    source = fields.Char()
    product_id = fields.Many2one('product.info', required=True)
    quantity = fields.Float(string='Quantity', default=1)
    rate = fields.Float(String='Rate', default=0)
    total_amount = fields.Float(string='Total', compute="_get_total_amount", store=True)

    @api.onchange('quantity', 'rate')
    @api.depends('quantity', 'rate')
    def _get_total_amount(self):
        for rec in self:
            rec.total_amount = rec.quantity * rec.rate
