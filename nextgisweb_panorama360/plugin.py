from nextgisweb.webmap.plugin import WebmapPlugin


@WebmapPlugin.registry.register
class Panorama360Plugin(WebmapPlugin):

    @classmethod
    def is_supported(cls, webmap):
        # TODO: Security
        panoramas = [dict(
            url=p360.resource.url,
            **p360.to_dict())
            for p360 in webmap.panoramas]
        return (
            "ngw-panorama360/plugin/Panorama360",
            dict(
                 panoramas=panoramas,
        )
        )
