from odoo import models, fields, api
from odoo.exceptions import ValidationError
import random
import string

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    responsible_employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Ответственный за выдачу товара',
        required=True,
    )

    new_field = fields.Char(
        string='New Field',
        compute='_compute_new_field',
        store=True,
        readonly=False,
    )

    @api.depends('order_line', 'order_line.price_subtotal', 'date_order')
    def _compute_new_field(self):
        for record in self:
            print(f"  record.id={record.id}, date={record.date_order}, new_field={record.new_field}")
            if not record.new_field:
                record.new_field = ''.join(random.choices(string.ascii_letters, k=10))
            elif record.date_order:
                date_str = record.date_order.strftime('%d/%m/%Y %H:%M:%S')
                record.new_field = f"{date_str} + {record.amount_total:.2f}"

    @api.constrains('new_field')
    def _check_new_field_length(self):
        for record in self:
            if record.new_field and len(record.new_field) > 30:
                raise ValidationError('Длина текста должна быть меньше 30 символов!')

    @api.onchange('new_field')
    def _onchange_new_field_length(self):
        if self.new_field and len(self.new_field) > 30:
            self.new_field = self.new_field[:30]
            return {
                'warning': {
                    'title': 'Ошибка',
                    'message': 'Длина текста должна быть меньше 30 символов!',
                }
            }