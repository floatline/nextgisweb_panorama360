/* globals define */

//@nextgisweb_panorama360/Panorama360"
define([
    "dojo/_base/declare",
    "dojo/_base/array",
    "dojo/dom-style",
    "dojo/data/ItemFileWriteStore",
    "dijit/_TemplatedMixin",
    "dijit/_WidgetsInTemplateMixin",
    "dijit/layout/ContentPane",
    "dijit/tree/TreeStoreModel",
    "dijit/Tree",
    "dijit/tree/dndSource",
    "@nextgisweb/pyramid/i18n!",
    "ngw-resource/serialize",
    "dojo/text!./template/WebMapWidget.hbs",
    // template
    "dijit/layout/BorderContainer",
    "dijit/layout/StackContainer",
    "dojox/layout/TableContainer",
    "dijit/Toolbar",
    "dijit/form/Button",
    "dijit/form/Form",
    "ngw-resource/ResourcePicker",
    "ngw-resource/form/ResourceLink",
    "ngw-pyramid/form/DisplayNameTextBox",
    "ngw-pyramid/form/ScaleTextBox",
    "@nextgisweb/gui/react-app",
    "@nextgisweb/Panorama360",
], function (
    declare,
    array,
    domStyle,
    ItemFileWriteStore,
    _TemplatedMixin,
    _WidgetsInTemplateMixin,
    ContentPane,
    TreeStoreModel,
    Tree,
    dndSource,
    i18n,
    serialize,
    template,
    reactApp,
    TableContainer,
    Panorama360
) {
    return declare([ContentPane, TableContainer, _TemplatedMixin, _WidgetsInTemplateMixin, serialize.Mixin], {
        title: i18n.gettext("Panorama360"),
        templateString: i18n.renderTemplate(template),

        constructor: function () {
            this.itemStore = new ItemFileWriteStore({data: {
                items: [{
                    item_type: "root"
                }]
            }});

           
        },

        buildRendering: function () {
            this.inherited(arguments);
            this.component = reactApp.default(
                Panorama360.default,
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
