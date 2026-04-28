{
    "name": "Employee Sale Performance for Board",
    "summary": "Graphics of sales per employee and analytics",
    "version": "18.0.1.0.0",
    "category": "Board",
    "author": "Nelson",
    "license": "AGPL-3",
    "depends": ["base", "board", "hr", "sale", "crm", "spreadsheet_dashboard"],
    "data": [
        "security/ir.model.access.csv",
        "views/sale_performance_views.xml",
    ],
    "installable": True,
    "application": False,
}
