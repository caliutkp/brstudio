odoo.define('studio.ToolbarWidget', function (require) {
    "use strict";

    var ComponentBase = require('studio.ComponentBase');

    var ToolbarWidget = ComponentBase.extend({
        template: 'StudioToolbar',
        events: {
            'click .add-field': '_onAddField',
            'click .add-group': '_onAddGroup',
            'click .add-notebook': '_onAddNotebook',
            'click .save-view': '_onSaveView',
            'click .preview-view': '_onPreviewView'
        },

        init: function (parent, options) {
            this._super.apply(this, arguments);
            this.tools = options.tools || [];
        },

        _onAddField: function () {
            this._triggerEvent('tool_field_add');
        },

        _onAddGroup: function () {
            this._triggerEvent('tool_group_add');
        },

        _onAddNotebook: function () {
            this._triggerEvent('tool_notebook_add');
        },

        _onSaveView: function () {
            this._triggerEvent('tool_view_save');
        },

        _onPreviewView: function () {
            this._triggerEvent('tool_view_preview');
        }
    });

    return ToolbarWidget;
});