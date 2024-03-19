# Copyright (c) 2023, Hitesh Mahto and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
	#pass
	def after_submit(self):
		self.current_status = "Completed"
