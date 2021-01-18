from ehub_python_protos.ehub_ecom import order_pb2,common_pb2,errors_pb2,product_rpc_pb2_grpc
from modules.order_management.methods import add_orders,get_orders_list

class CreateOrder:
    def __new__(cls, *args, **kwargs):
        add_orders.add_orders_list(args[0])

        response = order_pb2.CreateOrderResponse(
            error = False,
            success = True,
            msg = 'Successfully created'
        )
        return response


class ViewOrder:
    def __new__(cls, *args, **kwargs):
        data = get_orders_list.get_fetch_orders_list(args[0])

        response = order_pb2.OrdersListResponse(

            data = [{'orderId':'xxxxxxxxxx','date': '2020-12-04','customer': 'Janak Raikhola','orderStatus': 3,
            'paymentStatus': 2, 'total':1657, 'items':[{'productName': 'Dell Laptop','productLink':'www.demolink.com' }]}, {'orderId':'xxxxxxxxxx','date': '2020-12-04','customer': 'Janak Raikhola','orderStatus': 3,
            'paymentStatus': 2, 'total':1657, 'items':[{'productName': 'Dell Laptop','productLink':'www.demolink.com' }]}],

            msg = '',
            success = True,
            pagination = common_pb2.Pagination(
            )
        )
     
        return response
        
        
class InvoiceOrder():
    def __new__(cls, *args, **kwargs):
        response = order_pb2.InvoiceListResponse(
            vendorDetails = [{}],
            shipTo = [{}],
            billTo = [{}],
            iteams = [{}],
            bill = [{}],
        )

        return response


