#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created: zhangpeng <zhangpeng1@infohold.com.cn>

import elo
import os
import logging
import traceback

from torweb.urls import url
from torweb.tmpl import get_environment
from torweb.config import CONFIG as CONFIGURATION

CONFIG = CONFIGURATION(os.path.join(elo.base_path, "settings.yaml"))

env = get_environment(elo.__name__)

cache = elo.cache

from logging.handlers import TimedRotatingFileHandler
from os.path import join

def __init_log(_type):
    _log_path = join(elo.base_path, 'static', 'log', _type)
    if not os.path.exists(_log_path): os.makedirs(_log_path)
    _log = TimedRotatingFileHandler(join(_log_path, '%s.log' % _type), 'MIDNIGHT')
    _log.setFormatter(logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s'))
    _log.setLevel(logging.NOTSET)
    _logger = logging.getLogger(_type)
    _logger.addHandler(_log)
    return _logger

logger = __init_log('payment')



#from sqlalchemy import Table, Column, ForeignKey
#from sqlalchemy.types import String, Integer, Unicode, Date, DateTime
#from sqlalchemy.orm import mapper, relationship
#from sqlalchemy import select, and_, or_
#from sqlalchemy.ext.declarative import declarative_base
#
#BaseModel = declarative_base()

