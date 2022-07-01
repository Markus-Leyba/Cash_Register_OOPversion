

from datetime import datetime
from operator import attrgetter
from re import X
from sys import argv
import sys
import sys
import os
import datetime

 




####################### READ ME ########################

###Bugs in bundles###
# - load but errors occur in the place an order method. It seemes to be working correctly but this bug was noticed last minute. 
# - the bundle price is incorrect. There might be an issue in the dictionary logic for price and quantities. 


###class related bugs####
# - the vip threshold is a static method and adjusts the class attributes but not the object instances that are loaded when the program is run. I ran out of time. 
# - the same goes for the vip discount it is a static method. 

## The most popular product has a last minute bug. Not sure what happen. It was working then last minute there was an index out of range error. 

### REFLECTION ####

## While this program meets the majority of the use case requirements it is overly complex and often logically inconsistent. It attemtps implement low coupling and high cohesion. In some ways it succeeds. For example the concentration of methods are placed in the records class. This enables the Menu to be adjusted with minimal impact to the core functionality of the program. 
# I also implemented a Tools Class, which I am still not sure if it is efficient but my mindset was to treat it as if I was professional creating code that would be used by others. Therefore, a place for static methods that provide small functionalaties made creating other methods easier. 
# Also, because I am relatively new to programming, the program reflects those inconsistencies. In a sense, it is like a frankenstein. I have no regrets, because I have learned the hard way to think hard about the structure of data. For example, I would use dictionaries more often. I would also implement a method to convert lists and objects to dictionaries given 2 variables, 3 variables and so on. 
# I think this would really increase my work efficiency drastically. I would also create more methods that are reusable for example, string_inputValidation method in Tools can be used with (a message, a validator function, error message). This is an example of low coupling. 
# The place and order method is spaghetti code in some parts. This is mainly due to running out of time and my inexperience. There are some parts which I think are done well such as the validators functions and the while loop for ordering again. Also the stock, price and product quantity blocks in my 
# opinon exhibit low coupleing and high cohesion. This project has really helped me appreciate the immediate value of low coupling and high cohesion because errors in the IF statement heavy parts of the place an order section
# took a lot time to untangle and fix. It had high cohesion and high coupling. 



 
 
################################################################################# CUSTOMER CLASS ####################################################################################################
       
       
                                      
class Customer():
     
    customer_name = ''
    discount_rate= 1
    total_spent = 0

    def __init__(self, customer_ID, customer_name, discount_rate, total_spent): 
        self.customer_ID = customer_ID                                          
        self.customer_name = customer_name                                       
        self.discount_rate = discount_rate                                      
        self.total_spent = total_spent
        
    def __str__ (self):
        return ', '.join([str(i) for i in [self.customer_ID,self.customer_name,self.discount_rate,self.total_spent]]) 
    
    def __repr__(self) -> str:
        return f"({self.customer_ID}, {self.customer_name}, {self.discount_rate}, {self.total_spent})"
    
    @staticmethod
    def display_customer_attributes():
        if __name__ == '__main__':
            x = vars(VIPMemeber)
            for item in x:
                print (item ,' : ', x[item])
    
    @property
    def get_customer_ID(self):
        return self.customer_ID
    
    @property
    def get_customer_name(self):
        return self.customer_name
    
    @staticmethod    ## issue: not sure if I should use static variables here. NO unless i have a solid reason. 
    def get_discount_rate():
        return Customer.discount_rate
        
    @property
    def get_total_spent(self):
        return self.total_spent
    
    @get_total_spent.setter               ### THIS ALLOWS ME TO ADD ORDER TOTAL TO TOTAL SPENT FROM ORDERS/OPERATIONS CLASS
    def set_total_spent(self, order_total): #order_total will come from order class
        self.total_spent = self.total_spent + order_total
        
     
     
##############################################################################  MEMBERS  ################################################################################################
     
     
     
class Member(Customer):
    member_fee = 50.0
    discount_rate = 0.05 
     
    def __init__(self, customer_ID, customer_name, discount_rate, total_spent):
        self.customer_ID = customer_ID
        self.customer_name = customer_name
        self.discount_rate = 0.05
        self.total_spent = total_spent

    def __str__(self):
        return ', '.join([str(i) for i in [self.get_customer_ID,self.get_customer_name,self.discount_rate,self.get_total_spent]])
    
    def __repr__(self) -> str:
        return f"({self.customer_ID}, {self.customer_name}, {self.discount_rate}, {self.total_spent})" 
    
    @staticmethod
    def display_customer_attributes():
        if __name__ == '__main__':
            x = vars(Member)
            for item in x:
                print (item ,' : ', x[item])
    
    
    @staticmethod
    def get_discount_rate():
        #print('#### GET MEMBER.GET DISCOUNT RATE METHOD ###########')
        #print(Member.discount_rate)
        return Member.discount_rate
    
    
    #########################################################################  VIP MEMBERS  ############################################################################################
 
    
class VIPMemeber(Customer):
    discount_rate = 0.15
    vip_gap = 0.05
    __premium_rate = float(discount_rate + vip_gap) * 1 ### assumes the gap between rates will always be the same.
    vip_threshold = 1000
    vip_fee = 200.0
    
    def __init__(self, customer_ID, customer_name, discount_rate, total_spent):
        self.customer_ID = customer_ID
        self.customer_name = customer_name
        self.discount_rate = discount_rate
        self.total_spent = total_spent
        #print('########### VIP INIT ###################')
        #print(self)
        
    def __str__(self):
        #print('########### VIP STR ###################') 
        return ', '.join([str(i) for i in [self.get_customer_ID,self.get_customer_name,self.discount_rate,self.get_total_spent]]) 
        
    def __repr__(self) -> str:
        return f"({self.get_customer_ID}, {self.get_customer_name}, {self.discount_rate}, {self.get_total_spent})"
    
    @staticmethod
    def display_customer_attributes():
        if __name__ == '__main__':
            x = vars(VIPMemeber)
            for item in x:
                print (item ,' : ', x[item])
    
    
    @staticmethod               
    def adjust_vip_threshold(new_threshold):
        vip_threshold = new_threshold
        return vip_threshold
    
    @staticmethod
    def get_premium_rate():  ### premium rate is private attribute. 
        return VIPMemeber.__premium_rate
    
    @staticmethod
    def get_discount_rate():
        return VIPMemeber.discount_rate
    
    @staticmethod
    def adjust_vip_discount(new_rate):
        discount_rate = new_rate
        return discount_rate
        
        
########################################################################################### PRODUCTS CLASS ###################################################################################################


