# Copyright (c) 2023, Hitesh Mahto and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document


class AirplaneFlight(Document):
	#pass
	def before_submit(self):
		self.current_status = "Completed"
