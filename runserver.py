#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys
import argparse

if not os.path.isdir('uploads'):
    os.mkdir('uploads')

from uploader.app import app

parser = argparse.ArgumentParser(description="uploader")
parser.add_argument(
    "--port", "-p",
    type=int,
    help="Port to listen on",
    default=80,
)
args = parser.parse_args()

if __name__ == '__main__':
    flask_options = dict(
        host='0.0.0.0',
        debug=True,
        port=args.port,
        threaded=True,
    )
    print(app.root_path)

    app.run(**flask_options)

