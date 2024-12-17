odoo.define('studio.components', function (require) {
    "use strict";

    return {
        Base: require('studio.ComponentBase'),
        Field: require('studio.FieldWidget'),
        View: require('studio.ViewBuilder'),
        Toolbar: require('studio.ToolbarWidget'),
    };
});