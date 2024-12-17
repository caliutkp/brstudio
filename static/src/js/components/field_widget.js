odoo.define('studio.FieldWidget', function (require) {
    "use strict";

    var Widget = require('web.Widget');

    var StudioFieldWidget = Widget.extend({
        template: 'StudioFieldWidget',
        events: {
            'change .field-type': '_onTypeChange',
            'input .field-name': '_onNameChange'
        },

        init: function (parent, options) {
            this._super.apply(this, arguments);
            this.options = options || {};
        },

        _onTypeChange: function (ev) {
            this._updateFieldProperties($(ev.currentTarget).val());
        }
    });

    return StudioFieldWidget;
});