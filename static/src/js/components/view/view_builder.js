odoo.define('studio.ViewBuilder', function (require) {
    "use strict";

    var ComponentBase = require('studio.ComponentBase');
    var core = require('web.core');
    var QWeb = core.qweb;

    var ViewBuilder = ComponentBase.extend({
        template: 'StudioViewBuilder',
        custom_events: {
            'component_added': '_onComponentAdded',
            'component_moved': '_onComponentMoved',
            'component_removed': '_onComponentRemoved',
            'view_saved': '_onViewSaved'
        },

        init: function (parent, options) {
            this._super.apply(this, arguments);
            this.viewType = options.viewType;
            this.components = [];
            this.draggedComponent = null;
        },

        start: function () {
            this._initializeSortable();
            return this._super.apply(this, arguments);
        },

        _initializeSortable: function () {
            this.$('.components-container').sortable({
                items: '.studio-component',
                handle: '.component-handle',
                update: this._onSortUpdate.bind(this)
            });
        },

        _onComponentAdded: function (ev) {
            var component = ev.data.component;
            this.components.push(component);
            this._renderComponent(component);
        },

        _onComponentMoved: function (ev) {
            this._updateComponentPosition(ev.data.componentId, ev.data.newIndex);
        },

        _onComponentRemoved: function (ev) {
            this._removeComponent(ev.data.componentId);
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