# -*- coding: utf-8 -*-

import elo
from torweb.urls import url
from elo.shortcuts import *
from elo.handlers import Handler
import requests
import urlparse
import urllib
import urllib2
import time

@url("/")
class MainHandler(Handler):
    def get(self):
        data = {"name": "torweb"}
        return self.render("main.html", **data)


@url("/main.php/live/reward", name="reward")
@url("/main.php/live/partyList", name="partyList")
class PartyList(Handler):
    def post(self):
        p = self.args
        p["event_point"] = "1000"

        post_url = urlparse.urljoin(CONFIG("DOMAIN"), self.reverse_url(self.kwargs["name"]))
        logger.info(post_url)
        #response = requests.post(post_url, data=params, headers=self.request.headers)
        params = urllib.urlencode(p)
        logger.info("CALLBACK_REQ_DATA: %s" % params)
        req = urllib2.Request(url=post_url, data=params)
        logger.info("*****CALLBACK_REQ_ALL: %s" % str(post_url + "?" + params))
        req_start = time.time()
        response = urllib2.urlopen(req).read()
        logger.info("*****callback response: %s" % response)
        response = response.decode('utf-8')
        req_end = time.time()
        logger.info("CALLBACK_REQ_TIME: START:[%s]_____END:[%s]_____USE:[%s]" % (req_start, req_end, req_end - req_start))
        logger.info("CALLBACK_RESPONSE: %s" % response)

        logger.info(response)
        self.write("success")