class Product: 
    
    def __init__(self, product_ID, product_name, product_price, stock): ### these parameters will correlate with the structure of inputs in the load_products method in the records/operations section. 
        self.__product_ID = str(product_ID)
        self.__product_name = str(product_name)
        self.__product_price = float(product_price)
        self.__stock = int(stock)
        
    def __str__(self):
        
        return ', '.join([str(i) for i in [self.__product_ID, self.__product_name, self.product_price, self.__stock]])
    
    def __repr__(self) -> str:
        return f"({self.__product_ID}, {self.__product_name}, {self.product_price}, {self.__stock})"
    
    @property
    def get_product_ID(self):
        return self.__product_ID
    
    @property
    def get_product_name(self):
        return self.__product_name
    
    @property
    def get_product_price(self):
        return self.__product_price
    
    @get_product_price.setter
    def product_price (self, new_price): 
        self.__product_price = new_price ##self.something calls setter again, hence recursive issue. 
        
    @property
    def get_stock(self):
        return self.__stock
    
    @get_stock.setter                       ### this functions allows me to change stock from anywhere as along as product class is declared
    def set_stock(self, new_stock): ### product_quantity will be an attribute of orders class
        self.__stock = new_stock #stock change here
    
    ## RIGHT NOW I CAN'T SEE THE POINT OF USING ANY MORE METHODS.
    ## I ENVISION REFERENCES TO BE KEPT IN THE RECORDS CLASS AND/OR IN THE FILES WHICH WILL BE ACCESSE VIA RECORDS CLASS. 
    ## SO THE DESIGN DECISION HERE IS TO KEEP PRODUCT CLASS ONLY RELEVANT TO HOW PRODUCTS AS A CUSTOM DATA TYPE WILL BE APPLIED TO RECORD LISTS. 
    

################################################################################   BUNDLE SUBCLASS    ####################################################################################
    
    
class Bundle(Product):

                                                                                  # note that the fourth parameter needs to be a list. 
    def __init__(self, product_ID, product_name, product_ID_list, bundle_price, stock): #changed the order or parameters to suite products.txt  
         
        super().__init__(product_ID, product_name, bundle_price, stock)
        self.bundled_products_list = ','.join([str(i) for i in product_ID_list]) 
        #print('####### BUNDLE SELF #######')
        
    def __str__(self):
        return ', '.join([str(i) for i in [self.get_product_ID, self.get_product_name, self.bundled_products_list, self.get_stock]])
    
    def __repr__(self) -> str:
        return f"({self.get_product_ID}, {self.get_product_name}, {self.bundled_products_list}, {self.get_stock})"
        
    def find_product(self,prompt):
        return next(filter(lambda p: p.product_ID == prompt or p.product_name == prompt, self.products_list), None)
        
        
#####################################################################             RECORDS CLASS                        #########################################################################


