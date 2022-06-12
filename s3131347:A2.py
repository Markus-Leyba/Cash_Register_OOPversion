
from datetime import datetime
from re import X
from sys import argv
import sys
import sys
import os
import datetime
import time

CUSTOMERS_FILES = 'Assignment2/customers.txt'
PRODUCTS_FILE = 'Assignment2/products.txt'
ORDERS_FILE = 'Assignment2/orders.txt'

#sys.setrecursionlimit(10**6)


                     #Note: In this program because it's designed to match HD file output variable can always be found in their geometric position
                                      #in the file. E.g total_spent can always be found in customer_list[X][-1] because it will always be the last one for that list. 
                                      #similarly, customer_ID will always be customer_list[x][0] and customer_name is customer_list[X][1]. By referencing these as 
                                      #predictable way points, we can derrive other attributes. 
                                      #for example, with orders, the start and end indexes are always stable, we can therefore isolate a range of attributes
                                      #e.g product_id and quantities occur in an alternating pattern between two indexes. 
                                      #this holds true within a method.
                                      #Important question: does this hold true outside of a method? For example is there an index order to an object? Or is it like a #dictionary? Answer: Python class object instances use 'namespaces'. A name is related to an object. It's relationship with the 
                                      #object defines its scope. In other words, it's not indexed. It's like a dictionary. Also, dictionaries use name spaces. 
                                      #conclusion: it is great and fine to use geometrical equivalence within a scope of a method but it will get messy if this is relied upon outside of a method. Because to find something, there needs to be an intermediate method to get the positions of relevant items. Therefore, I think I'll stay away from list comprehension when assigning variables to another method. 
 
 
 
################################################################################# CUSTOMER CLASS ####################################################################################################
       
       
                                      
class Customer():
     
    customer_ID = ''
    
    customer_name = ''
    
    discount_rate= 0.00
    
    total_spent = 0


    def __init__(self, customer_ID, customer_name, discount_rate, total_spent): 
        self.customer_ID = customer_ID                                          
        self.customer_name = customer_name                                       
        self.discount_rate = discount_rate                                      
        self.total_spent = total_spent
        

    def __str__ (self):
        return ', '.join([str(i) for i in [self.customer_ID,self.customer_name,self.discount_rate,self.total_spent]]) 
    
    def __repr__(self) -> str:
        return f"({self.customer_ID}, {self.customer_name}, {self.discount_rate}, {self.total_spent}"
    
    @property
    def get_customer_ID(self):
        return self.customer_ID
    
    @property
    def get_customer_name(self):
        return self.customer_name
    
    @property    ## issue: not sure if I should use static variables here. NO unless i have a solid reason. 
    def get_discount_rate(self):
        return self.discount_rate
    
    @get_discount_rate.setter             ### THIS ALLOWS ME TO CHANGE DISCOUNT RATES OF ALL CUSTOMERS. 
    def set_discount_rate(self, new_rate):
        self.discount_rate = new_rate #reminder: setters don't need return statement.
        
    @property
    def get_total_spent(self):
        return self.total_spent
    
    @get_total_spent.setter               ### THIS ALLOWS ME TO ADD ORDER TOTAL TO TOTAL SPENT FROM ORDERS/OPERATIONS CLASS
    def set_total_spent(self, order_total): #order_total will come from order class
        self.total_spent = self.total_spent + order_total
        
     
     
##############################################################################  MEMBERS  ################################################################################################
     
     
     
class Member(Customer):
    discount_rate = 0.05 # ISSUE premise: overriding of inheritance means that even if discount rate is changed by a
                         # static method, it won't override the Member Class. 
    def __init__(self, customer_ID, customer_name, discount_rate, total_spent):
        self.customer_ID = customer_ID
        self.customer_name = customer_name
        self.discount_rate = discount_rate
        self.total_spent = total_spent

    def __str__(self):
        return ', '.join([str(i) for i in [self.get_customer_ID,self.get_customer_name,self.discount_rate,self.get_total_spent]])
    
    def __repr__(self) -> str:
        return f"({self.customer_ID}, {self.customer_name}, {self.discount_rate}, {self.total_spent}" ## potential issue with not using get_
    
    
    #########################################################################  VIP MEMBERS  ############################################################################################
 
    
