from nextgisweb.env import Base, _
from nextgisweb.lib import db
from nextgisweb.resource import (
    Resource,
    ResourceGroup,
    Serializer,
    SerializedProperty as SP,
    DataScope,
    DataStructureScope,
    ResourceScope,
    MetadataScope,
)

class Panorama360Webmap(Base):
    __tablename__ = 'panorama360_settings'

    resource_id = db.Column(db.ForeignKey(Resource.id), primary_key=True)
    enabled = db.Column(db.Boolean, default=False)
    panorama_layer_field = db.Column(db.Unicode, default="panorama_url")
    

    resource = db.relationship(Resource, backref=db.backref(
        'panorama360', cascade='all, delete-orphan', uselist=False))

    

    def to_dict(self):
        return dict(
            resource_id=self.resource_id,
            panorama_layer_field=self.panorama_layer_field,
            enabled=self.enabled)


class _Panorama360Webmap_enabled(SP):
    def getter(self, srlzr):
        panorama360 = srlzr.obj.panorama360
        if panorama360 is None:
            return None
        return panorama360.enabled
        
    def setter(self, srlzr, value):
        if srlzr.obj.panorama360 is None:
            srlzr.obj.panorama360 = Panorama360Webmap()
        srlzr.obj.panorama360.enabled = value


class _Panorama360Webmap_layer_field(SP):
    def getter(self, srlzr):
        panorama360 = srlzr.obj.panorama360
        if panorama360 is None:
            return None
        return panorama360.panorama_layer_field
        
    def setter(self, srlzr, value):
        if srlzr.obj.panorama360 is None:
            srlzr.obj.panorama360 = Panorama360Webmap()
        srlzr.obj.panorama360.panorama_layer_field = value




class Panorama360WebmapSerializer(Serializer):
    identity = Panorama360Webmap.__tablename__
    resclass = Resource

    enabled = _Panorama360Webmap_enabled(write=MetadataScope.write, read=MetadataScope.read)
    panorama_layer_field = _Panorama360Webmap_layer_field(write=MetadataScope.write, read=MetadataScope.read)





