from nextgisweb.feature_layer import FeatureExtension
from nextgisweb.env.model import DBSession
from nextgisweb.resource import (
    Resource,
    ResourceScope)
import requests

from .model import Panorama360Webmap
from nextgisweb.pyramid.view import home


class Panorama360Extension(FeatureExtension):
    identity = "panorama360"

    display_widget = "ngw-panorama360/DisplayWidget"
    # "@nextgisweb/panorama360/somecomponent"



    # def serialize(self, feature):

    #     # FIXME Somehow provide resource id of the webmap
    #     # Sending the table in a dict to front is a bad idea

    #     db_request = DBSession.query(Panorama360Webmap).all()
    #     result_dict = {}
    #     for row in db_request:
    #         result_dict[str(row.resource_id)] = row.to_dict()
    #     return (dict(feature.fields), result_dict)



    def serialize(self, feature):
        enabled =  DBSession.query(Panorama360Webmap).first().enabled
        panorama_layer_field = DBSession.query(Panorama360Webmap).first().panorama_layer_field
        if enabled:
            if panorama_layer_field in feature.fields.keys():
                url = feature.fields[panorama_layer_field]
                return url
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
