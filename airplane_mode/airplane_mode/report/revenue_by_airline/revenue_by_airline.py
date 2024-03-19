# Copyright (c) 2023, Hitesh Mahto and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	columns = [
		{
            'fieldname': 'airline',
            'label': 'Airline',
            'fieldtype': 'Link',
            'options': 'Airline'
        },
        {
            'fieldname': 'total_amount',
            'label': 'Revenue',
            'fieldtype': 'Currency',
            'fetch_from': 'total_amount'
        }
	]
	
	data =  get_data()
	
	total_revenue = get_total_revenue()
	
	summary = [{
		"label":"Total Revenue",
        "value": total_revenue,
        "indicator":"green",
		"datatype":"Currency"
    }
    ]

	chart = {
			"type":"donut",
			"data":
				{
					"labels":[d.airline for d in data],
					"datasets":[
                        {   "name":"Airline",
						    "values":[f.total_amount for f in data]
                        }
                    ]
                }
        }
    
	return columns, data, None, chart, summary

def get_data():
	data = frappe.db.sql("""select sum(total_amount) total_amount,x.name airline from `tabAirplane Ticket` t 
				  left join `tabAirplane Flight` f on f.name = t.flight 
				  left join `tabAirplane` a on a.name = f.airplane 
				  right join `tabAirline` x on x.name = a.airline  
				  group by x.name""",as_dict=1)
	return data

def get_total_revenue():
	revenue = frappe.db.sql("select sum(total_amount) total_amount from `tabAirplane Ticket`",as_dict=1)
	return revenue[0].total_amount