# -*- coding: utf-8 -*-
# © 2015 Eficent Business and IT Consulting Services S.L. -
# Jordi Ballester Alomar
# © 2015 Serpent Consulting Services Pvt. Ltd. - Sudhir Arya
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Operating Unit in Purchase Orders",
    "summary": "An operating unit (OU) is an organizational entity part of a\
        company",
    "version": "8.0.1.0.0",
    "author": "Eficent, Serpent Consulting Services Pvt. Ltd.,"
              "Odoo Community Association (OCA)",
    "website": "http://www.eficent.com",
    "category": "Purchase Management",
    "depends": ["purchase", "procurement_operating_unit"],
    "license": "AGPL-3",
    "data": [
        "security/purchase_security.xml",
        "views/purchase_order_view.xml",
        "views/purchase_order_line_view.xml",
    ],
    "demo": [
        "demo/purchase_order_demo.xml",
    ],
    "installable": True,
}
