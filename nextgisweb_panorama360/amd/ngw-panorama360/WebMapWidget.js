/* globals define */

//@nextgisweb_panorama360/Panorama360"
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
            this.component = reactApp.default(
                Panorama360Settings.default,
                { store: this.store },
                this.domNode
            );
        },
        destroy: function () {
            if (this.component) {
                this.component.unmount();
            }
            this.component = null;
        },

        serializeInMixin: function (data) {
            this._value = data.Panorama360;

            if (this.component){
                this.component.update();
            }
        },

        deserializeInMixin: function (data) {
            data.Panorama360 = this._value;
        }
    });
});
