// Copyright (c) 2026, Asief Tejani and contributors
// For license information, please see license.txt

 frappe.ui.form.on("Exchange Transactions", {
 	currency(frm) {
        if (!frm.doc.currency) {
            frm.set_value("rate", 0);
            return;
        }
        frappe.call({
            method: "erpnext.setup.utils.get_exchange_rate",
            args: {
                from_currency: frm.doc.currency,
                to_currency: "IRR",
                transaction_date: frappe.datetime.get_today()
            },
            callback: function(r) {
                if (r.message) {
                    frm.set_value("rate", r.message);
                }
            }
        });
 	},

    number_of_notes(frm) {
        calculate_total(frm);
    },

    rate(frm) {
        calculate_total(frm);
    }
 });

 function calculate_total(frm) {
    const notes = flt(frm.doc.number_of_notes);
    const rate = flt(frm.doc.rate);

    frm.set_value("total", notes * rate);
 }