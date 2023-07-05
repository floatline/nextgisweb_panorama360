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
    "@nextgisweb/pyramid/i18n!",
    "@nextgisweb/gui/react-app",
    "@nextgisweb/panorama360/panorama360-display",
    "@nextgisweb/pyramid/settings!webmap"
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
    i18n,
    reactApp,
    Panorama360Display,
    webmapSettings
) {
    return declare([DisplayWidget], {

        title: i18n.gettext("Panorama360"),

        buildRendering: function(){
			this.inherited(arguments);
            // To see global webmap settings
            // TODO: try to update global webmap settings model with panorama default params
            // console.log(webmapSettings)

            console.log(this.webmapId)
		},

        renderValue: function (url) {

            if (!this.isValidUrl(url)) {
                return false;
            };
            this.inherited(arguments);
            this.component = reactApp.default(
                Panorama360Display.default,
                {
                    url: url
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