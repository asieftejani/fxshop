# Copyright (c) 2026, Asief Tejani and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ExpensesandCosts(Document):
	def on_submit(self):
		journal = frappe.new_doc("Journal Entry")
		journal.voucher_type = "Journal Entry"
		journal.company = self.company
		journal.posting_date = self.transaction_date
		journal.multi_currency = 1

		journal.append(
			"accounts",
			{
				"account": self.expense_name,
				"exchange_rate": self.rate,
				"debit_in_account_currency": self.amount,
			},
		)
		journal.append(
			"accounts",
			{
				"account": self.paid_from,
				"exchange_rate": self.rate,
				"credit_in_account_currency": self.amount,
			},
		)

		try:
			journal.insert()
			journal.submit()

		except Exception:
			frappe.throw(frappe.get_traceback())
