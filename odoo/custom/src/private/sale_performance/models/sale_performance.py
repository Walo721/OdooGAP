from odoo import fields, models


class SalePerformanceReport(models.Model):
    _name = "sale.performance.report"
    _description = "Sale Performance Analysis"
    _auto = False
    _rec_name = "employee_id"

    employee_id = fields.Many2one("hr.employee", readonly=True)
    sale_count = fields.Integer(string="Number of Sales", readonly=True)
    total_amount = fields.Float(readonly=True)
    date = fields.Date(readonly=True)

    @property
    def _table_query(self):
        return """
            SELECT
                row_number() OVER () as id,
                he.id as employee_id,
                count(so.id) as sale_count,
                sum(so.amount_total) as total_amount,
                so.date_order::date as date
            FROM
                sale_order so
            JOIN
                hr_employee he ON he.user_id = so.user_id
            WHERE
                so.state in ('sale', 'done')
            GROUP BY
                he.id, so.date_order::date
        """


class CrmPerformanceReport(models.Model):
    _name = "crm.performance.report"
    _description = "CRM Performance Analysis"
    _auto = False
    _rec_name = "employee_id"

    employee_id = fields.Many2one("hr.employee", readonly=True)
    lead_count = fields.Integer(string="Number of Leads/Opps", readonly=True)
    expected_revenue = fields.Float(readonly=True)
    date = fields.Date(string="Create Date", readonly=True)

    @property
    def _table_query(self):
        return """
            SELECT
                row_number() OVER () as id,
                he.id as employee_id,
                count(cl.id) as lead_count,
                sum(cl.expected_revenue) as expected_revenue,
                cl.create_date::date as date
            FROM
                crm_lead cl
            JOIN
                hr_employee he ON he.user_id = cl.user_id
            GROUP BY
                he.id, cl.create_date::date
        """
