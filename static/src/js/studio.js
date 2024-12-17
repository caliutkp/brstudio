odoo.define('studio.main', function (require) {
    "use strict";

    // Load all required components
    require('studio.Editor');
    require('studio.ViewBuilder');
    require('studio.FieldWidget');
    require('studio.ToolbarWidget');

    // Export main entry point
    return {
        Editor: require('studio.Editor'),
        ViewBuilder: require('studio.ViewBuilder'),
        FieldWidget: require('studio.FieldWidget'),
        ToolbarWidget: require('studio.ToolbarWidget'),
    };
});