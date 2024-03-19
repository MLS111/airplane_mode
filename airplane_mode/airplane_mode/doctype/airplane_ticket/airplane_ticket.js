// Copyright (c) 2023, Hitesh Mahto and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airplane Ticket', {
    refresh: function(frm) {
    
      frm.add_custom_button(__('Assign Seat'), function(){
        let newseat = new frappe.ui.Dialog({
            title: 'Select Seat',
            fields: [
                {
                    label: 'Seat Number',
                    fieldname: 'seat',
                    fieldtype: 'Data'
                }
            ],
            primary_action_label: 'Assign',
            primary_action(values) {
                cur_frm.set_value('seat',values.seat)
                newseat.hide();
            }
        });
        newseat.show();
    }, __("Actions"));
    
  }
});
