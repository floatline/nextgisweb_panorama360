from nextgisweb.webmap.plugin import WebmapPlugin


@WebmapPlugin.registry.register
class Panorama360Plugin(WebmapPlugin):

    @classmethod
    def is_supported(cls, webmap):
        return (
            "ngw-panorama360/WebMapWidget",
            dict(
                 enabled=webmap.panorama360.enabled,
                 panorama_layer_field=webmap.panorama360.panorama_layer_field,    
        )
        )
