// Copyright (c) 2023, Hitesh Mahto and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airline", {
	refresh(frm) {        
        // frm.trigger('add_custom_link');
        frm.add_web_link(frm.doc.website, "Visit Website");
	},
    add_custom_link: function(frm) {
        if (!frm.doc.__islocal && frm.doc.website) {
            let sidebar = $('.layout-side-section').find('.form-sidebar');
            if (sidebar.length > 0 && sidebar.find('.custom-website-link').length == 0) {
                sidebar.prepend('<ul class="custom-website-link list-unstyled side-menu user-actions"><li class="user-action-row"><a href="' + frm.doc.website + '" target="_blank">Visit Website</a></li></ul>');
            }
        }
    }
});
