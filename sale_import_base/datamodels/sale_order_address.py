#  Copyright (c) Akretion 2020
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from odoo.addons.datamodel import fields
from odoo.addons.datamodel.core import Datamodel


class SaleOrderAddressDatamodel(Datamodel):
    _name = "sale.order.address"

    name = fields.Str(required=True)
    street = fields.Str(required=True)
    street2 = fields.Str(allow_none=True)
    zip = fields.Str(required=True)
    city = fields.Str(required=True)
    email = fields.Email()
    state_code = fields.Str()
    country_code = fields.Str(required=True)
    phone = fields.Str()
    mobile = fields.Str()
