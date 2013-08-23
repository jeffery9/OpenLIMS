__author__ = 'DELL'

import time

from openerp.osv import fields, osv
import openerp.addons.decimal_precision as dp
from openerp.tools.translate import _
from openerp import netsvc


class sample_sample_property(osv.osv):
    _name = 'sample.sample.property'
    _description = 'sample property'

    _columns = {
        'key': fields.char('key', size=64),
        'value': fields.char('Value', size=64),
        'sample_id': fields.many2one('sample.sample', 'Sample',
                                       required=True),
    }

    # _defaults = {}


sample_sample_property()


class sample_sample_property_key(osv.osv):
    _name = 'sample.sample.property.key'
    _description = 'sample property key'

    _columns = {
        'key': fields.char('key', size=64),
        'template_id': fields.many2one('sample.sample.template', 'Template',
                                       required=True),
    }

    # _defaults = {}


sample_sample_property()


class sample_sample_template(osv.osv):
    _name = 'sample.sample.template'
    _description = 'sample template'

    _columns = {
        'name': fields.char('Template Name', size=64),
        'properties': fields.one2many('sample.sample.property.key',
                                      'template_id',
                                      'Properties',
                                      required=True),
        'samples': fields.one2many('sample.sample', 'template_id',
                                   'Samples',
                                   required=True),
        'company_id': fields.many2one('res.company', 'Company', required=True,
                                      readonly=True),

    }

    _defaults = {
        'company_id': lambda self, cr, uid, ctx: self.pool.get(
            'res.company')._company_default_get(cr, uid,
                                                'sample.sample',
                                                context=ctx),
    }


sample_sample_template()


class sample_sample(osv.osv):
    _name = 'sample.sample'
    _description = 'Sample'

    _columns = {
        'code': fields.char('Code', size=64),
        'template_id': fields.many2one('sample.sample.template', 'Template',
                                       required=True),
        'properties': fields.one2many('sample.sample.property',
                                      'sample_id',
                                      'Properties',
                                      required=True),
        'company_id': fields.many2one('res.company', 'Company', required=True,
                                      readonly=True,
        ),
    }

    _defaults = {
        'company_id': lambda self, cr, uid, ctx: self.pool.get(
            'res.company')._company_default_get(cr, uid,
                                                'sample.sample',
                                                context=ctx),
    }


sample_sample()


class product_product(osv.osv):
    _inherit = ['product.product']
    _name = 'product.product'
    _columns = {
        'is_sample': fields.boolean('Is Sample'),
    }

    # _order = ''


product_product()


