# Copyright (c) 2023, Hitesh Mahto and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FlightPassenger(Document):
	#pass
	def before_save(self):
		self.fullname = self.first_name + " " + self.last_name
