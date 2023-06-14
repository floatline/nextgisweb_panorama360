from nextgisweb.env import Component, require
from nextgisweb.lib.config import Option
from .model import Base, Panorama360Webmap
__all__ = [
    'Base', 'Panorama360Webmap'
]

VERSION = "0.0.1"


class Panorama360Component(Component):
    identity = 'panorama360'
    metadata = Base.metadata

    def initialize(self):
        from . import plugin

    def configure(self):
        super(Panorama360Component, self).configure()

    @require('resource', 'webmap')
    def setup_pyramid(self, config):
        from . import view

    def client_settings(self, request):
        return 

    def sys_info(self):
        return (
            ("Panorama360", VERSION),
        )


def pkginfo():
    return dict(components=dict(panorama360="nextgisweb_panorama360"))


def amd_packages():
    return ((
        'ngw-panorama360', 'nextgisweb_panorama360:amd/ngw-panorama360'
    ),)
