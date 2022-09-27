# Copyright 2020 Camptocamp SA (http://www.camptocamp.com)
# Copyright 2020 Akretion (http://www.akretion.com)
# Copyright 2020 BCIM
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Shopfloor",
    "summary": "manage warehouse operations with barcode scanners",
    "version": "13.0.5.1.0",
    "development_status": "Alpha",
    "category": "Inventory",
    "website": "https://github.com/OCA/wms",
    "author": "Camptocamp, BCIM, Akretion, Odoo Community Association (OCA)",
    "maintainers": ["guewen", "simahawk", "sebalix"],
    "license": "AGPL-3",
    "application": True,
    "depends": ["shopfloor_base", "stock", "base_rest", "auth_api_key", "stock_picking_batch"],
    "data": [
        "security/groups.xml",
        "views/shopfloor_menu.xml",
        "views/stock_picking_type.xml",
        "views/stock_location.xml",
    ],
}
