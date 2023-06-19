from nextgisweb.feature_layer import FeatureExtension
from nextgisweb.env.model import DBSession

from .model import Panorama360Webmap

class Panorama360Extension(FeatureExtension):
    identity = "panorama360"

    display_widget = "ngw-panorama360/DisplayWidget"

    def serialize(self, feature):
        # enabled = Panorama360Webmap.enabled
        # panorama_layer_field = Panorama360Webmap.panorama_layer_field
        # if self.layer.
        pass

    def deserialize(self, feature, data):
        # obj = Panorama360Webmap.first()

        # if obj is None:
        #     if data is not None:
        #         obj = Panorama360Webmap(
        #             resource_id = self.layer.id
        #         )
        pass