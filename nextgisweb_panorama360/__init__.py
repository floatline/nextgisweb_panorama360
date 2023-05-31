from nextgisweb.env import Component
from nextgisweb.lib.config import Option
from .model import Base
__all__ = [

]

VERSION = "0.0.1"


class Panorama360Component(Component):
    identity = 'panorama360'
    metadata = Base.metadata

    def initialize(self):
        super(Panorama360Component, self).initialize()

    def configure(self):
        super(Panorama360Component, self).configure()

    def setup_pyramid(self, config):
        super(Panorama360Component, self).setup_pyramid(config)

        from . import view
        view.setup_pyramid(self, config)

    def sys_info(self):
        return (
            ("Panorama360", VERSION),
        )


    


def pkginfo():
    return dict(components=dict(panorama360="nextgisweb_panorama360"))


def amd_packages():
    return ((
        'ngw-panorama-360', 'nextgisweb_panorama_360:amd/ngw-panorama360'
    ),)
