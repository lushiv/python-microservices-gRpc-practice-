from ehub_python_protos.ehub_ecom import order_rpc_pb2_grpc
from bb_python_utils.helpers.config import Config
from bb_python_utils.libraries.grpc import BaseService

from definition.definitions import ROOT_DIR
from services import service


class Service(BaseService.GRPCService): # inherit from BaseService (GRPCService os Parent classs and Service is Child)
    def __init__(self): # Constructor
        super(Service, self).__init__(workers=10, interceptors=None)  # super is also called inherit classs and this super import __init__ and first parameter is whic is use

    def prepare_boot(self):     #  abstract method for prepare_boot on Parent class
        Config.load_env(ROOT_DIR + '/.env')
        order_rpc_pb2_grpc.add_OrderManagementServicesServicer_to_server(service, self.server)  # send to details from services package
        print('Server is Running')

if __name__ == "__main__":
    Service().start(secure=False) # first create obj service and run Service class go on Constructor