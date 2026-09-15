# Copyright (c) 2026, Asief Tejani and contributors
# For license information, please see license.txt

import frappe
from erpnext.accounts.utils import get_balance_on
from frappe.model.document import Document


class PartnerTransfer(Document):
	def validate(self):
		self.total = self.notes * self.rate
		self.credit_current_balance = get_balance_on(
			account=self.account_paid_from, date=self.transaction_date, company=self.company
		)
		self.credit_post_transaction_balance = self.credit_current_balance - self.notes
		self.debit_current_balance = get_balance_on(
			account=self.account_paid_to, date=self.transaction_date, company=self.company
		)
		self.debit_post_transaction_balance = self.debit_current_balance + self.notes

	def on_submit(self):
		journal = frappe.new_doc("Journal Entry")
		journal.voucher_type = "Journal Entry"
		journal.company = self.company
		journal.posting_date = self.transaction_date
		journal.multi_currency = 1

		journal.append(
			"accounts",
			{
				"account": self.account_paid_to,
				"exchange_rate": self.rate,
				"debit_in_account_currency": self.notes,
			},
		)
		journal.append(
			"accounts",
			{
				"account": self.account_paid_from,
				"exchange_rate": self.rate,
				"credit_in_account_currency": self.notes,
			},
		)

		try:
			journal.insert()
			journal.submit()

		except Exception:
			frappe.throw(frappe.get_traceback())