class VIPMemeber(Customer):
    discount_rate = 0.15
    vip_gap = 0.05
    __premium_rate = 1 * (1 - float(discount_rate + vip_gap)) ### assumes the gap between rates will always be the same.
    vip_threshold = 1000
    
    def __init__(self, customer_ID, customer_name, discount_rate, total_spent):
        self.customer_ID = customer_ID
        self.customer_name = customer_name
        self.discount_rate = discount_rate
        self.total_spent = total_spent
        print('########### VIP INIT ###################')
        print(self)
        
        
    def __str__(self):
        print('########### VIP STR ###################') 
        return ', '.join([str(i) for i in [self.get_customer_ID,self.get_customer_name,self.discount_rate,self.get_total_spent]]) 
        
    def __repr__(self) -> str:
        return f"({self.get_customer_ID}, {self.get_customer_name}, {self.discount_rate}, {self.get_total_spent}"
        
    @staticmethod               ### Note to self: python works on assignment so it won't change other variables.
    def adjust_vip_threshold(new_threshold):
        vip_threshold = new_threshold
        return vip_threshold
    
        
    @property
    def get_premium_rate(self):  ### premium rate is private attribute. 
        return self.__premium_rate
    
    @property
    def get_vip_discount(self):
        return self.discount_rate
    
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
        return f"({self.__product_ID}, {self.__product_name}, {self.product_price}, {self.__stock}"
    
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
    def get_stock (self, product_quantity): ### product_quantity will be an attribute of orders class
        self.stock = self.__stock - product_quantity
    
    ## RIGHT NOW I CAN'T SEE THE POINT OF USING ANY MORE METHODS.
    ## I ENVISION REFERENCES TO BE KEPT IN THE RECORDS CLASS AND/OR IN THE FILES WHICH WILL BE ACCESSE VIA RECORDS CLASS. 
    ## SO THE DESIGN DECISION HERE IS TO KEEP PRODUCT CLASS ONLY RELEVANT TO HOW PRODUCTS AS A CUSTOM DATA TYPE WILL BE APPLIED TO RECORD LISTS. 
    

################################################################################   BUNDLE SUBCLASS    ####################################################################################
    
    
class Bundle(Product):
    
    
                                                                                        # note that the fourth parameter needs to be a list. 
    def __init__(self, product_ID, product_name, product_ID_list, bundle_price, stock): #changed the order or parameters to suite products.txt  
         
        super().__init__(product_ID, product_name, bundle_price, stock)
        self.bundled_products_list = ','.join([str(i) for i in product_ID_list]) 
        print('####### BUNDLE SELF #######')
        
        
    def __str__(self):
        return ', '.join([str(i) for i in [self.get_product_ID, self.get_product_name, self.bundled_products_list, self.get_stock]])
    
    def __repr__(self) -> str:
        return f"({self.get_product_ID}, {self.get_product_name}, {self.bundled_products_list}, {self.get_stock}"
        
    def find_product(self,prompt):
        return next(filter(lambda p: p.product_ID == prompt or p.product_name == prompt, self.products_list), None)
        
        
#####################################################################             RECORDS CLASS                        #########################################################################

## STRUCTURE of the records class constructor means that it will load the 3 records lists from files
## except for orders which is optional. What does this means for the save_data method in records clas?
## it means that the attributes are already formatted appropriately and this implies that when saving data to a file there is no
## no need to reformat it. ## By this logic it also implies that any issues exist and should be resolved in the formatting of the data
## BEFORE it has been saved in the different records lists. (unless it's a simply issue in the save_data method)

