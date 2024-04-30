// Copyright (c) 2024, Sejal Pachaghare and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride", {
	refresh(frm) {

	},
});

frappe.ui.form.on("Cost Breakup",{
    amount(frm,ctd,cdn){
       let total =0;
       frm.doc.cost_breakup.forEach(function(d){
        total+=parseInt(d.amount);
       }) 
       frm.set_value("total",total);
    }
})

