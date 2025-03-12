// Example JS for handling some dynamic behavior
odoo.define('gpt_timesheet_grid.timesheet_script', function (require) {
    "use strict";
    var publicWidget = require('web.public.widget');
    var core = require('web.core');

    publicWidget.registry.MyWidget = publicWidget.Widget.extend({
        selector: '.o_timesheet_widget',
        events: {
            'click .approve_button': '_onApproveClick',
        },
        _onApproveClick: function (ev) {
            // Example logic for handling button clicks
            ev.preventDefault();
            alert('Approve Clicked!');
        },
    });
});
