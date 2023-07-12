from nextgisweb.env import Component, require
from nextgisweb.lib.config import Option
from .model import Panorama360Webmap, Base


class Panorama360Component(Component):

    def initialize(self):
        from . import extension

    def configure(self):
        super(Panorama360Component, self).configure()

    @require('resource', 'webmap')
    def setup_pyramid(self, config):
        from . import view

    def client_settings(self, request):
        return 
