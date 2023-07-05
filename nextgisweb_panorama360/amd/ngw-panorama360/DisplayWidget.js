define([
    "dojo/_base/declare",
    "dojo/_base/array",
    "dojo/dom-class",
    "dojo/on",
    "dojo/request",
    "put-selector/put",
    "@nextgisweb/pyramid/i18n!",
    "@nextgisweb/pyramid/api",
    "ngw-feature-layer/DisplayWidget",
    "@nextgisweb/gui/react-app",
    "@nextgisweb/panorama360/panorama360-display",

], function (
    declare,
    i18n,
    array,
    domClass,
    on,
    put,
    route,
    request,
    DisplayWidget,
    reactApp,
    Panorama360Display,

) {
    return declare([DisplayWidget], {
        
        // var data = plugin.display.get("itemConfig").plugin[plugin.identity];
        // webmap information


        title: "Panorama360",
        // title: i18n.gettext("Panorama360"),
        // Uncaught TypeError: i18n.gettext is not a function

        startup: function () {
            this.inherited(arguments);
        },



        renderValue: function (url) {
            // var plugin = this.plugin;
            // console.log(plugin.display.get("itemConfig").plugin[plugin.identity]);
            console.log(url);
            if (!this.isValidUrl(url)) {
                return false;
            };



            this.inherited(arguments);
            var widget = this;
            this.component = reactApp.default(
                Panorama360Display.default, 
                {
                    url: url,
                    _open: true
                },
                this.domNode
            );
        },


        isValidUrl: function (url) {
            var pattern = new RegExp(/^(https?:\/\/)?([\w.\-]+)\.([a-z]{2,})(\/[\w.\-%]*)*\/?$/i);
            return pattern.test(url);

        },



    });
})