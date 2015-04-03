#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created: zhangpeng <zhangpeng1@infohold.com.cn>

import os
import elo
import logging
import tornado.web
from tornado.options import options
from torweb.application import make_application 
from torweb.config import CONFIG
from torweb import run_torweb
from code import interact
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


settings_path = os.path.join(elo.base_path, "settings.yaml")
logging.info("^_^")
logging.info(settings_path)

CONF = CONFIG(settings_path)
debug = CONF("DEBUG_PAGE")
url_root = CONF("URL_ROOT")

default_port = 8888
app = make_application(elo, debug, wsgi=True, settings_path=settings_path, url_root=url_root)
setattr(app, '_wsgi', False)
if options.cmd == "runserver":
    run_torweb.run(app, port=default_port)
else:
    run_torweb.show_urls(elo)
