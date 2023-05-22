from odoo import api, fields, models


class SalesReport(models.TransientModel):
    _name = 'sales.report'
    _description = 'Sales Report'
    
    from_date = fields.Date(string='From Date', required=True, default=lambda self: fields.Date.today())
    to_date = fields.Date(string='To Date', required=True, default=lambda self: fields.Date.today())
    customer = fields.Many2one('res.partner', required=True)

    def sales_report_btn(self):
        return {
            'name': f'Sales Report: {self.customer.name} ({self.from_date} - {self.to_date})',
            'view_mode': 'tree',
            'res_model': 'sales.info',
            'type': 'ir.actions.act_window',    
            'target': 'main',
            'domain': [('customer', '=', self.customer.id), ('invoice_date', '>=', self.from_date), ('invoice_date', '<=', self.to_date)]
        }