# -*-coding: utf-8 -*-
import tornado.ioloop
import tornado.httpserver

import urls

port = 8020

if __name__ == "__main__":
    app = urls.application
    app.listen(port)
    print("Starting development server at http://127.0.0.1:" + str(port))
    print("Quit the server with CONTROL-C.")
    tornado.ioloop.IOLoop.instance().start()