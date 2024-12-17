odoo.define('studio.Editor', function (require) {
    "use strict";

    var Widget = require('web.Widget');
    var ViewBuilder = require('studio.ViewBuilder');
    var ToolbarWidget = require('studio.ToolbarWidget');
    var FieldWidget = require('studio.FieldWidget');

    var StudioEditor = Widget.extend({
        template: 'StudioEditor',
        custom_events: {
            'tool_field_add': '_onToolFieldAdd',
            'tool_group_add': '_onToolGroupAdd',
            'tool_notebook_add': '_onToolNotebookAdd',
            'tool_view_save': '_onToolViewSave',
            'tool_view_preview': '_onToolViewPreview',
            'component_added': '_onComponentAdded',
            'component_moved': '_onComponentMoved',
            'component_removed': '_onComponentRemoved'
        },

        init: function (parent, options) {
            this._super.apply(this, arguments);
            this.viewType = options.viewType;
            this.model = options.model;
            this.components = [];
        },

        start: function () {
            this._initSubComponents();
            return this._super.apply(this, arguments);
        },

        _initSubComponents: function () {
            this.toolbar = new ToolbarWidget(this, {
                tools: this._getAvailableTools()
            });
            this.viewBuilder = new ViewBuilder(this, {
                viewType: this.viewType
            });

            this.toolbar.appendTo(this.$('.studio-toolbar'));
            this.viewBuilder.appendTo(this.$('.studio-view-builder'));
        },

        _getAvailableTools: function () {
            return [
                { id: 'field', name: 'Field' },
                { id: 'group', name: 'Group' },
                { id: 'notebook', name: 'Notebook' }
            ];
        }
    });

    return StudioEditor;
});