class Records():
    
    customers_list = []
    products_list = []
    orders_list = []
                                                        
     ###these parameters will correlate with the structure of inputs in load_products/load_customers/load_orders methods in the records/operations section.                                                   
    def __init__(self, customers_file, products_file, orders_file = None):  
        self.customers_file = customers_file              
        self.products_file = products_file
        self.orders_file = orders_file if orders_file is not None else 'orders.txt'
        if orders_file:
            self.load_orders(orders_file) ### THESE THREE METHODS IN RECORDS CLASS
        self.load_customers(customers_file)
        self.load_products(products_file)
    
    def __str__(self):
       return ', '.join([str(i) for i in [self.customer_list, self.products_list, self.orders_list]])
    
    def __repr__(self) -> str:
        return f"({self.customer_list}, {self.products_list}, {self.orders_list})"
    
    @property
    def get_customers_list(self):
        return self.customers_list
    
    @get_customers_list.setter                       ### THIS OPTION CAN REPLACE THE WHOLE LIST
    def set_customers_list(self, updated_customers_list):
        self._customers_list = updated_customers_list
        
    def add_customer(self, a_customer):              ### THIS OPTION ADDS A SINGLE CUSTOMER
        self.customers_list.append(a_customer)       ### HAVING BOTH THESE OPTIONS ADDS VERSATILITY TO THE RECORDS CLASS FUNCTIONALITY. 
    
    @property
    def get_products_list(self):
        return self.products_list
    
    def add_product(self, a_product): ### ADDS A SINGLE PRODUCT
        self.products_list.append(a_product) # operator won't work. Use apphend instead. 
    
    @property
    def get_orders_list(self):
        return self.orders_list
        
    def add_order(self, an_order):  ### ADDS A SINGLE ORDER
        self.orders_list.append(an_order) 
    
    
    #### VALIDATOR METHODS ######
    
    def existing_customer(self, customer_identifier):
        #print('##### EXISTING CUSTOMER METHOD ###########')
        customer = self.find_customer(customer_identifier) # returns tupple. 
        #print(customer)
        if customer: # empty tupple is false, otherwise it's true. 
            #print('### TRUE ###')
            return True
        else:
            #print('### FALSE ###')
            return False
    

    def existing_member(self, customer_identifer): ## in this case it will be name. 
        #print('####### CUSTOMER IDENTIFIER ###########')
        #print(customer_identifer) ## this works, prints the correct customer_identifier
        customer = self.find_customer(customer_identifer) ### therefore the problem is here
        #print('########   CUSTOMER VARIABLE (in existing_member method)  ##################')
        #print(str(customer)) ## why is customer variable None
        if customer[0:0] == 'V':
            return True
        if customer[0:0] == 'M':
            return True
        elif customer is None:
            #print('##### CUSTOMER VARIABLE IS NONE ########')
            return False
        else:
            print('###### UNIDENTIFIED ERROR (EXISING_MEMBER METHOD) ############')
            return False
            
    def sign_up(self, str): ## str is input should be y or n Or Y or N
        answer = str
        if answer == 'n' or answer == 'N':
            return False
        if answer == 'y' or answer == 'Y':
            return True            
            
    def member_is_VIP(self, customer_identifier):
        customer = self.find_customer(customer_identifier)
        #print('########    CUSTOMER VAR in member is vip method   ########')
        #print(customer)
        #print(customer_identifier, '######CUSTOMER IDENTIFIER####')
        if customer[0].get_customer_ID[0] == 'V':
            return True
        if customer[0].get_customer_ID[0] == 'M':
            return False
        else:
            print('###### UNIDENTIFIED ERROR (EXISING_MEMBER METHOD) ############')
            return False
    
   
                
            
    ##### AUTO LOADING METHODS #####        
    
    def load_customers(self, customers_file): #read_customer  
        file_object=open(customers_file, "r")
        i=0
        line=file_object.readline()
        while(line!=""):
            customer_fields=line.split(",")
            customer_ID=str(customer_fields[0].strip(' '))
            customer_name=str(customer_fields[1].strip(' '))
            discount_rate=float(customer_fields[2].strip(' '))
            total_spent=float(customer_fields[3].strip(' '))
            a_customer = Customer(customer_ID, customer_name, discount_rate, total_spent) 
            self.add_customer(a_customer)
            line=file_object.readline()
            i+=1
        #print('##################################LOAD CUSTOMERS METHOD################################')
        #print(self.customers_list)
        #print(self.customers_list[0])
        #print(type(self.customers_list[0])) ## object 
        file_object.close()
        
            
    
    def load_products(self, products_file): #read_products       
        #print('##################################LOAD PRODUDUCTS METHOD################################')
        file_object=open(products_file, "r")                     
        i=0                                                       
        line=file_object.readline()
        while(line!=""):
            product_fields = line.split(",") #should already be a list here. Because of split. 
            #print('#########product_fields#########')
            #print(product_fields)
            #print('#### product_fields [0] ########')
            #print(product_fields[0])
            if (product_fields[0][0] == 'P'):
                product_ID = str(product_fields[0].strip(' '))
                product_name = str(product_fields[1].strip(' '))
                try:
                    product_price = (product_fields[2].strip(' '))
                    float(product_price)
                except ValueError as e:
                    #print('#####VALUE ERROR#####') 
                    #print (e) 
                    #print('PRODUCT PRICE')
                    product_price = 0.00
                    #print(product_price)
                except:
                    print('######## UNKNOWN ERROR ########')    
                    
                stock=int(product_fields[3].strip(' '))
                #print('#########product_fields after IF before instantiated #########')
                #print(product_fields)
                a_product = Product(product_ID, product_name, product_price, stock)
                #print('################################## A PRODUCT VARIABLE ################################')
                #print(a_product)
               
                #print('################################## PRODUCTS LIST BEFORE ADD_PRODUCT METHOD ################################')
                #print(self.products_list)
                self.add_product(a_product)
                #print('################################## PRODUCTS LIST AFTER ADD_PRODUCT METHOD ################################')
                #print(self.products_list)
                #time.sleep(10)
            elif (product_fields[0][0] == 'B'):   
                product_ID = str(product_fields[0].strip(' '))
                product_name = str(product_fields[1].strip(' '))
                stock = int(product_fields[-1].strip(' '))
                product_ID_list = []
                for i in product_fields[2: -1: 2]: #slice item syntax
                    i.strip(' ')
                    product_ID_list.append(i)
                bundle_price = sum([p.product_price for p in self.products_list]) * 0.8 
                #print('######### product_fields after IF (bundle) before instantiated #########')
                #print(product_fields)
                #time.sleep(10)
                a_product = Bundle(product_ID, product_name, product_ID_list, bundle_price, stock) 
                
                ## creates namespace as it's declared as object. products_list will now be a list of objects.  # need to revisit save_data as not sure how it fits now. 
                #print('################################## A PRODUCT VARIABLE (BUNDLE) ################################')
                #print(a_product)
                
                #print('################################## PRODUCTS LIST BEFORE ADD_PRODUCT METHOD ################################')
                #print(self.products_list)                                                                              
                self.add_product(a_product)
                #print('################################## PRODUCTS LIST AFTER ADD_PRODUCT METHOD ################################')
                #print(self.products_list)
            line=file_object.readline()
            
        #print('################################## PRODUCTS LIST AFTER ADD_PRODUCT METHOD ################################')
        #print(self.products_list)
        file_object.close()
        
    
    def load_orders(self, orders_file):    #read_orders            
        file_object = open(orders_file, "r")                       
        line=file_object.readline()
        while(line!=""):
            order_fields = line.split(",") #split turns string into a list #therefore each line of file is declared as list variable.
            
           
           # both single and multi product orders now take lists so that the initializer can be used for both without added methods.
               
          
            customerID_Or_name = order_fields[0].strip()
            order_date = order_fields [-1].strip()                                 
            productList = []
            for p in order_fields[1: -2: 2]:
                p.strip() 
                productList.append(p)                     
            quantities = []
            for q in order_fields[2: -1: 2]:
                q.strip()
                quantities.append(q)
            an_order = Order(customerID_Or_name, productList, quantities, order_date) 
            #print('###################      AN ORDER        ######################')
            #print(an_order)
            # adds to orders_list Records attribute
            self.add_order(an_order)  
            # the above method should also create an object of record class. Which invokes constructor. Therefore, it makes sense to align an_order with orders constructor. 
            #print('################################   ORDERS LIST  ########################################')
            #print(self.orders_list)
            line=file_object.readline()
            
        #print('##################################LOAD ORDERS METHOD################################')
        #print(self.orders_list)               
        file_object.close()
        
    
    ######FIND METHODS ######
    
    
    def find_customer(self, prompt): #prompt is customer_name or customer_ID
        #print('########## FIND_CUSTOMERS METHOD ########')
        #print('##### PROMPT ######')
        #print(prompt)
        #print('########## self.customers_list ########')
        #print(self.customers_list)
        the_customer = [c for c  in self.customers_list if c.get_customer_name == prompt]  
        #the_customer = next(filter(lambda x: x.customer_ID == prompt or x.customer_name == prompt, self.customers_list), None)
        #print('#### THE CUSTOMER VARIABLE ########')
        #print(the_customer)
        #print(type(the_customer))
        #print(type(the_customer[0]))
        return the_customer     
            
    def find_product(self, prompt): #prompt is product_name or product_ID
        #return next(filter(lambda p: p.product_ID == prompt or p.product_name == prompt, self.products_list), None)
        #print('########## FIND_PRODUCT METHOD ########')
        #print('##### PROMPT ######')
        #print(prompt)
        #print('########## self.products_list ########')
        #print(self.products_list)
        #print('### for i in temp list ######')
        the_product = [c for c  in self.products_list if c.get_product_name == prompt]  
        #print('#### THE PRODUCT VARIABLE ########')
        #print(the_product)
        return the_product 
    
    # caution: This works differently to the previous two find_variables methods
    
    def find_orders(self, prompt): #prompt is product_name or product_ID
        #return next(filter(lambda p: p.product_ID == prompt or p.product_name == prompt, self.products_list), None)
        #print('########## FIND_ORDERS METHOD ########')
        #print('##### PROMPT ######')
        #print(prompt)
        #print('########## self.orders_list ########')
        #print(self.orders_list)
        the_orders_list = [o for o  in self.orders_list if o.get_o_customer == prompt]  
        #the_customer = next(filter(lambda x: x.customer_ID == prompt or x.customer_name == prompt, self.customers_list), None)
        #print('#### THE ORDERS VARIABLE ########')
        #print(the_orders_list)
        return the_orders_list
    ### FORMATTED STRING IN MAIN MENU (no reason)
    
    def existing_member(self, prompt): #prompt is customer_name or customer_ID
        #print('########## EXISITING MEMBER METHOD ########')
        #print('##### PROMPT ######')
        #print(prompt)
        #print('########## self.customers_list ########')
        #print(self.customers_list)
        #print('### for i in temp list ######')
        #for x in self.customers_list:            ###### VERY IMPORTANT. THIS SHOWS THAT LIST RECORDS CAN BE ACCESSED #################
            #print(x)
            #print(x.get_customer_name)
            #print(x.get_customer_name.strip(' '))
            #print(type(x.get_customer_name)) #its a class object
        the_customer_temp_list = [c for c  in self.customers_list if c.get_customer_name == prompt]  
        #print('#### THE CUSTOMER TEMP LIST ########')
        #print(the_customer_temp_list)
        if len(the_customer_temp_list)<1:
            #print('#### CUSTOMER WAS NOT FOUND #####')
            return False
        elif len(the_customer_temp_list)>= 1: ### method doesn't deal with non=unique customers
            the_customer = the_customer_temp_list[0]
            #print('### THE CUSTOMER ######')
            #print(the_customer)
            the_customer_ID = the_customer.get_customer_ID
            #print('### THE CUSTOMER ID ######')
            #print(the_customer_ID)
            #print(the_customer_ID[0][0])
            #print(type(the_customer_ID[0][0]))
            if (the_customer_ID[0][0]) in ['M','V']:
                #print('#### IS A MEMBER OR VIP #####')
                return True    
            else:
                print(prompt, 'IS NOT A MEMEBER OR WAS NOT FOUND #####')
                return False  
             
            
    
    def find_next_customer_number(self):
        temp_customers_list = self.customers_list
        #for i in temp_customers_list:            ###### VERY IMPORTANT. THIS SHOWS THAT LIST RECORDS CAN BE ACCESSED #################
            #print(i)
            #print(i.get_customer_name)
        
        most_recent_cust = temp_customers_list[-1]
        
        most_recent_ID = most_recent_cust.get_customer_ID 
        #print('#### MOST RECENT ID #####')
        #print(most_recent_ID) ## prints correctly
        try:
            most_recent_num_str = most_recent_ID[1:]
            most_recent_num = int(most_recent_num_str)
            #print('###### MOST RECENT NUM VERSION 2 #######')
            #print(most_recent_num)
            #print(type(most_recent_num))
            new_number = most_recent_num + 1
            #print('##### new num #######')
            #print(new_number)
            #print(type(new_number))
            return str(new_number)
        except: 
            print('### UNINDENTIFIED ERROR (find next customer number method')
            
    #product_name_to_ID
    def convert_name_to_ID(self, product_name):
        product_object = self.find_product(product_name)
        converted_ID = product_object[0].get_product_ID
        return converted_ID
    
    def find_product_price(self, product_identifier): #product_name or product_ID
        for p in self.products_list: #iterate through list attribute of objects
            id = p.get_product_ID
            name = p.get_product_name
            if id == product_identifier or name == product_identifier:
                price = p.get_product_price
                return price # should return price of one product at a time. 
    
    
    ### METHODS INVOKED AFTER AN ORDER IS PLACED ####
    
    def add_to_total_spent(self, customer_identifier, order_total): #from place and order method in records class
        customer = self.find_customer(customer_identifier)
        #print(customer_identifier)
        current_total = customer[0].get_total_spent
        new_total = current_total + order_total
        customer[0].set_total_spent = new_total
        
        ## testing different syntaxes 
        
    def subtract_quantity_from_stock(self, product_identifier, quantity):
        product = self.find_product(product_identifier)
        #print(product_identifier)
        quantity = quantity
        new_stock = product[0].get_stock - int(quantity) ## LAST MINUTE ISSUE
        product[0].set_stock = new_stock
        
     ## THIS ADDS TOTAL ORDER COST TO TOTAL SPENT ATTRIBUTE OF CUSTOMER OBJECT IN CUSTOMERS_LIST IN RECORDS CLASS.
    ## THE CUSTOMERS_LIST IS INSTANTIATED IN OPERATIONS MENU VIA RECORDS VARIABLE. 
    def addOrder_to_totalSpent(self, customer_identifier, order_total):
        #print('######### ADDORDER_TO_TOSPENT METHOD  ##############')
        customer = self.find_customer(customer_identifier) #should assign customer tupple to customer variable
        #print('############  CUSTOMER VARIABLE BEFORE LIST METHOD  ################')
        #print(customer)
        list(customer)
        #print('############  CUSTOMER VARIABLE AFTER LIST METHOD  ################')
        #print(customer)
        customer[-1].set_total_spent += order_total
    
        
    
    #### COUNTING METHODS ####
    
    def most_valuable_customer(self):
                
        mvp = max(self.customers_list, key =attrgetter('total_spent'))
        #print('##### MVP IN MOST VALUABLE CUSTOMER ######')
        #print(mvp)
        print('######################################################################')
        print('{x} is the most valuable customer with ${y} spent.'.format(x = mvp.get_customer_name, y = mvp.get_total_spent))
        print('######################################################################')
        
        
    def most_popular_product(self):
        #print('##### MOST POPULAR PRODUCT ########')
        counter_dict = {} 
        for o in self.orders_list: # o is an object
            temp_list = o.productAndQuantity.strip().split(',') 
            print('##### TEMP LIST ######')        
            print(temp_list)
            productlist = []
            print('##### PRODUCT LIST ######')
            productlist.append(temp_list[0])
            print(productlist)
            quantityList = []
            print('##### TEMP LIST INDEX 1 ######')
            print(temp_list[0])
            print('##### QUANTITY LIST ######') ## its a list of strings that represent numbers
            quantityList.append(temp_list[1])
            print(quantityList)  
            
            
            
            dict_to_count =  dict(zip(productlist, quantityList))
            print('#### DICT TO COUNT #######')
            print(dict_to_count.items())
            
            for k, q in dict_to_count.items():
                print('#### QQQQQ (values of dict to count) ######')
                q = int(q)
                print(q)
                print(type(q))
                counter_dict[k] = counter_dict.get(q, 0) + q
            print('#### COUNTER DICT ######')
            print(counter_dict)   
        
        popular_product = max(counter_dict, key=counter_dict.get) #accessing key with max value
        times_purchased = counter_dict[max(counter_dict, key=counter_dict.get)] #accessing max value
        
        print('##################### POPULAR PRODUCT VARIABLE ######################')
        print(popular_product)
        print(times_purchased)
        print('######################################################################')
        print(f'The most popular product is {popular_product}. It has been purchased {times_purchased} times.')
        print('######################################################################')
        return 
            
            
    #product_name_to_ID
    def convert_name_to_ID(self, product_name):
        product_object = self.find_product(product_name)
        converted_ID = product_object[0].get_product_ID
        return converted_ID
    
    def summarize_all_orders(self): ##
        print('#### SUMMARIZE ALL ORDERS #####')
        ## method dictionaries 
        order_num = {}
        orders_by_users = {}
        order_quantity = {}
        
        
        product_namelist = ["P1", "P2", "P3", "P4", "P5", 'P9', 'B10' "P11"]
        print(product_namelist)
        dynamic_product_ID_list = [p.get_product_ID for p in [x for x in self.products_list]]
        
        dynamic_product_names_list = [p.get_product_name for p in [x for x in self.products_list]]
        print(dynamic_product_names_list)
        
        
        
        for order in self.orders_list: #For each order object in orders list
            split_list_quants = [int(i.strip()) for i in order.productAndQuantity.split(",") if i.strip().isnumeric()] #strip and split into list if numeric
            split_list_prods = [i.strip() for i in order.productAndQuantity.split(",") if not i.strip().isnumeric()] #strip and split into list if not numeric
            if order.o_customer not in orders_by_users: #if customer isn't in orders_by_users dict then create key with customer ID and empty dictionary as value.
                orders_by_users[order.o_customer] = {}
                
            for k, v in dict(zip(split_list_prods, split_list_quants)).items(): # for key and value (product_ID, quantity) in dict created via zipping two lists
                if k in orders_by_users[order.o_customer]: # if product_ID in orders by users dict 
                    orders_by_users[order.o_customer][k] = orders_by_users[order.o_customer][k] + v #then add product quantity to that the product keys value
                else:                                                                       ## by doing this, it loops through all objects in the orders_list
                    orders_by_users[order.o_customer][k] = v                            ## and adds the quantity of each product to that product's key in the
                                                                                    ## orders_by_users dictionary.                                                                              
                #here im making for order_num
                if k not in order_num:
                    order_num[k] = 0
                if v > 0:
                    order_num[k] += 1
          
                if k in order_quantity:
                    order_quantity[k] += v
                else:
                    order_quantity[k] = v  
                    
                    for p in dynamic_product_names_list:  #### this was the cause of the bundles missing from the order summary count and quantity 
                        if p not in order_num.keys():     #### essentially I added the products with no count to the dict. 
                            order_num[p] = 0
                        if p not in order_quantity.keys():
                            order_quantity[p] = 0
                                                                                    
        
        
        #### CONVERTION LOOP FOR ORDERS BY USERS DICT #######
        print('#### CONVERTION LOOP FOR ORDERS BY USERS DICT #######')
        for customer, v in orders_by_users.items():
            print(customer)
            if isinstance(v, dict):
                temp_dict = {}
                for x, y in v.items(): 
                    #print(type(x))
                    #print(x, '<<------- VAR X in V (of C,V in orders_by_users.items')
                    ID = self.convert_name_to_ID(x)
                    temp_dict[ID] = y
                    orders_by_users[customer] = temp_dict
                    #print(x, '<<------- NEW VAR X in V (of C,V in orders_by_users.items')
            else: 
                print('###### ERROR #######')
        
        
        ###IMPORTANT LESSON HERE ABOUT REPLACING DICTIONARY KEYS.####
        #### THEY POINT TO A DICTIONARY VALUE in this case that value is a string but I cannot convert a dictionary key the same way as a string ######
        
        #print('######### FORMATTING OF SUMMARIZE ALL ORDERS METHOD ###################')
        print('\t'+'\t'.join([p.get_product_ID for p in self.products_list])) # this prints the first line  
        print('-'*(15+8*len(orders_by_users.values()))*3)
        for c, v in orders_by_users.items():
            str_to_print_str = c
  
            for prod in dynamic_product_ID_list:
                str_to_print_str = f'{str_to_print_str}\t{str(v.get(prod, 0))}'.format(str_to_print_str, str(v.get(prod, 0)))
            print(str_to_print_str)
            print()
        
        
        print('-'*(15+8*len(orders_by_users.values()))*3)
        print('Ord#\t'+'\t'.join([str(order_num[p]) for p in order_num]))
        print('OrdQ\t'+'\t'.join([str(order_quantity[p]) for p in order_quantity]))    
        
        
        
        
        
        ###### LIST METHODS (RECORDS CLASS) #######
        
    def list_customers(self):
        #print('##########################list_customers_method######')
        #print(self.customers_list, 'list_customers method')
        #print('############## LIST OF EXISTING CUSTOMERS ########################')
        for c in self.customers_list: ###list of objects, hence difference
            print(c)
            
    def list_products(self):
        #print('##########################list_products_method######')
        #print(self.products_list, 'list products method')
        #print('############## LIST OF EXISTING PRODUCTS ########################')
        for p in self.products_list:
            print(p)
            
    def list_orders(self):
        #print('##########################list_orders_method######')
        #print(self.orders_list, 'list orders method')
        #print(self.orders_list[0].productAndQuantity)
        #print(type(self.orders_list[0].productAndQuantity), '### TYPE(PRODUCTANDQUANTITY) ######')
        #print('############## LIST OF ALL PAST ORDERS ########################')
        for o in self.orders_list:
            print(o)
            
    #### Save method ####
    
    def save_to_file(self):   
        customers_file = open(self.customers_file, "w")
        customers_file.write('\n'.join([str(c) for c in self.customers_list])) #turns customers_list attribute into a line by line string
        customers_file.close()
        products_file = open(self.products_file, "w")
        products_file.write('\n'.join([str(p) for p in self.products_list])) #the iterable is a list comprehension
        products_file.close()
        orders_file = open(self.orders_file, 'w')
        orders_file.write('\n'.join([str(o) for o in self.orders_list]))
        orders_file.close()
            
                 
