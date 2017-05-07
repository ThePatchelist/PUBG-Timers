from distutils.core import setup
import py2exe

setup(
    name='pubg_timer',
    version='1.0.1',
    install_requires=['pypiwin32'],
    license='Copyright by ThePatchelist',
    windows=[{
        'script': 'main.py',
        'icon_resources': [(0, "assets/favicon.ico")],
        'dest_base': 'PUBGTimers',
    }],
    options={'py2exe': {'compressed': 1,
                        'bundle_files': 1
                        },
             },
    data_files=[("assets", ["assets/favicon.ico", "assets/alarm.wav"])],
    zipfile=None
)