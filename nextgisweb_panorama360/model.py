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

    panorama360_table_id = db.Column(db.Integer, primary_key=True)
    resource_id = db.Column(db.ForeignKey(Resource.id), primary_key=True)
    # position = db.Column(db.Integer)
    display_name = db.Column(db.Unicode, nullable=False)
    # enabled = db.Column(db.Boolean)
    # opacity = db.Column(db.Float)

    # table = db.relationship(
    #     WebMap, foreign_keys=webmap_id, backref=db.backref(
    #         'basemaps', cascade='all, delete-orphan', order_by=position,
    #         collection_class=ordering_list('position')))

    #resource = db.relationship(
    #     Resource, foreign_keys=resource_id,
    #     backref=db.backref('_basemaps', cascade='all'))

    # def to_dict(self):
    #     return dict(
    #         resource_id=self.resource_id,
    #         position=self.position,
    #         display_name=self.display_name,
    #         enabled=self.enabled,
    #         opacity=self.opacity)





