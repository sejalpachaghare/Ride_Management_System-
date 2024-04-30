import frappe
from frappe.utils import today,add_days
from frappe import _
def send_insurance_remainder():
    three_day_ahead=add_days(today(),3)
    insurance_renewals=frappe.get_all("Vehicle",filters={"insurances_expiry": three_day_ahead},fields=["name","make"])

    for vehicle in insurance_renewals:
        frappe.sendmail(
            recipients=["sejalpachghare22@navgurukul.org"],
            subject=_("Insurance Renewal Remainder"),
            message=_("Insurance for {0} expires on {1}").format(vehicle.make,three_day_ahead)

        )

