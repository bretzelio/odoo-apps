# -*- coding: utf-8 -*-
#
#  ┌────────────────────────────────────────────────────────────────────┐
#  │   Developed by: Bretzel.io                                        │
#  │   Website: https://www.bretzel.io/                                │
#  │   Support: support@bretzel.io                                     │
#  │   Description: Display cost excluding taxes on product form       │
#  └────────────────────────────────────────────────────────────────────┘
#
#  💰 See your real product costs at a glance, taxes excluded!
{
    "name": "Product Cost Without Tax Display",
    "version": "19.0.1.0.0",
    "summary": "Display cost excluding taxes on product form",
    "description": """
        Product Cost Without Tax Display
        ===================================
        This module enhances the product form by showing the cost price excluding taxes.

        Key Features
        ------------
        • Displays "(= X,XX € hors taxes)" next to the cost field on the product form
        • Mirrors the existing behavior for the sale price
        • Helps purchasing teams see the real cost at a glance

        Ideal for companies that need a clear view of product costs without tax included.
    """,
    "author": "Bretzel.io",
    "maintainer": "Bretzel.io",
    "company": "Bretzel.io",
    "support": "support@bretzel.io",
    "website": "https://www.bretzel.io/",
    "category": "Accounting",
    "license": "LGPL-3",
    "depends": [
        "account",
    ],
    "data": [
        "views/product_template_views.xml",
    ],
    "images": [
        "static/description/main_screenshot.png",
        "static/description/screenshot_en.png",
        "static/description/screenshot_fr.png",
    ],
    "assets": {},
    "installable": True,
    "application": False,
    "auto_install": False,
}
