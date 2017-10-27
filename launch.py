import time

from zeroconf import ServiceBrowser, Zeroconf


class ServiceListener(object):
    def __init__(self, zeroconf):
        self._zeroconf = zeroconf
        self._workers = []

    @property
    def workers(self):
        return self._workers

    def remove_service(self, zeroconf, service_type, name):
        print("service removed: {}".format(name))

    def add_service(self, zeroconf, service_type, name):
        info = self._zeroconf.get_service_info(service_type, name, timeout=30)
        print("service added - name: '{}', type: '{}', info: {}".format(name, service_type, info))
        self._workers.append(info)


zeroconf = Zeroconf()
listener = ServiceListener(zeroconf)
SERVICE_TYPE = "_service-worker._tcp.local."
browser = ServiceBrowser(zeroconf, SERVICE_TYPE, listener)

try:
    while True:
        time.sleep(7)
finally:
    zeroconf.close()
