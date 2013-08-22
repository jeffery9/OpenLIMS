__author__ = 'DELL'

import time

from openerp.osv import fields, osv
import openerp.addons.decimal_precision as dp
from openerp.tools.translate import _
from openerp import netsvc


class sample(osv.osv):
    _name = 'sample.sampler'
    _description = 'Sample'
    # _inherit = ['mail.thread', 'ir.needaction_mixin']

    _columns = {
        'code': fields.char('code', size=64),
        'name': fields.char('Reference', size=64),
        'company_id': fields.many2one('res.company', 'Company', required=True, readonly=True,
                                      states={'draft': [('readonly', False)]}),
    }

    _defaults = {
        'state': lambda *a: 'draft',
        'company_id': lambda self, cr, uid, c: self.pool.get('res.company')._company_default_get(cr, uid,
                                                                                                 'sample.sample',
                                                                                                 context=c),
    }

    # _order = ''
sample()


class product(osv.osv):
    _inherit = 'product.product'
    _columns = {
        'is_sample': fields.boolean('Is Sample'),
    }

    # _order = ''
product()

