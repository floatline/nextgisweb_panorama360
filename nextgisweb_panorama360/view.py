from nextgisweb.resource import Widget
from nextgisweb.webmap import WebMap



class Panorama360MapWidget(Widget):
    resource = WebMap
    operation = ('create', 'update')
    amdmod = 'ngw-panorama360/WebMapWidget'
