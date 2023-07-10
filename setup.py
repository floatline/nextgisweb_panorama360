import io
from setuptools import setup, find_packages

with io.open('VERSION', 'r') as fd:
    VERSION = fd.read().rstrip()


# add any packages that you used
requires = (
    'nextgisweb>=4.5.0.dev7'
)

entry_points = {
    'nextgisweb.packages': [
        'nextgisweb_panorama360 = nextgisweb:single_component',
    ],
}

setup(
    name='nextgisweb_panorama360',
    version=VERSION,
    description='360 Panorama Viewer for NextGIS Web',
    author='floatline',
    author_email='info@nextgis.com',
    #packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8,<4",
    install_requires=requires,
    entry_points=entry_points,
)
