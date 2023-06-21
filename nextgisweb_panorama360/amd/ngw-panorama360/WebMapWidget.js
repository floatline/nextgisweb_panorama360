/* globals define */

define([
    "dojo/_base/declare", 
    "dijit/layout/ContentPane",
    "dojox/layout/TableContainer",
    "@nextgisweb/pyramid/i18n!",
    "ngw-resource/serialize",
    "@nextgisweb/gui/react-app",
    "@nextgisweb/panorama360/panorama360-settings",
], function (
    declare,
    ContentPane,
    TableContainer,
    i18n,
    serialize,
    reactApp,
    Panorama360Settings
) {
    return declare([ContentPane, TableContainer, serialize.Mixin], {
        title: i18n.gettext("Panorama360"),

        constructor: function () {
        },

        buildRendering: function () {
            this.inherited(arguments);
            var widget = this;
            this.component = reactApp.default(
                Panorama360Settings.default,
                { onChange: function(values) {
                    widget._value = values
                }  },
                this.domNode
            );
        },
        destroy: function () {
            if (this.component) {
                this.component.unmount();
            }
            this.component = null;
        },

        deserializeInMixin: function (data) {
            this._value = data.panorama360_settings;

            if (this.component){
                this.component.update({ values: this._value }) ;

            }
        },

        serializeInMixin: function (data) {
            // Something should be done in here
            data.panorama360_settings = this._value;
        }
    });
});
