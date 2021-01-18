from bb_python_utils.libraries.database import MySqlDB
import json
import  os
import  random
import  uuid
from bb_python_utils.helpers import validation_helper

db = MySqlDB.MysqlDatabase(database_name='ehub_order_service_db')
db.connect()


def get_fetch_orders_list(args):
    try:
        current_page = args.currentPage
        per_page = args.perPage
        db = MySqlDB.MysqlDatabase(database_name='ehub_order_service_db')
        db.connect()
        order_list =[]
        query = "select * from order_table o  INNER JOIN address_details a ON a.address_details = a.order_id;"
        data = db.get_fetch_data(query)
        for row in data:
            customer_data ={}
            customer_data['data']={}
            customer_data['data']['order_id'] = row[1]
            customer_data['data']['custumer_id'] = row[2]
            customer_data['data']['custumer_type'] = row[3]
            customer_data['data']['first_name'] = row[4]
            customer_data['data']['last_name'] = row[5]
            customer_data['data']['email'] = row[6]
            customer_data['data']['phone'] = row[7]
            customer_data['data']['address_line1'] = row[8]
            customer_data['data']['address_line2'] = row[9]
            customer_data['data']['ordstateer_id'] = row[10]
            customer_data['data']['city'] = row[11]
            customer_data['data']['postal_zip'] = row[12]
            order_list.append(customer_data)
        
        print(order_list)
        return order_list


    except Exception as e:
        raise e