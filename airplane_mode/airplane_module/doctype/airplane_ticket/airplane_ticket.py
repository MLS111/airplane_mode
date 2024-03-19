# Copyright (c) 2023, Hitesh Mahto and contributors
# For license information, please see license.txt

import frappe,random
from frappe.model.document import Document


class AirplaneTicket(Document):
	#pass
	def before_save(self):
		counttotal=0;
		for items in self.add_ons:
			counttotal += items.amount
		self.total_amount = counttotal + self.flight_price	

		self.seat = str(random.randint(1,99)) + random.choice(['A','B','C','D','E'])

	def before_submit(self):
		if self.current_status != "Boarded":
			frappe.throw("Your data cannot be submitted as your current status is not boarded")


	def before_validate(self):
		add=[];
		for items in self.add_ons:
			if items.item not in add :
				add.append(items.item)
			else:
				self.add_ons.remove(items)
				continue	