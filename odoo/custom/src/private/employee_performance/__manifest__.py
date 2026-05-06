# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Employee Performance",
    "version": "18.0.1.0.0",
    "category": "Human Resources",
    "summary": "Dashboard for employee performance metrics (Sales, CRM, Expenses)",
    "author": "Nelson Vera Cabrera",
    "website": "https://www.binhex.cloud",
    "license": "AGPL-3",
    "depends": [
        "board",
        "sale",
        "crm",
        "hr_expense",
        "spreadsheet_dashboard",
    ],
    "data": [
        "views/employee_performance_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
