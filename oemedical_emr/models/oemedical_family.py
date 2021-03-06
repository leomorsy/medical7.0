# -*- coding: utf-8 -*-
#/#############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
#    Special Credit and Thanks to Thymbra Latinoamericana S.A.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#/#############################################################################

from openerp.osv import fields, orm
from openerp.tools.translate import _


class OeMedicalFamily(orm.Model):
    _name = 'oemedical.family'

    _columns = {
        'info': fields.text(string='Extra Information'),
        'operational_sector': fields.many2one('oemedical.operational_sector',
                                              string='Operational Sector', ),
        'name': fields.char(size=256, string='Family', required=True, 
                            help='Family code within an operational sector'),
        'members': fields.one2many('oemedical.family_member', 'family_id',
                                   string='Family Members', ),
    }
    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Family Code must be unique!'),
    ]


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