class Records():
    
    customers_list = []
    products_list = []
    orders_list = []
                                                        
     ###these parameters will correlate with the structure of inputs in load_products/load_customers/load_orders methods in the records/operations section.                                                   
    def __init__(self, customers_file, products_file, orders_file = None):  
        self.customers_file = customers_file              
        self.products_file = products_file
        self.orders_file = orders_file if orders_file is not None else 'Assignment2/orders.txt'
        if orders_file:
            self.load_orders(orders_file) ### THESE THREE METHODS IN RECORDS CLASS
        self.load_customers(customers_file)
        self.load_products(products_file)
    
    def __str__(self):
       return ', '.join([str(i) for i in [self.customer_list, self.products_list, self.orders_list]])
    
    def __repr__(self) -> str:
        return f"({self.customer_list}, {self.products_list}, {self.orders_list}"
    
    
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
    
    @get_products_list.setter         ### REPLACES WHOLE LIST
    def set_products_list(self, updated_products_list):
        self.customer_list = updated_products_list
    
    def add_product(self, a_product): ### ADDS A SINGLE PRODUCT
        self.products_list.append(a_product) # operator won't work. Use apphend instead. 
    
    @property
    def get_orders_list(self):
        return self.orders_list
    
    @get_orders_list.setter         ### REPLACED WHOLE LIST 
    def set_orders_list(self, updated_orders_list):
        self.orders_list = updated_orders_list
        
    def add_order(self, an_order):  ### ADDS A SINGLE ORDER
        self.orders_list.append(an_order) 
    
    ## THIS ADDS TOTAL ORDER COST TO TOTAL SPENT ATTRIBUTE OF CUSTOMER OBJECT IN CUSTOMERS_LIST IN RECORDS CLASS.
    ## THE CUSTOMERS_LIST IS INSTANTIATED IN OPERATIONS MENU VIA RECORDS VARIABLE. 
    def addOrder_to_totalSpent(self, customer_identifier, order_total):
        print('######### ADDORDER_TO_TOSPENT METHOD  ##############')
        customer = self.find_customer(customer_identifier) #should assign customer tupple to customer variable
        print('############  CUSTOMER VARIABLE BEFORE LIST METHOD  ################')
        print(customer)
        list(customer)
        print('############  CUSTOMER VARIABLE AFTER LIST METHOD  ################')
        print(customer)
        customer[-1] = float(customer[-1]) + order_total
        
        
    #### VALIDATOR METHODS ######
    
    def existing_customer(self, customer_identifier):
        customer = self.find_customer(customer_identifier) # returns tupple. 
        if customer: # empty tupple is false, otherwise it's true. 
            return True
        else:
            return False
    
    def existing_member(self, customer_identifer): ## in this case it will be name. 
        customer = self.find_customer(customer_identifer)
        print('########   CUSTOMER VARIABLE (in existing_member method)  ##################')
        print(customer)
        if customer[0][0] == 'P'| customer[0][0] == 'M':
            return True
        elif not customer:
            return False
        else:
            print('###### UNIDENTIFIED ERROR (EXISING_MEMBER METHOD) ############')
            
    def sign_up(self, str): ## str is input should be y or n Or Y or N
        answer = str
        if answer == 'n' | answer == 'N':
            return False
        if answer == 'y' | answer == 'Y':
            return True            
            
            
    ##### AUTO LOADING METHODS #####        
    
    def load_customers(self, customers_file): #read_customer  
        file_object=open(customers_file, "r")
        i=0
        line=file_object.readline()
        while(line!=""):
            customer_fields=line.split(",")
            customer_ID=str(customer_fields[0])
            customer_name=str(customer_fields[1])
            discount_rate=float(customer_fields[2])
            total_spent=float(customer_fields[3])
            a_customer = Customer(customer_ID, customer_name, discount_rate, total_spent) 
            self.add_customer(a_customer)
            line=file_object.readline()
            i+=1
        print('##################################LOAD CUSTOMERS METHOD################################')
        print(self.customers_list)
        file_object.close()
        
            
    
    def load_products(self, products_file): #read_products       
        print('##################################LOAD PRODUDUCTS METHOD################################')
        file_object=open(products_file, "r")                     
        i=0                                                       
        line=file_object.readline()
        while(line!=""):
            product_fields = line.split(",") #should already be a list here. Because of split. 
            print('#########product_fields#########')
            print(product_fields)
            print('#### product_fields [0] ########')
            print(product_fields[0])
            if (product_fields[0][0] == 'P'):
                product_ID = str(product_fields[0])
                product_name = str(product_fields[1])
                try:
                    product_price = (product_fields[2])
                    float(product_price)
                except ValueError as e:
                    print('#####VALUE ERROR#####') 
                    print (e) 
                    print('PRODUCT PRICE')
                    product_price = 0.00
                    print(product_price)
                except:
                    print('######## UNKNOWN ERROR ########')    
                    
                stock=int(product_fields[3])
                print('#########product_fields after IF before instantiated #########')
                print(product_fields)
                a_product = Product(product_ID, product_name, product_price, stock)
                print('################################## A PRODUCT VARIABLE ################################')
                print(a_product)
               
                print('################################## PRODUCTS LIST BEFORE ADD_PRODUCT METHOD ################################')
                print(self.products_list)
                self.add_product(a_product)
                print('################################## PRODUCTS LIST AFTER ADD_PRODUCT METHOD ################################')
                print(self.products_list)
                #time.sleep(10)
            elif (product_fields[0][0] == 'B'):   
                product_ID = str(product_fields[0])
                product_name = str(product_fields[1])
                stock = int(product_fields[-1])
                product_ID_list = []
                for i in product_fields[2: -1: 2]: #slice item syntax
                    product_ID_list.append(i)# attempting to do array slicing 
                bundle_price = sum([p.product_price for p in self.products_list]) * 0.8 
                print('######### product_fields after IF (bundle) before instantiated #########')
                print(product_fields)
                #time.sleep(10)
                a_product = Bundle(product_ID, product_name, product_ID_list, bundle_price, stock) ### RECURSION PROBLEM PART 1
                
                ## creates namespace as it's declared as object. products_list will now be a list of objects.  # need to revisit save_data as not sure how it fits now. 
                print('################################## A PRODUCT VARIABLE (BUNDLE) ################################')
                print(a_product)
                
                print('################################## PRODUCTS LIST BEFORE ADD_PRODUCT METHOD ################################')
                print(self.products_list)                                                                              
                self.add_product(a_product)
                print('################################## PRODUCTS LIST AFTER ADD_PRODUCT METHOD ################################')
                print(self.products_list)
            line=file_object.readline()
            
        print('################################## PRODUCTS LIST AFTER ADD_PRODUCT METHOD ################################')
        print(self.products_list)
        file_object.close()
        
    
    def load_orders(self, orders_file):    #read_orders            
        file_object = open(orders_file, "r")   # 'a' mode append                    
        i=0
        line=file_object.readline()
        while(line!=""):
            order_fields = line.split(",") #split turns string into a list #therefore each line of file is declared as list variable.
           
           # both single and multi product orders now take lists so that the initializer can be used for both without added methods.
               
          
            customerID_Or_name = order_fields[0]
            order_date = order_fields [-1]                                 
            productList = []
            for p in order_fields[1: -2: 2]: 
                productList.append(p)                     
            quantities = []
            for q in order_fields[2: -1: 2]:
                quantities.append(q)
            an_order = Order(customerID_Or_name, productList, quantities, order_date) 
            print('###################      AN ORDER        ######################')
            print(an_order)
            # adds to orders_list Records attribute
            self.add_order(an_order)  
            # the above method should also create an object of record class. Which invokes constructor. Therefore, it makes sense to align an_order with orders constructor. 
            print('################################   ORDERS LIST  ########################################')
            print(self.orders_list)
            line=file_object.readline()
            
        print('##################################LOAD ORDERS METHOD################################')
        print(self.orders_list)        
            #except Exception:        
        file_object.close()
        
    
    ######FIND METHODS ######
    
    #These methods don't return lists, they return tupples 
    def find_customer(self, prompt): #prompt is customer_name or customer_ID
        return next(filter(lambda c: c.customer_ID == prompt or c.customer_name == prompt, self.customers_list), None) 
    ## This iterates through the self.product list and returns all items that are true.
    ## Because next has been used it will return the first match in the iteratble (self.products)
    
    def find_product(self, prompt): #prompt is product_name or product_ID
        return next(filter(lambda p: p.product_ID == prompt or p.product_name == prompt, self.products_list), None) 
    #self.products_list IS definitely an iterable object. The reason this method/syntax is confusing is that lambda seta a condition that accesses a value in an uniterable object that is stored in an iterable list as an attribute of a uninterable class instance object (records).
    
    # THIS CAN BE CALLED FROM MENU - CUSTOMER ORDER HISTORY
    # caution: This works differently to the previous two find_variables methods
    ## this iterates through orders_list and will return all matches.
    def find_orders(self, prompt): #prompt is customer_name or customer_ID
        customer_order_history = filter(lambda o: o.customer_ID == prompt or o.customer_name == prompt, self.orders_list) 
        return list(customer_order_history)
    
    def find_next_customer_number(self):
        most_recent_cust = self.customer_list[-1]
        if len(most_recent_cust) == 2:
            most_recent_num = most_recent_cust[0][1] #verify if this syntax is correct
            int(most_recent_num)
            new_number = most_recent_num + 1
            return str(new_number)
        elif len(most_recent_cust) > 2:
            most_recent_num = most_recent_cust[0][1: -1, 1]
            int(most_recent_num)
            new_number = most_recent_num + 1
            return str(new_number)
        else: 
            print('### UNINDENTIFIED ERROR (find next customer number method')
            
    
    #### PRINTING CORE RECORD LISTS METHODS ####
    
    def list_customers(self):
        print('##########################list_customers_method######')
        print(self.customers_list, 'list_customers method')
        for c in self.customers_list: ###list of objects, hence difference
            print(c)
            
    def list_products(self):
        print('##########################list_products_method######')
        print(self.products_list, 'list products method')
        for p in self.products_list:
            print(p)
            
    def list_orders(self):
        print('##########################list_orders_method######')
        print(self.orders_list, 'list orders method')
        for o in self.orders_list:
            print(o)
            
    #### Save method ####
    
    ## structure of save methods means it assumes that the attribute list (e.g customers_list) stored in records object is already geometrically defined. 
    ## KEY issue from what I understand, the customers_file variable needs to exist in an object instance
    ## but where? It makes sense for it to be held in records class object. If so, it should be created at the start when everything loads
    ## which it actually does when I look at the Records constructor. 
    ## I think what that means is that when save_to_file method is invoked. It will open the customer's file (which will be declared in operations class for example customers_file = customers.txt) and loop through the customer_list of objects. Even though objects use name space instead of index, a premise is that 'they will still have identical formats because they are identical custom data types'. In other words the premise is that even though objects are not indexed, their structure is not randomized and can be iterated through with a for loop. 
    ## its complex because there are iterators and iterables but iterators are iterables themselves. 
    ## "In Python 3.6 and beyond, the keys and values of a dictionary are iterated over in the same order in which they were created. However, this behavior may vary across different Python versions, and it depends on the dictionary’s history of insertions and deletions."
    # this is important as I need to readjust some of my constructor methods. 
    ## However, my earlier premise regarding the structure of python was correct. 
    ## another things about iterating over objects. Objects themselves are not iterables. BUT an object can store iterable values. THEREFORE, I can iterate through an iterable value in a object. E.g I can always access the list variables in an object instance and loop through that. But I can't loop through the object itself. To make an object iterable, I need to use the __inter__ methods.  
    ###Note: A LOT OF THE ABOVE WAS MUDDLING THROUGH THINGS. IN THE END, STR LETS ME FORMAT THE OBJECT AS A STRING. SIMILAR TO FORMAT. THOSE STRING ARE ASSOCIATED WITH VALUES, WHICH CAN BE ACCESSED THROUGH NAME SPACE. 
    
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

    total_price = float(0)  #not initialised
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

    def add_to_unit_price_list(self, prompt): # prompt is unit price
        self.unit_price_list.append(prompt)

    @property
    def get_total_price(self, list): #list is unit_price_list
        self.total_price = float(0)
        for x in list:
            self.total_price += x
        return self.total_price

    ## Constructor method 
  
      
    def __init__(self, identifier, productList, quantities, order_date):                                        
        self.o_customer = identifier #accept name or id          
        productAndQuantity_list = Tools.combine_2_lists(productList, quantities) 
        self.date = order_date ##order_date must always be defined before Order class is declared. 
        self.productAndQuantity = ','.join([str(i) for i in productAndQuantity_list])
        print('###### SELF ORDER INIT ######')
        print(self)
        
    def __str__(self):
        return ', '.join([str(i) for i in [self.o_customer, self.productAndQuantity, self.date]]) 
    
    
    def __repr__(self) -> str:
        return f"({self.o_customer}, {self.productAndQuantity}, {self.order_date}"
            
