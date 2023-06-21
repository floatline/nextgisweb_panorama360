from nextgisweb.feature_layer import FeatureExtension
from nextgisweb.env.model import DBSession
import requests

from .model import Panorama360Webmap


class Panorama360Extension(FeatureExtension):
    identity = "panorama360"

    display_widget = "ngw-panorama360/DisplayWidget"
    # "@nextgisweb/panorama360/somecomponent"



    def serialize(self, feature):
        enabled =  DBSession.query(Panorama360Webmap).first().enabled
        panorama_layer_field = DBSession.query(Panorama360Webmap).first().panorama_layer_field
        if enabled:
            if panorama_layer_field in feature.fields.keys():
                url = feature.fields[panorama_layer_field]
                if url:
                    try:
                        response = requests.head(url)
                        # if response.status_code == requests.codes.ok:
                        # why does it give the 403 Forbidden code?
                        if response.status_code in (200, 403):
                            return url
                    except requests.exceptions.RequestException:
                        raise Exception("Nothing came")
        else:
            return None
        

    def deserialize(self, feature, data):
        # obj = Panorama360Webmap.first()

        # if obj is None:
        #     if data is not None:
        #         obj = Panorama360Webmap(
        #             resource_id = self.layer.id
        #         )
        pass
