# -*- coding: utf-8 -*-
{
    "name": "PynKart ZPL Studio Connector",
    "version": "1.0.0",
    "category": "Inventory",
    "summary": "Native Odoo connector for PynKart ZPL Studio — design labels visually, print unlimited with RFID, automations & 29 languages",
    "description": """
PynKart ZPL Studio Connector
=============================

Native Odoo connector for PynKart ZPL Studio desktop application.
Connect your Odoo instance to the most powerful ZPL label design
and printing platform built specifically for Odoo ERP.

What This Module Does
---------------------
• Exposes Odoo models and fields to PynKart ZPL Studio via secure API
• Generates and manages API tokens for authentication
• Supports all standard and custom Odoo models
• Navigates relational fields (many2one, one2many, many2many)
• Exports structured data for label printing (CSV / JSON)
• Works with Odoo Online, Odoo.sh, and On-Premise

Desktop App Capabilities (Licensed Separately)
-----------------------------------------------
• Visual drag-drop label designer with Monaco code editor
• 40+ ZPL elements including 1D/2D barcodes and RFID encoding
• Print automations with Odoo/API/Database triggers
• Async batch printing (10,000+ labels)
• 8 database connectors (MySQL, PostgreSQL, MongoDB, Redis, etc.)
• Multi-user roles (Admin, Editor, Operator, Viewer)
• IoT / CNC API for external device printing
• 29 UI languages with RTL support
• Dark mode, auto-save, template permissions

Supported Versions
------------------
Odoo 12.0 – 19.0

Desktop App Licensing (Recurring)
----------------------------------
• 14-Day Free Trial (all features, no credit card)
• From $12/14 days — $235/year
• Per-machine license, unlimited printing
• Purchase at pynkart.com/shop

Contact
-------
• Email: pynkart.com@gmail.com
• Website: pynkart.com/contactus

License
-------
Odoo Proprietary License (OPL-1)
""",

    "author": "PynKart",
    "website": "https://pynkart.com",
    "support": "https://pynkart.com/contactus",
    "license": "OPL-1",

    "price": 54.00,
    "currency": "USD",

    "depends": ["base", "product", "stock"],

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
        "static/description/banner.png",
        "static/description/icon.png",
        "static/description/screenshot_1.png",
        "static/description/screenshot_2.png",
        "static/description/screenshot_3.png",
    ],

    "live_test_url": "https://youtube.com/playlist?list=PL-lluQB0QKMe-DkSABzjmCZ7rxgdZHqLx",

    "sequence": 10,
}