###########################################################################     OPERATIONS CLASS        #######################################################################################
class Tools ():
            
    #TOOLS 
    @staticmethod
    def sum_list( prompt): # prompt is a list
        sum = 0
        for x in prompt: 
            sum += x
        return sum
    
    @staticmethod                                      
    def combine_2_lists(list1, list2): ### THIS WORKED WITHOUT SELF. HAVE NOT TESTED WITH SELF. SAME WITH 3 LIST METHOD
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
            if validator_function(user_input):
                break
            else:
                print(error_message)
        return user_input
    
    @staticmethod
    def intger_inputValidation(display_message, validator_function, error_message):
        user_input = int 
        while True: 
            user_input = int(input(display_message))
            if validator_function(user_input):
                break
            else:
                print(error_message)
        return user_input
    
    
    def auto_save(self):
        pass #This will be invoked from Tools or menu class. It simply calls the save_to_file if program exits. 
 

############################################################################    OPERATIONS UI CLASS     #################################################################################################



class OperationsUI(): # menu
    
    #records = Records(customers_file, products_file, orders_file)

    date_format = '%d/%m/%Y %H:%M:%S'

    def main(self, argv): 
        if not argv: argv = ['Assignment2/customers.txt', 'Assignment2/products.txt', 'Assignment2/orders.txt']
        if len(argv) not in (0, 2, 3):
            sys.stdout.write('Illegal number of file arugments.\n')
            sys.stdout.write(f'USE: {os.path.basename(__file__)}\n')
            sys.stdout.write(f'    OR {os.path.basename(__file__)} [customers_file] [products_file]\n')
            sys.stdout.write(f'    OR {os.path.basename(__file__)} [customers_file] [products_file] [orders_file]\n')
            exit()

        print('####################################################################### HELLOOOO ##############################################################################')
        sys.stdout.write('\n \n \n')
        
        records = Records(*argv) #instantiates a record object which can be accessed via records.attribute
        
        
        print('################################## AUTO LOADED LISTS################################')
        print(records.customers_list,'############customers_list##########','\n, \n, \n', records.products_list, '###########products_list#########', '\n \n \n', records.orders_list, '##############records_list##########')
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

            #menu_reference_main = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
            choice = Tools.string_inputValidation('Choose an option:', lambda x: x in menu_reference_main, 'Please enter a valid option!') 
            print('waypoint 0.')
            print(choice, 'choice') ## prints None
            print('####### RECORDS.CUSTOMERS_LIST')
            print(records.customers_list)
            
            ### I know that it works up to here because it says please enter valid option when i use letter inputs. 
            
            
            if  choice == '1':
                print('waypoint 1') 
                print(records.customers_list)
                customers_file = 'Assignment2/customers.txt'
                products_file = 'Assignment2/products.txt'
                orders_file = 'Assignment2/orders.txt'
                self.place_an_order(customers_file, products_file, orders_file) #Task 1
                print('################################# WAYPOINT AFTER place_an_order method (choice 1) ######################') 
                #doesn't reach here yet. Takes another path. 
                # place order >
                
            elif choice == '2':
                print('waypoint 2')
                records_2 = dir(records.customers_list)
                print(records_2, 'customers_list') #it's printing the object locations not object vales
                records.list_customers() #i think this is correct as self says Tools does not have the method
                
            elif choice == '3':
                print('waypoint 3')#Note: assigning to variable is neccessary as input_and_validation method returns a value
                #time.sleep(2)
                records.list_products()
            
            
            elif choice == '4':
                print('waypoint 4')# verify if this the right syntax for multiple lambda conditions. 
                new_vip_rate = Tools.float_inputValidation('Enter new VIP discount rate (float).', lambda x: isinstance(x, float) and x > 0, 'Enter a FLOAT that is 0 or greater.')
                print("##### VIP DISCOUNT ########")
                print(VIPMemeber.get_vip_discount)
                VIPMemeber.adjust_vip_discount(float(new_vip_rate))
                print("##### NEW VIP DISCOUNT ########")
                print(VIPMemeber.get_vip_discount)
                
                #### TEST: does it change just the class discount or also discounts or all VIPmemebers.
                
                
            elif choice == '5':
                print('waypoint 5')
                new_threshold = Tools.intger_inputValidation('Enter new VIP threshold (integer).', lambda x: isinstance(x, int) and x > 0, 'Enter an INTGER greater than 0.' )
                print("##### VIP THRESHOLD ########")
                print(VIPMemeber.vip_threshold)
                VIPMemeber.adjust_vip_threshold(int(new_threshold))
                print("##### NEW VIP THRESHOLD ########")
                print(VIPMemeber.vip_threshold)
                
                #### TEST: does it change just the class threshold or also threshold or all VIPmemebers.
                
                
            elif choice == '6':
                print('waypoint 6')
                print("##### ORDERS LIST ########")
                print(records.orders_list)
                print(records.list_orders())
                records.list_orders()
            
            
            elif choice == '7':
                print('waypoint 7')
                customers_file = 'Assignment2/customers.txt'
                products_file = 'Assignment2/products.txt'
                orders_file = 'Assignment2/orders.txt'
                print("##### DISPLAY ALL ORDERS OF A CUSTOMER ########")                                        
                customer_identifier = Tools.input_and_validation('Enter customer name or ID', lambda x: x in records.customer_list, 'Not a valid customer.')
                return records.find_orders(customer_identifier)
                #### this should have an error or exiting main menu as there is return statement. 
            
            
            elif choice == '8':
                print('waypoint 8')
                customers_file = 'Assignment2/customers.txt'
                products_file = 'Assignment2/products.txt'
                orders_file = 'Assignment2/orders.txt'
                print("##### SUMMARIZE ALL ORDERS ########") 
                Tools.summarize_all_orders  #task 2
                #### this should have an error or exiting main menu as there is return statement.
            
            elif choice == '9':
                print('waypoint 9')
                customers_file = 'Assignment2/customers.txt'
                products_file = 'Assignment2/products.txt'
                orders_file = 'Assignment2/orders.txt'
                print("##### MOST VALUABLE CUSTOMER ########") 
                Tools.most_valuable_customer #task 3
                #### this should have an error or exiting main menu as there is return statement.
            
            elif choice == '10':
                print('waypoint 10')
                customers_file = 'Assignment2/customers.txt'
                products_file = 'Assignment2/products.txt'
                orders_file = 'Assignment2/orders.txt'
                print("##### MOST POPULAR PRODUCT ########") 
                Tools.most_popular_product #task 4
                #### this should have an error or exiting main menu as there is return statement.
            
            elif choice == '0':
                print('waypoint 11')
                print("##### BEFORE SAVE TO FILE AND EXIT ########") 
                records.save_to_file # task 5 edit/re-examine save_to_file method
                print('waypoint 12')
                exit()
                
            else:
                pass
                
    menu_reference_main = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    
    ##MAIN MENU METHODS
    
    def place_an_order(self, customers_file, products_file, orders_file):
        
        records = Records(customers_file, products_file, orders_file)
        # customer_identifier
        # exising_customer Boolean # method is records class
        # member Boolean   #### method is in records class
        # If not member: signup Boolean ### signup boolean method is in records class
        
        # productsList   ### taken as input by orders consturctor
        # quantitiesList ### taken as input by orders constructor
        ##### turns to productAndQuantities List when Orders() is instantiated. ######
        
        
        # date = datetime ## format has been declared in UI class. ## verify if this will work. 
        
        # order total ####note added to order. resolved and added to customer object in customers_list within method#### Uses addOrder_totalSpent method in records
        
        temp_productsList = []
        temp_quantitiesList = []
        
        customer_identifier = Tools.string_inputValidation('Enter customer name.', lambda x: isinstance(x, str), 'Error. Try again.\n Enter customer name.') ## lamba is redundant here. Just filler.
        
        is_member = (records.existing_member(customer_identifier))
        print('###### IS MEMBER VARIABLE ###########')
        print(is_member)
        if is_member == False:
            ask_to_join = Tools.string_inputValidation('Enter y or n (e.g y = yes)', lambda x: x in ['n','N','y','Y'], 'Error. Try again.\n Enter y or n.')
            sign_up = records.sign_up(ask_to_join) #method returns boolean
            if sign_up == True: 
                membership_type = Tools.string_inputValidation('Enter m or v (e.g v = vipmember)', lambda x: x in ['v', 'V', 'm', 'M'], 'Error. Try again.\n Enter v or m.')
                if membership_type == 'v'| membership_type == 'V':
                    membership_num = records.find_next_customer_number()
                    customer_ID = 'V'+membership_num
                    print('############### CUSTOMER ID VARIABLE (in place and order method) (if V)   ###############')
                    print(customer_ID)
                elif membership_type == 'm'| membership_type == 'M':
                    membership_num = records.find_next_customer_number()
                    customer_ID = 'M'+membership_num
                    print('############### CUSTOMER ID VARIABLE (in place and order method) (if M)   ###############')
                    print(customer_ID)
                else:
                    print('###### UNIDENTIFIED ERROR ##########')
            if sign_up == False:
                membership_num = records.find_next_customer_number()
                customer_ID = 'C'+membership_num
                print('############### CUSTOMER ID VARIABLE (in place and order method) (if M)   ###############')
                print(customer_ID)
        else: 
            pass
        
        is_new_customer = records.existing_customer(customer_identifier)
        
        print('##### MEMBERSHIP NUMBER (after is_new_customer variable ##################')        
        print(membership_num)
        
        
        ##### MOST VALUABLE CUSTOMER METHOD ########
        
    def reveal_most_valuable_customer(self, record):    ## need to find an efficiency way of passing records instead of adding 3 files each time
                                                        ## but it can be passed the same way as place_an_order method
                                                
        print('########   REVEAL MOST VALUABLE CUSTOMER METHOD  ##############')
        customers = record.customers

        if customers and len(customers)>0:
            max_spent_customer = max(customers, key=lambda x: x.total_spent) ### MAX TOTAL IS CALCULATED 

            print('{0} is the most valuable customer. \r\nTheir total spent was {2:.1f}'\
            .format(max_spent_customer.customer_name, max_spent_customer.total_spent))
        else:
            print('No customer!')
  
  
        ##### MOST VALUABLE PRODUCT METHOD ########
  
   # def reveal_the_most_popular_product(self, records):
        #print('##### MOST VALUABLE PRODUCT METHOD ########')
        #products  = records.products_list
        #orders = records. ## need to create a get_orders method that appends orders to a list
        ## need to create a counter for each product.  

       

       # most_popular_product = max() #needs to return highest of order counters. 

       # print('{0} is the most popular product. \r\nIt ordered {1} times'\
           # .format(most_popular_product.product_name, counter]))
            
        
        ##########################################
         
            
            
            #if choice in menu_reference_main: 
    
                #menu_reference_main = [] 
                ### premise: the condition is a list. lists are False when they are empty. Semantically, this should work.
                ### the above was how I previously ended the while loop. 
                
              ## UP TO HERE SHOULD BE A WHILE LOOP THAT KEEP GOING BACK TO MENTION OPTIONS UNTIL LAMBDA VALIDATES IT. 
        
        ### IN MAIN_METHOD INDENTATION    
    ###EQUAL TO MAIN_METHOD_INDENTATION  
          
        ##END OF LOOP
    
    
### Note: when records is called/defined in operations, the constructor calls all three load functions, so operations should call the records class at the start,
### this way, operations class can simply refer to the attributes stored in the records class, instead of the initial design of writing and reading each time to the file. That original design might be better in relation to a different IT architecture. 

##RUNNS PROGRAM

if __name__ == "__main__": ### if this is file being run directly (not being imported)
    print('######## SYS.ARGV #########')
    print(sys.argv)
    #time.sleep(20)
    menu = OperationsUI()
    menu.main(sys.argv[1:])
    