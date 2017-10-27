from os import listdir
from os.path import isfile, join
import socket
import time

import sys
import tensorflow as tf
from zeroconf import ServiceInfo, Zeroconf


class ServiceAdvertiser(object):
    SERVICE_TYPE = '_service-worker._tcp.local.'
    SERVICE_NAME = 'MyService'

    def __init__(self):
        self._zeroconf = Zeroconf()
        self._port = 4242

    def start(self):
        fqdn = socket.gethostname()
        ip_address = socket.gethostbyname(fqdn)
        print("fqdn: {}".format(fqdn))
        print("ip address: {}".format(ip_address))
        descriptor = {'service': self.SERVICE_NAME, 'version': '1.0.0'}
        self._service_info = ServiceInfo(self.SERVICE_TYPE,
                                         fqdn + ' ' + self.SERVICE_NAME + '.' + self.SERVICE_TYPE,
                                         socket.inet_aton(ip_address), self._port, 0, 0,
                                         descriptor, fqdn + ".local")
        self._zeroconf.register_service(self._service_info)

    def stop(self):
        if self._service_info is not None:
            self._zeroconf.unregister_service(self._service_info)


worker = ServiceAdvertiser()
worker.start()
try:
    config = open("/config.json").read()
    print("config: {}".format(config))
    sys.stdout.flush()
    with tf.Session() as session:
        while True:
            time.sleep(7)
except KeyboardInterrupt:
    print("exiting")
finally:
    worker.stop()
