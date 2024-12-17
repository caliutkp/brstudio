odoo.define('studio.FieldWidget', function (require) {
    "use strict";

    var Widget = require('web.Widget');

    var StudioFieldWidget = Widget.extend({
        template: 'StudioField',
        events: {
            'change .field-type': '_onTypeChange',
            'input .field-name': '_onNameChange'
        },

        init: function (parent, options) {
            this._super.apply(this, arguments);
            this.options = options || {};
        },

        _onTypeChange: function (ev) {
            this.trigger_up('field_type_changed', {
                type: $(ev.currentTarget).val()
            });
        },

        _onNameChange: function (ev) {
            this.trigger_up('field_name_changed', {
                name: $(ev.currentTarget).val()
            });
        }
    });

    return StudioFieldWidget;
});