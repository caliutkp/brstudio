odoo.define('studio.ViewEditor', function (require) {
    "use strict";

    var Widget = require('web.Widget');
    var core = require('web.core');

    var StudioViewEditor = Widget.extend({
        template: 'StudioViewEditor',
        events: {
            'dragstart .field-component': '_onDragStart',
            'drop .view-container': '_onDrop',
            'click .save-view': '_onSaveView'
        },

        init: function (parent, options) {
            this._super.apply(this, arguments);
            this.viewType = options.viewType;
            this.model = options.model;
        },

        _onDragStart: function (ev) {
            ev.originalEvent.dataTransfer.setData('fieldType', 
                $(ev.currentTarget).data('field-type'));
        },

        _onDrop: function (ev) {
            ev.preventDefault();
            var fieldType = ev.originalEvent.dataTransfer.getData('fieldType');
            this._createField(fieldType, ev.currentTarget);
        },

        _onSaveView: function () {
            this._saveViewConfiguration();
        }
    });

    return StudioViewEditor;
});