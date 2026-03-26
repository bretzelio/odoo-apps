from odoo import api, fields, models, _
from odoo.tools.misc import format_amount


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    cost_tax_string = fields.Char(
        compute='_compute_cost_tax_string',
    )

    @api.depends('supplier_taxes_id', 'standard_price')
    @api.depends_context('company')
    def _compute_cost_tax_string(self):
        for record in self:
            if not record.supplier_taxes_id:
                record.cost_tax_string = " "
                continue

            company = record.company_id or self.env.company
            currency = company.currency_id

            res = record.supplier_taxes_id._filter_taxes_by_company(
                company
            ).compute_all(
                record.standard_price,
                product=record,
                partner=self.env['res.partner'],
            )

            excluded = res['total_excluded']

            if currency.compare_amounts(excluded, record.standard_price):
                excl_string = _(
                    "%(amount)s Excl. Taxes",
                    amount=format_amount(self.env, excluded, currency),
                )
                record.cost_tax_string = f"(= {excl_string})"
            else:
                record.cost_tax_string = " "
