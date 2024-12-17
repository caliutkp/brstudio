odoo.define('studio.ViewBuilder', function (require) {
    "use strict";

    var Widget = require('web.Widget');
    var core = require('web.core');
    var QWeb = core.qweb;

    var ViewBuilder = Widget.extend({
        template: 'StudioViewBuilder',
        custom_events: {
            'component_added': '_onComponentAdded',
            'component_moved': '_onComponentMoved',
            'component_removed': '_onComponentRemoved'
        },

        init: function (parent, options) {
            this._super.apply(this, arguments);
            this.viewType = options.viewType;
            this.components = [];
            this.draggedComponent = null;
        },

        start: function () {
            this.$el.sortable({
                items: '.studio-component',
                handle: '.component-handle',
                update: this._onSortUpdate.bind(this)
            });
            return this._super.apply(this, arguments);
        },

        _onComponentAdded: function (ev) {
            var component = ev.data.component;
            this.components.push(component);
            this._renderComponent(component);
        },

        _onComponentMoved: function (ev) {
            var component = ev.data.component;
            var newIndex = ev.data.newIndex;
            this._updateComponentPosition(component, newIndex);
        },

        _renderComponent: function (component) {
            var $component = $(QWeb.render('StudioComponent', {
                component: component
            }));
            this.$('.components-container').append($component);
        }
    });

    return ViewBuilder;
});