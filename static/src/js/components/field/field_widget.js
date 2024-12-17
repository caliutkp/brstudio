odoo.define('studio.FieldWidget', function (require) {
    "use strict";

    var ComponentBase = require('studio.ComponentBase');

    var FieldWidget = ComponentBase.extend({
        template: 'StudioFieldWidget',
        events: {
            'change .field-type': '_onTypeChange',
            'input .field-name': '_onNameChange',
            'change .field-required': '_onRequiredChange',
            'change .field-readonly': '_onReadonlyChange'
        },

        init: function (parent, options) {
            this._super.apply(this, arguments);
            this.fieldTypes = options.fieldTypes || [];
        },

        _onTypeChange: function (ev) {
            this._triggerEvent('field_type_changed', {
                type: $(ev.currentTarget).val()
            });
        },

        _onNameChange: function (ev) {
            this._triggerEvent('field_name_changed', {
                name: $(ev.currentTarget).val()
            });
        },

        _onRequiredChange: function (ev) {
            this._triggerEvent('field_required_changed', {
                required: $(ev.currentTarget).is(':checked')
            });
        },

        _onReadonlyChange: function (ev) {
            this._triggerEvent('field_readonly_changed', {
                readonly: $(ev.currentTarget).is(':checked')
            });
        }
    });

    return FieldWidget;
});