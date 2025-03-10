#  Copyright (c) Akretion 2020
#  License AGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)
{
    "name": "Sale Import REST",
    "summary": "REST API for importig Sale Orders",
    "version": "14.0.1.0.1",
    "category": "Generic Modules/Sale",
    "author": "Akretion, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/sale-channel",
    "depends": [
        "sale_import_base",
        "auth_api_key",
        "base_rest",
        "base_rest_datamodel",
    ],
    "license": "AGPL-3",
    "data": ["views/sale_channel.xml"],
    "demo": ["demo/demo.xml"],
    "installable": False,
}
