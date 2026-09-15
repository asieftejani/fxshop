# Copyright (c) 2026, Asief Tejani and contributors
# For license information, please see license.txt

# import frappe
from frappe import frappe
from frappe.model.document import Document


class ExchangeTransactions(Document):
	def validate(self):
		self.total = self.number_of_notes * self.rate
		if self.buy_or_sell == "Buy":
			self.doctype_link = "Supplier"
		else:
			self.doctype_link = "Customer"

	def on_submit(self):
		if self.buy_or_sell == "Buy":
			invoice = frappe.new_doc("Purchase Invoice")
			invoice.supplier = self.customer
			invoice.is_paid = True
			invoice.cash_bank_account = self.teller + " - SLLC"

		else:
			invoice = frappe.new_doc("Sales Invoice")
			invoice.customer = self.customer
			invoice.is_pos = True
			invoice.pos_profile = self.teller
			invoice.append(
				"payments",
				{
					"mode_of_payment": self.teller,
					"amount": self.total,
				},
			)

		invoice.company = self.company
		invoice.posting_date = self.transaction_date
		invoice.update_stock = True

		invoice.append(
			"items",
			{
				"item_code": self.currency,
				"qty": self.number_of_notes,
				"rate": self.rate,
				"warehouse": self.warehouse,
			},
		)

		try:
			invoice.insert()
			invoice.submit()

		except Exception:
			frappe.throw(frappe.get_traceback())
