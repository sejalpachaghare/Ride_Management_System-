import frappe
def get_context(context):
    context.no_cache=1 
    context.vehicles=frappe.get_all("Vehicle",fields=["name","make","model","status","year"])
    return context 
