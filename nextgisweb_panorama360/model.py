from sqlalchemy.ext.orderinglist import ordering_list

from nextgisweb.env.model import declarative_base
from nextgisweb.lib import db
from nextgisweb.resource import (
    Resource,
    ResourceGroup,
    Serializer,
    SerializedProperty as SP,
    DataScope,
    ResourceScope,
    MetadataScope,
)
from nextgisweb.webmap import WebMap

from .util import _

Base = declarative_base()

class Panorama360Settings(Base):
    __tablename__ = 'panorama360_settings'

    resource_id = db.Column(db.ForeignKey(Resource.id), primary_key=True)
    panorama_layer_field = db.Column(db.Unicode, nullable=False)
    enabled = db.Column(db.Boolean)

    resource = db.relationship(Resource, backref=db.backref(
        'panorama360', cascade='all, delete-orphan', uselist=False))

    

    def to_dict(self):
        return dict(
            resource_id=self.resource_id,
            panorama_layer_field=self.panorama_layer_field,
            enabled=self.enabled,)


class _Panorama360Settings_enabled(SP):
    def getter(self, srlzr):
        panorama360 = srlzr.obj.panorama360
        if panorama360 is None:
            return None
        return panorama360.enabled
        
    def setter(self, srlzr, value):
        if srlzr.obj.panorama360 is None:
            srlzr.obj.panorama360 = Panorama360Settings()


class _Panorama360Settings_layer_field(SP):
    def getter(self, srlzr):
        panorama360 = srlzr.obj.panorama360
        if panorama360 is None:
            return None
        return panorama360.panorama_layer_field
        
    def setter(self, srlzr, value):
        if srlzr.obj.panorama360 is None:
            srlzr.obj.panorama360 = Panorama360Settings()
        srlzr.obj.panorama360 = value


class _Panorama360Settings_resource_id(SP):
    def getter(self, srlzr):
        panorama360 = srlzr.obj.panorama360
        return panorama360.resource_id
              


class Panorama360pSettingsSerializer(Serializer):
    identity = Panorama360Settings.__tablename__
    resclass = Resource

    resource_id = _Panorama360Settings_resource_id(write=ResourceScope.read)
    enabled = _Panorama360Settings_enabled(write=MetadataScope.write, read=MetadataScope.read)
    panorama_layer_field = _Panorama360Settings_layer_field(write=MetadataScope.write, read=MetadataScope.read)