##################################################################################      CLASS ORDER       ######################################################################################


class Order():

    
    order_date = datetime


    ## customer methods
    @property
    def get_o_customer(self):
        return self.o_customer  

    @get_o_customer.setter
    def set_o_customer(self, prompt): #prompt is customer name or ID
        self.o_customer = prompt    

    ## product methods   
    @property
    def get_o_products_list(self):
        return self.o_products_list 

    @get_o_products_list.setter
    def set_o_products_list(self, updated_product_list):
        self.o_products_list = updated_product_list

    def add_to_products_list(self, a_product):
        self.o_products_list.append(a_product)  

    ## quantites methods
    @property
    def get_o_quantities_list(self):
        return self.o_quantities_list   

    @get_o_quantities_list.setter
    def set_o_quantities_list(self, updated_list):
        self.o_quantities_list = updated_list

    def add_quantity(self, quantity): 
        self.o_quantities_list.append(quantity)

    ## price methods    
    @property
    def get_unit_price_list(self):
        return self.unit_price_list
    
    @get_unit_price_list.setter
    def set_unit_price_list(self, list): #list is updated unit price list
        self.unit_price_list = list


    def add_order(self, order_object):
        self.orders_list.append(order_object)

    ## Constructor method 
    def __init__(self, identifier, productList, quantities, order_date):                                        
        self.o_customer = identifier #accept name or id          
        productAndQuantity_list = Tools.combine_2_lists(productList, quantities) 
        self.date = order_date ##order_date must always be defined before Order class is declared. 
        self.productAndQuantity = ','.join([str(i) for i in productAndQuantity_list])
        #print('###### SELF ORDER INIT ######')
        #print(self)
        
    def __str__(self):
        return ', '.join([str(i) for i in [self.o_customer, self.productAndQuantity, self.date]]) 
    
    
    def __repr__(self) -> str:
        return f"({self.o_customer}, {self.productAndQuantity}, {self.order_date})"
            
