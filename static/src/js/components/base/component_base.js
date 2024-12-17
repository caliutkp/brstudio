odoo.define('studio.ComponentBase', function (require) {
    "use strict";

    var Widget = require('web.Widget');

    var ComponentBase = Widget.extend({
        init: function (parent, options) {
            this._super.apply(this, arguments);
            this.options = options || {};
            this.componentId = _.uniqueId('component_');
        },

        destroy: function () {
            this._super.apply(this, arguments);
        },

        _triggerEvent: function (eventName, data) {
            this.trigger_up(eventName, Object.assign({
                componentId: this.componentId
            }, data));
        }
    });

    return ComponentBase;
});