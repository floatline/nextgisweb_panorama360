from nextgisweb.env import Component
from nextgisweb.lib.config import Option, OptionAnnotations


__all__ = [

]


# 360_viewer was NOT a good name
class Panorama360Component(Component):
    identity = 'Panorama_360_viewer'
    metadata = Base.metadata

    def initialize(self):
        super(Panorama360Component, self).initialize()
        self._qgis_initialized = False

    def configure(self):
        super(Panorama360Component, self).configure()

    def setup_pyramid(self, config):
        super(Panorama360Component, self).setup_pyramid(config)

        from . import view, api
        api.setup_pyramid(self, config)
        view.setup_pyramid(self, config)

    def sys_info(self):
        return (
            ("Panorama360", VERSION),
        )


    option_annotations = OptionAnnotations((
        Option('svg_path', list, doc="Search paths for SVG icons."),
        Option('default_style', bool, default=True),
        Option('logging_level', str, default=None),
        Option('test.qgis_headless_path', str, default=None, doc=(
            "Path to QGIS headless package for loading test data.")),
    ))


def pkginfo():
    return dict(components=dict(panorama360="nextgisweb_360_viewer"))


def amd_packages():
    return ((
        'ngw-360-viewer 'nextgisweb_360_viewer:amd/ngw-360-viewer'
    ),)
