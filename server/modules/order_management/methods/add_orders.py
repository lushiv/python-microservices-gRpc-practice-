from bb_python_utils.libraries.database import MySqlDB
import json
import  os
import  random
import  uuid
from bb_python_utils.helpers import validation_helper

db = MySqlDB.MysqlDatabase(database_name='ehub_order_service_db')
db.connect()

def add_orders_list(*args, **kwargs):
    try:
        data = args[0]
        unique_id = uuid.uuid4().hex
        generalDetails = data.generalDetails
        order_date = generalDetails.orderDate
        payment_status = generalDetails.paymentStatus
        order_status = generalDetails.orderStatus
        remark = generalDetails.orderStatusChangeRemarks
        payment_type = generalDetails.payment
        sql = "INSERT into order_table (uuid,order_date, payment_status,order_status,order_remark,payment_type) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (unique_id,order_date,payment_status,order_status,remark,payment_type)
        order_id=db.insert_data(sql,val)
        
        #Product detailss
        productDetails = data.productDetails[0]
        product_name = 'sample product'
        product_image = 'www.sample.com'
        product_sku = 'SWRE32354'
        product_qnty = productDetails.quantity
        product_cost = 7898
        total_cost = product_qnty*product_cost
        product_id = 12

        sql = "INSERT into product_details (product_id,order_id,name,link,sku,quantity,cost,total) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (product_id,order_id,product_name,product_image,product_sku,product_qnty,product_cost,total_cost)
        db.insert_data(sql,val)
        #addressDetails
        custumer_id = 1
        addressDetails = data.addressDetails
        custumer_type = addressDetails.customerType
        first_name = addressDetails.firstName
        last_name = addressDetails.lastName

        email = addressDetails.email
        valid_email= validation_helper.check_mails(email)
        if valid_email == True:
            phone = addressDetails.phone
            address_line1 = addressDetails.addressLine1
            address_line2 = addressDetails.addressLine2
            state = addressDetails.State
            city = addressDetails.city
            postal_zip = addressDetails.postalZip
            sql = "INSERT into address_details (order_id,custumer_id,custumer_type,first_name,last_name,email,phone,address_line1,address_line2,state,city,postal_zip) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (order_id,custumer_id,custumer_type,first_name,last_name,email,phone,address_line1,address_line2,state,city,postal_zip)
            db.insert_data(sql,val)
        else:
            return()

    except Exception as e:
        raise e