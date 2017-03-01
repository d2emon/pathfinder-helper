#! /usr/bin/env python
# -*- coding:utf-8 -*-
from web import app


import os
debug = os.environ.get('DEBUG', False)
if __name__ == "__main__":
    app.run(debug=debug)
