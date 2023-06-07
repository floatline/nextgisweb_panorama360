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
)
from nextgisweb.webmap import WebMap

from .util import _

# I'm not sure how Base works but without it Panorama360 doesn't show up in the Resource tab
Base = declarative_base()

class Panorama360Layer(Base, Resource):
    identity = 'panorama360_layer'
    cls_display_name = _("Panorama360")

    __scope__ = DataScope

    url = db.Column(db.Unicode, nullable=False)
    # qms = db.Column(db.Unicode)
    # copyright_text = db.Column(db.Unicode)
    # copyright_url = db.Column(db.Unicode)

    @classmethod
    def check_parent(cls, parent):
        return isinstance(parent, ResourceGroup)


class Panorama360Table(Base):
    __tablename__ = 'panorama360_table'

    webmap_id = db.Column(db.ForeignKey(WebMap.id), primary_key=True)
    resource_id = db.Column(db.ForeignKey(Resource.id), primary_key=True)
    display_name = db.Column(db.Unicode, nullable=False)
    panorama_layer_field = db.Column(db.Unicode, nullable=False)
    enabled = db.Column(db.Boolean)
    
    
    table = db.relationship(
        WebMap, foreign_keys=webmap_id, backref=db.backref(
                'panoramas', cascade='all, delete-orphan',
                collection_class=ordering_list('panorama_layer_field')))
    resource = db.relationship(
         Resource, foreign_keys=resource_id,
         backref=db.backref('_panoramas', cascade='all'))

    def to_dict(self):
        return dict(
            resource_id=self.resource_id,
            panorama_layer_field=self.panorama_layer_field,
            enabled=self.enabled,)

class Panorama360LayerSerializer(Serializer):
    identity = Panorama360Layer.identity
    resclass = Panorama360Layer

    url = SP(read=DataScope.read, write=DataScope.write)
    # qms = SP(read=DataScope.read, write=DataScope.write)
    # copyright_text = SP(read=DataScope.read, write=DataScope.write)
    # copyright_url = SP(read=DataScope.read, write=DataScope.write)


class _panorama360_attr(SP):
    def getter(self, srlzr):
        return [p360.to_dict() for p360 in srlzr.obj.panoramas]

    def setter(self, srlzr, value):
        srlzr.obj.panoramas = []

        for p360 in value:
            p360_object = Panorama360Table(resource_id=p360['resource_id'])
            srlzr.obj.panoramas.append(p360_object)

            for attr in ('display_name', 'enabled', 'panorama_layer_field'):
                setattr(p360_object, attr, p360[attr])


class Panorama360pWebMapSerializer(Serializer):
    identity = Panorama360Table.__tablename__
    resclass = WebMap

    panoramas = _panorama360_attr(read=ResourceScope.read,
                               write=ResourceScope.update)




