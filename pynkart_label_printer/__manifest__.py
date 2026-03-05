# -*- coding: utf-8 -*-
{
    "name": "PynKart Label Printer",
    "version": "1.0.0",
    "category": "Productivity",
    "summary": "Windows desktop label printer for Odoo — design ZPL labels visually, connect via API key, print from any Odoo model. Installer included.",
    "description": """
PynKart Label Printer
=====================

Windows desktop application for ZPL label printing with Odoo.
The .exe installer is bundled inside this module.

IMPORTANT — This Is a Desktop Application
------------------------------------------
This is NOT a traditional Odoo server module. PynKart Label Printer
is a standalone Windows desktop application packaged as an Odoo module
so that it can be distributed through the Odoo App Store.

Installing this module does NOT modify your Odoo database, add menus,
or run any server-side code. It simply delivers the Windows installer
(.exe) to your system.

How It Works
------------
1. Install this module from the Odoo App Store
2. Locate and run PynKart-Setup-1.0.0.exe from the module folder
3. Enter your Odoo URL and API key in the desktop app
4. Browse any Odoo model, design labels, and print

The desktop app connects to Odoo Online, Odoo.sh, and On-Premise
deployments via XML-RPC / JSON-RPC using your API key. It reads
data from any standard or custom Odoo model for label printing.

What the Desktop App Does
--------------------------
- Visual drag-drop ZPL label designer with Monaco code editor
- 40+ ZPL elements: 1D/2D barcodes, text, shapes, images, RFID
- Browse all Odoo models and relational fields (many2one, one2many, many2many)
- Async batch printing (10,000+ labels)
- Print automations triggered by Odoo events, API calls, or schedules
- 8 data connectors: Odoo, REST API, Excel, CSV, MySQL, PostgreSQL, MongoDB, Redis
- Multi-user roles: Admin, Editor, Operator, Viewer
- 29 UI languages with RTL support and dark mode
- USB and network printer support, IoT / CNC API

Compatibility
-------------
- Odoo: 12, 13, 14, 15, 16, 17, 18, 19
- Platforms: Odoo Online, Odoo.sh, On-Premise
- Desktop: Windows 10 or later, 4 GB RAM, .NET 8.0 (included)

Desktop App Licensing
---------------------
- 14-Day Free Trial — all features, no credit card
- $149 / year per machine — everything included, no restrictions
- Unlimited printing — no per-label fees
- Purchase at pynkart.com/shop

100% Developer Support
-----------------------
Built and supported directly by the developer — no outsourced
helpdesks, no ticket queues. You talk to the person who wrote the
code. Questions answered within 24 hours.

- Email: pynkart.com@gmail.com
- Support & Enquiry: pynkart.com/contactus
- Video Tutorials: youtube.com/@pynkart

Pre-sales questions, integration help, custom label design —
just reach out. We're here to help you succeed.

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

    "depends": ["base"],

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
