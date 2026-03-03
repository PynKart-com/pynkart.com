# -*- coding: utf-8 -*-
{
    "name": "PynKart ZPL Studio Connector",
    "version": "1.0.0",
    "category": "Inventory",
    "summary": "Export product and stock data from Odoo to external ZPL label tools",
    "description": """
PynKart ZPL Studio Connector
===========================

This module provides a native Odoo interface to export product and inventory
data for ZPL label generation using external tools.

Key Features
------------
• Export products, barcodes, prices, and quantities
• Generate CSV / JSON files for label printing
• Secure API token generation
• Works with Odoo Online, Odoo.sh, and On-Premise
• No system access required
• Lightweight and safe

What This Module Does
---------------------
This addon extends Odoo by allowing users to:
• Select products or inventory records
• Export structured data for ZPL label printing
• Manage connection tokens for external tools

The actual label design and printing is handled by a companion desktop
application (optional).

Important
---------
• This module is fully functional on its own
• No external software is required to install the addon
• Compatible with Odoo Online

Supported Versions
------------------
Odoo 16.0 – 19.0

License
-------
Odoo Proprietary License (OPL-1)
""",

    "author": "PynKart",
    "website": "https://pynkart.com",
    "support": "https://pynkart.com/contactus",
    "license": "OPL-1",

    "price": 0.00,
    "currency": "USD",

    "depends": ["base", "product", "stock"],

    # REQUIRED: must actually do something
    "data": [
        "security/ir.model.access.csv",
        "views/pynkart_menu.xml",
        "views/export_wizard_view.xml",
        "views/settings_view.xml",
    ],

    "assets": {},

    "application": True,
    "installable": True,
    "auto_install": False,

    "images": [
        "static/description/banner.png",        # Cover image / thumbnail (REQUIRED for 5/5 score)
        "static/description/icon.png",          # Module icon (automatically used if present)
        "static/description/screenshot_1.png",  # Desktop app interface
        "static/description/screenshot_2.png",  # Odoo integration screen
        "static/description/screenshot_3.png",  # Batch printing or features
    ],

    "live_test_url": "https://www.youtube.com/watch?v=Udd58fuvzPc",

    "sequence": 10,
}
