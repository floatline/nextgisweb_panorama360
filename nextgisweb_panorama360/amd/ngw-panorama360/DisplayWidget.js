define([
    "dojo/_base/declare",
    "dojo/_base/array",
    "dojo/dom-class",
    "dojo/on",
    "put-selector/put",
    "@nextgisweb/pyramid/i18n!",
    "@nextgisweb/pyramid/api",
    "ngw-feature-layer/DisplayWidget",
    "@nextgisweb/gui/react-app",
    "@nextgisweb/panorama360/panorama360-plugin",

], function (
    declare,
    i18n,
    array,
    domClass,
    on,
    put,
    route,
    DisplayWidget,
    reactApp,
    Panorama360Plugin,

) {
    return declare([DisplayWidget], {



        title: "Panorama360",
        // title: i18n.gettext("Panorama360"),
        // Uncaught TypeError: i18n.gettext is not a function

        startup: function () {
            this.inherited(arguments);
        },

        isValidUrl: function (url) {
            var pattern = new RegExp(/^(https?:\/\/)?([\w.\-]+)\.([a-z]{2,})(\/[\w.\-%]*)*\/?$/i);
            return pattern.test(url);
        },


        renderValue: function (url) {
            console.log(url);
            if (!this.isValidUrl(url)) {
                return false;
            }
            


            this.inherited(arguments);
            var widget = this;
            this.component = reactApp.default(
                Panorama360Plugin.default,
                {
                    // onChange: function (url) {
                    //     widget._url = url
                    // }

                    url: url
                },
                this.domNode
            );
        },


    });
})