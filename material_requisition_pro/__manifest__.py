# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name' : 'MaterialRequisition' ,
    'author': 'ProValues',
    'sequence': 18,
    'summary': 'Material Requisition module for managing material requests',
    'category': 'Inventory',
    'version': '17.0',
    'depends': ['hr', 'product'],
    'description': """
Material Requisition Management
===============================
This module facilitates the management of material requisitions within an organization, providing a streamlined process for requesting, approving, and tracking materials.

Features:
---------
- Submit material requisition requests with details like product, quantity, and department information.
- Approval workflow with multiple levels: requester, department manager, and procurement manager.
- Role-based access controls to ensure that only authorized users can view, approve, or reject requisitions""",
    'data': [
        'views/material_requisition_views.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'assets': {},
    'license': 'LGPL-3',

}