###########################################################################     TOOLS CLASS        #######################################################################################
class Tools():
            
    #TOOLS 
    @staticmethod
    def sum_list(prompt): # prompt is a list
        print('#### PROMPT VAR IN SUM LIST METHOD ######')
        print(prompt)
        sum = 0
        for x in prompt: 
            sum += x
        print('########### SUM VAR ##########')
        print(sum)
        return sum
    
    @staticmethod                                      
    def combine_2_lists(list1, list2): 
        combined_list = [item for pair in zip(list1, list2 + [0]) for item in pair]
        return combined_list
    
    @staticmethod   
    def combine_3_lists(list1, list2, list3):
        combined_list = list(zip(list1, list2, list3))
        return combined_list
    
    
    
    ###### VALIDATION METHODS ######
    
    
    @staticmethod
    def float_inputValidation(display_message, validator_function, error_message):
        user_input = float 
        while True: 
            user_input = float(input(display_message))
            if validator_function(user_input):
                break
            else:
                print(error_message)
        return user_input
            
    @staticmethod
    def string_inputValidation(display_message, validator_function, error_message):
        user_input = '' 
        while True: 
            user_input = input(display_message)
            if validator_function(user_input): ### if validator function returns true
                break
            else:
                print(error_message)
                print('##### USER INPUT #######')
                print(user_input)
                print(type(user_input))
        return user_input
    
    @staticmethod
    def integer_inputValidation(display_message, validator_function, error_message):
        user_input = int
        while True: 
            user_input = input(display_message)
            if validator_function(user_input):
                break
            else:
                print(error_message)
        return user_input
     
    @staticmethod
    def is_positive_integer(prompt):
        r = False
        try:
            x = int(prompt)
            if x > 0: 
                r = True
        except:
            r = False
        return r

    @staticmethod
    def is_positive_float(prompt):
        r = False
        try:
            x = float(prompt)
            if x > 0: 
                r = True
        except:
            r = False
        return r

