# -*- coding: utf-8 -*-
{
    'name': 'GTS Anzer Odoo Integration',

    'summary': 'Integration module for synchronizing accounting, products, contacts, and assets with external systems.',

    'description': """
GTS Anzer Odoo Integration
==========================

This module is developed by Glow Together Solutions Co., Ltd (GTS) to integrate
Odoo with external systems such as Anzer or other third-party platforms.

Main Features
-------------
* Integration with external accounting systems
* Synchronization of:
    - Products
    - Customers / Contacts
    - Journals
    - Taxes
    - Accounts
    - Accounting Moves
    - Assets
* Custom integration configuration
* Integration line management
* Secure data exchange between systems

Benefits
--------
* Automates accounting data flow
* Reduces manual data entry
* Improves financial accuracy
* Enables scalable system integration

Technical Information
---------------------
Developed using Odoo framework best practices and designed for
extensibility and future integrations.

Company
-------
Glow Together Solutions Co., Ltd (GTS)
Website: https://gtsolutionsmyanmar.com
""",

    'author': 'Aung Min Soe',
    'company': 'Glow Together Solutions Co., Ltd',
    'maintainer': 'Glow Together Solutions Co., Ltd',
    'website': 'https://gtsolutionsmyanmar.com',

    'category': 'Accounting/Accounting',
    'version': '0.1',
    'license': 'LGPL-3',

    'depends': [
        'base',
        'account',
        'account_asset',
        'analytic',
    ],

    'data': [
        # Security
        'security/ir.model.access.csv',

        # Actions
        'views/action.xml',

        # Menus
        'views/menu.xml',

        # Search Views
        'views/search.xml',

        # Main Views
        'views/cl_asset.xml',
        'views/cl_product.xml',
        'views/cl_contact.xml',
        'views/cl_account_move.xml',
        'views/cl_account_account.xml',
        'views/cl_account_tax.xml',
        'views/cl_account_integration.xml',
        'views/cl_account_journal.xml',
        'views/cl_account_integration_line.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}