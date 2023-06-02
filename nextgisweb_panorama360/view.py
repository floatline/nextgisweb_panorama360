from nextgisweb.resource import Widget
from nextgisweb.webmap import WebMap
from .model import Panorama360Layer


class Panorama360LayerWidget(Widget):
    resource = Panorama360Layer
    operation = ('create', 'update')
    amdmod = 'ngw-panorama360/LayerWidget'


class Panorama360MapWidget(Widget):
    resource = WebMap
    operation = ('create', 'update')
    amdmod = 'ngw-panorama360/WebMapWidget'
