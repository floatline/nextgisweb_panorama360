from .model import Panorama360Webmap
from nextgisweb.env.model import DBSession


def get_enabled(resource, request):
    request.resource_permission(MetadataScope.read)
    enabled = DBSession.query(Panorama360Webmap).filter(resource.id).enabled
    return enabled


def get_layer_field(resource, request):
    request.resource_permission(MetadataScope.read)
    panorama_layer_field = DBSession.query(
        Panorama360Webmap).filter(resource.id).enabled
    return panorama_layer_field

def setup_pyramid(comp, config):
    colurl = '/api/resource/{id}/feature/{fid}/attachment/'
    itmurl = '/api/resource/{id}/feature/{fid}/attachment/{aid}'

    config.add_route(
        'panorama360.enabled',
        itmurl + '/download',
        factory=resource_factory,
    ).add_view(download)

    config.add_route(
        'panorama360.layer_field',
        itmurl + '/layer_field',
        factory=resource_factory,
    ).add_view(image)

    config.add_route(
        'feature_attachment.item', itmurl,
        factory=resource_factory) \
        .add_view(iget, request_method='GET') \
        .add_view(iput, request_method='PUT') \
        .add_view(idelete, request_method='DELETE')

    config.add_route(
        'feature_attachment.collection', colurl,
        factory=resource_factory) \
        .add_view(cget, request_method='GET') \
        .add_view(cpost, request_method='POST')

    config.add_route(
        'feature_attachment.export',
        '/api/resource/{id}/feature_attachment/export',
        factory=resource_factory
    ).add_view(export)

    config.add_route(
        'feature_attachment.import',
        '/api/resource/{id}/feature_attachment/import',
        factory=resource_factory
    ).add_view(import_attachment, request_method='PUT')