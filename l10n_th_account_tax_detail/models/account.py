# -*- coding: utf-8 -*-
from openerp import fields, models, api


class AccountPeriod(models.Model):
    _inherit = 'account.period'

    taxdetail_sequence_ids = fields.One2many(
        'account.tax.detail.sequence',
        'period_id',
        string='Tax Detail Sequence',
    )


class AccountMove(models.Model):
    _inherit = 'account.move'

    tax_detail_ids = fields.One2many(
        'account.tax.detail',
        'ref_move_id',
        string='Tax Detail',
        readonly=False,
    )

    # Remove this part because it conflict with some some module installation
    # def init(self, cr):
    #     env = Environment(cr, SUPERUSER_ID, {})
    #     TaxDetail = env['account.tax.detail']
    #     tax_details = TaxDetail.search([('ref_move_id', '=', False)])
    #     for rec in tax_details:
    #         rec.ref_move_id = rec.invoice_tax_id.invoice_id.move_id or \
    #             rec.voucher_tax_id.voucher_id.move_id or \
    #             rec.move_line_id.move_id

    @api.multi
    def action_set_tax_sequence(self):
        for move in self:
            for tax in move.tax_detail_ids:
                date_doc = tax.invoice_date
                tax._set_next_sequence(date_doc)
