#!/usr/bin/env python

import tornado
from datetime import date
import tornado.escape
import tornado.ioloop
import tornado.web
import opendsd
import json


class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        response = {'version': '0.0.1', 'last_build':  date.today().isoformat()}
        self.write(response)


class GraffitiHandler(tornado.web.RequestHandler):
    def get(self):
        dsd = opendsd.OpenDSD()

        swlat = '32.71879985593221'
        swlong = '-117.16525563507082'
        nelat = '32.74399836325726'
        nelong = '-117.12534436492922'

        complaints = dsd.getRegionalComplaints(swlat, swlong, nelat, nelong)
        print complaints
        graffitiComplaints = dsd.findGraphiti(complaints)
        response = json.dumps(graffitiComplaints)
        self.write(response)


application = tornado.web.Application([
    (r"/hello", HelloHandler),
    (r"/graffiti", GraffitiHandler)
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
