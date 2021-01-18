import os
from concurrent import futures

import grpc


class GRPCService:
    def __init__(self, workers=10, interceptors=None):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=workers), interceptors=interceptors)

    def prepare_boot(self):
        """
        :return:
        """
        raise NotImplemented

    def add_health_check(self, health_check=None):
        """
        :param health_check:
        :return:
        """
        pass

    def boot(self, secure=False):
        """
        :param service:
        :param secure:
        :return:
        """
        if secure:
            raise Exception('Secure boot not implemented')
        else:
            self.server.add_insecure_port(f'{os.environ.get("HOST")}:{os.environ.get("PORT")}')

    def start(self, secure=False):
        """
        :param secure:
        :return:
        """
        self.prepare_boot()
        self.boot(secure)
        self.server.start()
        self.server.wait_for_termination()