############################################################################    OPERATIONS UI CLASS     #################################################################################################



class OperationsUI(): # menu
    

    date_format = '%d/%m/%Y %H:%M:%S'

    def main(self, argv): 
        if not argv: argv = ['customers.txt', 'products.txt', 'orders.txt']
        if len(argv) not in (0, 2, 3):
            sys.stdout.write('Illegal number of file arugments.\n')
            sys.stdout.write(f'USE: {os.path.basename(__file__)}\n')
            sys.stdout.write(f'    OR {os.path.basename(__file__)} [customers_file] [products_file]\n')
            sys.stdout.write(f'    OR {os.path.basename(__file__)} [customers_file] [products_file] [orders_file]\n')
            exit()

        print('####################################################################### HELLOOOO ##############################################################################')
        sys.stdout.write('\n \n \n')
        
        records = Records(*argv) #instantiates a record object which can be accessed via records.attribute
        
        
        #print('################################## AUTO LOADED LISTS################################')
        #print(records.customers_list,'############customers_list##########','\n, \n, \n', records.products_list, '###########products_list#########', '\n \n \n', records.orders_list, '##############records_list##########')
        sys.stdout.write('\n \n \n')
        
        sys.stdout.write('Welcome to the retail management system!\n')
        
        menu_reference_main = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        
        while True:
            sys.stdout.write('\r\n###############################################################\n')
            sys.stdout.write('CHOOSE FROM THE FOLLOWING OPTIONS:\n')
            sys.stdout.write('1: PLACE ORDER\n')
            sys.stdout.write('2: DISPLAY EXISTING CUSTOMERS\n')
            sys.stdout.write('3: DISPLAY EXISING PRODUCTS\n')
            sys.stdout.write('4: ADJUST VIP DISCOUNT (for all)\n')
            sys.stdout.write('5: ADJUST VIP THRESHOLD (for all)\n')
            sys.stdout.write('6: DISPLAY ALL ORDERS\n')
            sys.stdout.write('7: DISPLAY ALL ORDERS (of a customer)\n')
            sys.stdout.write('8: SUMMARIZE ALL ORDERS\n')
            sys.stdout.write('9: DISPLAY MOST VALUABLE CUSTOMER\n')
            sys.stdout.write('10: DISPLAY MOST POPULAR PRODUCT\n')
            sys.stdout.write('0: EXIT THE PROGRAM\n')
            sys.stdout.write('###############################################################\r\n')

            
            choice = Tools.string_inputValidation('Choose an option:', lambda x: x in menu_reference_main, 'Please enter a valid option!') 
           
            
            ### MENU CHOICE IF STATMENTS ####
            if  choice == '1':
                #print('waypoint 1') 
                #print(records.customers_list)
                self.place_an_order(records)
                #print('################################# WAYPOINT AFTER place_an_order method (choice 1) ######################') 
                
            elif choice == '2':
                #print('waypoint 2')
                records.list_customers() #i think this is correct as self says Tools does not have the method
                
            elif choice == '3':
                #print('waypoint 3')
                records.list_products()
            
            
            elif choice == '4':
                #print('waypoint 4')# verify if this the right syntax for multiple lambda conditions. 
                new_vip_rate = Tools.float_inputValidation('Enter new VIP discount rate (float).', lambda x: Tools.is_positive_float(x), 'Enter a FLOAT that is 0 or greater.')
                #print("##### VIP DISCOUNT ########")
                #print(VIPMemeber.get_discount_rate())
                VIPMemeber.adjust_vip_discount(new_vip_rate)
                #print("##### NEW VIP DISCOUNT ########")
                #print(VIPMemeber.get_discount_rate())
                
                
            elif choice == '5':
                print('waypoint 5')
                new_threshold = Tools.integer_inputValidation('Enter new VIP threshold (integer).', lambda x: Tools.is_positive_integer(x), 'Enter an INTGER greater than 0.' )
                print("##### VIP THRESHOLD ########")
                print(VIPMemeber.vip_threshold)
                VIPMemeber.adjust_vip_threshold(new_threshold)
                print("##### NEW VIP THRESHOLD ########")
                print(VIPMemeber.vip_threshold)
                VIPMemeber.display_customer_attributes()
                
                  
            elif choice == '6':
                print('waypoint 6')
                print("##### PRINT ALL ORDERS (MAIN MENU) ########")
                print(records.orders_list)
                #print(records.list_orders())
                records.list_orders()
            
            
            elif choice == '7':
                print('waypoint 7')
                print("##### DISPLAY ALL ORDERS OF A CUSTOMER ########")                                        
                customer_identifier = Tools.string_inputValidation('Enter customer name or ID', lambda x: records.existing_customer(x) , 'Not a valid customer.')
                is_customer = records.find_customer(customer_identifier)
                records.find_orders(is_customer)
                print('#### IS CUSTOMER VARIABLE main_method')
                print(is_customer)
                print ('#### CUSTOMER IDENTIFIER IN main_method ######')
                print(customer_identifier)
                the_orders_list = records.find_orders(customer_identifier)
                print('_______________________________________________________________________________________________________________')
                print()
                print('BELOW ARE ALL OF THEIR ORDERS.')
                print('_______________________________________________________________________________________________________________')
                for o in the_orders_list:
                    print(o)
                print('_______________________________________________________________________________________________________________')
                
            
            elif choice == '8':
                print('waypoint 8')
                print("##### SUMMARIZE ALL ORDERS ########") 
                records.summarize_all_orders()  
            
            
            elif choice == '9':
                print('waypoint 9')
                print("##### MOST VALUABLE CUSTOMER ########") 
                records.most_valuable_customer() 
            
            
            elif choice == '10':
                print('waypoint 10')
                print("##### MOST POPULAR PRODUCT ########") 
                records.most_popular_product() 
                
            
            elif choice == '0':
                print('waypoint 11')
                print("##### BEFORE SAVE TO FILE AND EXIT ########") 
                records.save_to_file() 
                print('waypoint 12')
                exit()
                
            else:
                print('###### ERROR Skipped menu if statements #########')
                
    menu_reference_main = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    
    ##MAIN MENU METHODS
    
    def place_an_order(self, records): #customers_file, products_file, orders_file):
        
        ### ORDER VARS ####
        temp_productsList = []
        temp_quantitiesList = []
        order_total = 0
        
        customer_identifier = Tools.string_inputValidation('Enter customer name.', lambda x : x is not x.isnumeric(), 'Error. Try again.\n Enter customer name without numbers.') ## lamba is redundant here. Just filler.
        
        ##### ORDER/REORDER LOGIC #####
        another_product = 'y'
        while True:
            
            print('##### PRODUCT SELECTION LOGIC ######')
            product_identifier = Tools.string_inputValidation('Enter product ID or Name', lambda x: x in [y.get_product_name or y.get_product_ID for y in records.products_list] , 'Enter a valid product ID or Name.')
            print(product_identifier)
            temp_productsList.append(product_identifier)
            print(temp_productsList)
            print('#### TEMP PRODUCTS LIST ####')                                                   #no logic for stock comparison 
            product_quantity = Tools.integer_inputValidation('Enter product quantity (integer).', lambda x: Tools.is_positive_integer(x) ,'Invalid input. Please enter product quantity (Integer).')
            print('#### PRODUCT QUANTITY #####')
            print(product_quantity) 
            temp_quantitiesList.append(product_quantity)
            print('#### TEMPT QUANTIES LIST')
            print('##### ANOTHER PRODUCT ######')
            another_product = Tools.string_inputValidation('Do you want to purchase another product? (y or n)', lambda x: x in ['y', 'Y', 'n', 'N'] ,'Try again. Enter y or n')
            print(another_product)
            if another_product in ['n', 'N']:
                break
            
            #loop works, it reaches here
            
         
       
        
         ### create dictionary logic for products and quantities 
        print('####### DICTIONARY LOGIC FOR STOCK #########')
        stock_dict = dict(zip(temp_productsList, temp_quantitiesList))
        print(stock_dict.items())
        print(str(stock_dict)) # CORRECT. IT IS A DICT
        
        ####### REMOVES STOCK #######
        for k,v in stock_dict.items():
            records.subtract_quantity_from_stock(k, v)
        
        ###### CREATES PRICE LIST ######
        price_list = []
        for c, v in stock_dict.items():
            print('#### C IN PRICES LOOP #####')
            print(c)
            print('##### V IN PRICES LOOP #####')
            print(v)
            z = records.find_product_price(c)
            v = float(v)
            x = z * v
            print('#### Z IN PRICES LOOP #####')
            print(z)
            price_list.append(x)
        
        ### SUMMING TO TEMP PRICE ###
        temp_total = Tools.sum_list(price_list) ## sum list works. But there is no price information
        print('##### TEMPT TOTAL ########')
        print(temp_total)  
        
        
        ### MEMBERSHIP LOGIC
        is_member = (records.existing_member(customer_identifier)) ## returns True for Harry
        print('###### IS MEMBER VARIABLE ###########')
        print(is_member)
        if is_member == False:
            ask_to_join = Tools.string_inputValidation('Do they want to join? Enter y or n (e.g y = yes)', lambda x: x in ['n','N','y','Y'], 'Error. Try again.\n Enter y or n.')
            sign_up = records.sign_up(ask_to_join) #method returns boolean
            print('#### SIGN UP VARIABLE  #######')
            print(sign_up)
            if sign_up == True: 
                membership_type = Tools.string_inputValidation('Choose Membership type. Enter m or v (e.g v = vipmember)', lambda x: x in ['v', 'V', 'm', 'M'], 'Error. Try again.\n Enter v or m.')
                print('#### MEMBERSHIP TYPE ######')
                print(membership_type)
                if membership_type in  ['v', 'V']:
                    membership_num = records.find_next_customer_number()
                    customer_ID = 'V'+ str(membership_num) #creates new VIP ID (e.g V14)
                    print('############### CUSTOMER ID VARIABLE (in place and order method) (if V)   ###############')
                    print(customer_ID)
                    normal_sign_up = False
                    print('normal_sign_up', normal_sign_up)
                elif membership_type in ['m', 'M']:
                    membership_num = records.find_next_customer_number()
                    customer_ID = 'M'+ str(membership_num) #creates new Member ID (e.g V15)
                    print('############### CUSTOMER ID VARIABLE (in place and order method) (if M)   ###############')
                    print(customer_ID)
                    normal_sign_up = True
                    print('normal_sign_up', normal_sign_up)
                else:
                    print('###### UNIDENTIFIED ERROR ##########')
            if sign_up == False: # ARRY NOT SIGNGING UP GOES THROUGH HERE
                print('##### IF SIGNUP FALSE and is member FALSE ##################')  ##### LILY GOES THROUGH HERE (NOT MEMBER AND NOT SIGNUP)
                is_customer_temp = records.existing_customer(customer_identifier) ## returns 
                if is_customer_temp == True: ## if customer is in records, then they have ID already
                    cust_obj_list = records.find_customer(customer_identifier)
                    cust_obj = cust_obj_list[0]
                    customer_ID = cust_obj.get_customer_ID
                    pass ### LILY PASSES AS SHE IS A CUSTOMER THEREFORE CUSTOMER ID IS NOT ASSIGNED FOR LILY
                else:                        ## if not create new customer ID (e.g C23). 
                    membership_num = records.find_next_customer_number()
                    print('##### MEMBERSHIP NUMBER (after  variable ##################')
                    print(membership_num)
                    customer_ID = 'C' + membership_num
                    print('############### CUSTOMER ID VARIABLE (in place and order method) (if M)   ###############')
                    print(customer_ID)
                    
        ## is_member will be used again.        
        elif is_member == True:         
                print('#### IS MEMBER TRUE code block #######')
                member_is_vip = records.member_is_VIP(customer_identifier)
                print('#### MEMBER IS VIP #####')
                print(member_is_vip)
                customer_temp = records.find_customer(customer_identifier)
                customer_ID = customer_temp[0].get_customer_ID[0]
                
                
        else: 
            print('###### ERROR (IS MEMBER MUST BE TRUE OR FALSE) #########')
        
       
         
        ### SAVE, UPDATE, ADD CUSTOMER LOGIC #####
        print('### SAVE, UPDATE, ADD CUSTOMER LOGIC #####')
        

        ### IS NEW CUSTOMER referenced later in block.
        not_new_customer = records.existing_customer(customer_identifier)
        print('#### IS NOT NEW CUSTOMER VAR (main_method)')
        print(not_new_customer)
        
        print('##### AFTER NOT NEW CUSTOMER VAR ##################')
        
        print('##### IF EXISTING CUSTOMER #########')
        #if existing customer
        if not_new_customer:
        #cust_obj = records.find_customer(customer_identifier)
         #   if not sign_up: 
          #      c = cust_obj[0]
           #     customer_ID = c.get_customer_ID
                customer_ID = customer_ID
                if customer_ID[0] in ['v', 'V']:
                    premium_rate = VIPMemeber.get_premium_rate()  ###ISSUE maye I can't assign a class property/attribute to a variable?
                    print(premium_rate)
                    print(str(premium_rate))
                    #premium_rate = x.get_premium_rate()
                    print(premium_rate)
                    discount_rate = VIPMemeber.get_discount_rate()
                    print(discount_rate)
                    order_total = temp_total * (1 - premium_rate) if (temp_total > 1000) else temp_total * (1 - discount_rate)
                    records.add_to_total_spent(customer_identifier, order_total)
                    z = records.find_customer(customer_identifier) #ID or name works
                    a_customer = z[0] # assumes above method returns list with an object
                elif customer_ID[0] in ['m', 'M']:
                    discount_rate = Member.get_discount_rate()  ### THE ISSUE WITH WILSON IS that even though he is a member, I might be retrieving the value. 
                    print(discount_rate)
                    order_total = temp_total * (1 - discount_rate)
                    records.add_to_total_spent(customer_identifier, order_total)
                    z = records.find_customer(customer_identifier) #ID or name works
                    a_customer = z[0] # assumes above method returns list with an object
                    print('#### CUSTOMER VARIABLE FOR EXISTING MEMBERS ######')
                    print(a_customer)
                elif customer_ID[0] in ['c', 'C']:
                    discount_rate = 0
                    order_total = temp_total
                    records.add_to_total_spent(customer_identifier, order_total)
                    z = records.find_customer(customer_identifier) #ID or name works
                    a_customer = z[0] # assumes above method returns list with an object
                else: 
                    print('#### ERROR sign up should not reach else statement')
        
        # if new customer 
        elif not not_new_customer:
                print('###### IF NEW CUSTOMER SECTION ########')
               
                if customer_ID[0] in ['v', 'V']:
                    order_total = temp_total * (1 - VIPMemeber.__premium_rate) if (temp_total > 1000) else temp_total * (1 - VIPMemeber.get_discount_rate())
                    discount_rate = VIPMemeber.get_discount_rate()
                    a_customer = VIPMemeber (customer_ID, customer_identifier, VIPMemeber.get_discount_rate(), order_total)
                    records.add_customer(a_customer)
                    
                elif customer_ID[0] in ['m', 'M']:
                    order_total = temp_total * (1 - (Member.get_discount_rate()))
                    discount_rate = Member.get_discount_rate()
                    a_customer = Member(customer_ID, customer_identifier, Member.get_discount_rate(), order_total) # self discount rate might be an issue
                    records.add_customer(a_customer)
                    
                elif customer_ID[0] in ['c', 'C']:
                    order_total = temp_total
                    discount_rate = Customer.get_discount_rate()
                    a_customer = Customer(customer_ID, customer_identifier, discount_rate, order_total)
                    records.add_customer(a_customer)
                    
                
                else: 
                    print('#### ERROR sign up should not reach else statement')
                
                
                
        #print('###### ORDER IS INSTANTIATED AND ADDED TO ORDERS LIST ############')
        #print('### CUSTOMER IDENTIFIER #####')
        #print(customer_identifier)
        this_order = Order(customer_identifier, temp_productsList, temp_quantitiesList, order_date = datetime) #object
        #print('##### THIS ORDER OBJECT VARIABLE IN PLACE AN ORDER METHOD (BEFORE ADDING ORDER TO ORDERS LISTS  ###################')
        #print(this_order)
        #print(type(this_order))
        records.add_order(this_order)
        
        ## I think I can add order now because it's not impacted by type of member except in regards to customerID but that variable has already been declared. 
        ## furthermore, the orders list is referenced and that is all that is relevant for the records class. 
        
            
       
        #PRINT TRANSACTION LOGIC
        print('\r\n----------------------------------------')
        for v in range(len(temp_productsList)):
            print(f'{a_customer.customer_name} purchases {temp_productsList[v]} x {temp_quantitiesList[v]}') #should loop through starting at index 0 to end
            product_obj_list = records.find_product(temp_productsList[0]) # assumes method returns list
            product_obj = product_obj_list[0] 
            price = product_obj.get_product_price
            print('Unit price:\t\t{0:>13}'.format(f'{float(price):.1f} (AUD)'))
        if a_customer.get_customer_ID[0] in ['v', 'V']:
            print('Membership price:\t{0:>13}'.format(f'{VIPMemeber.vip_fee:.1f} (AUD)'))  
        elif a_customer.get_customer_ID[0] in ['M', 'm']:                             ### ISSUE NOT PRINTING MEMEBERSHIP LINE FOR ARRY
            print('Membership fee:\t{0:>13}'.format(f'{Member.member_fee:.1f} (AUD)')) 
        print('----------------------------------------')#1:>7.1%
        print(f'{a_customer.get_customer_name} gets a discount of {discount_rate}.') ### might be issue here becasue of how different customer discounts are implemented
        print('Total price:\t\t{0:>13}'.format(f'{order_total:.1f} (AUD)'))
        print('----------------------------------------')    
        
        
        
        print('################################################################# REACHES END ############################################################################################')
        return
      
            
    
        
        
        
        
        
  
  

##RUNNS PROGRAM

if __name__ == "__main__": ### if this is file being run directly (not being imported)
    print('######## SYS.ARGV #########')
    print(sys.argv)
    #time.sleep(20)
    menu = OperationsUI()
    menu.main(sys.argv[1:])
    