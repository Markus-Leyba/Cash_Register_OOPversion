# Cash_Register_OOPversion

#### PART 1: STAR analysis ####

''' 
#### SITUATION ####
This a project for a programming subject in my masters degree. This was my first attempt at OOP in Python for a full project. 

### TASK ###

To build a cash register that satisfies provided use cases (USE CASES HAVE BEEN PROVIDED AT THE END OF THIS README). 

parameters of task:
- pure python. Only imports allowed were sys, datetime, os. 
- individual assignment. 
- must use OOP paradigm. 
- I worked on this project for approximately 8 days. 

### ACTION ###

- I built the classes first.
- I don't remember exactly al the steps I took but there was a lot of panic and using lists where I should dictionaries. 
- On multiple occasions, I coded for hours without testing the new code (I'll never do that again). 

### RESULT ###

As a student, the assignment recieved a score of 23.5/30. That's 0.5 marks from a HD so that's not too bad. 

As a progammer, I cooked up my first serving of spaghetti code. It's messy, convoluted and from a design point of view logically inconsistent. 
BUT it's mine and I learned a lot. I learned what not to do and that programming is not just about bargin ahead and making it work. 
Below I've listed a few key lessons I took away from this spaghetti and applied to the next project (see PurePython_ReportGenerator)

- think and build in terms of modules (because it makes isolating bugs easier, it increases reusability and if someone else where to work on this code, it'd be easier for them.)
- I learned that although iteration is key (and that I should have started a couple weeks earlier) it's just as important to take time to carefully consider what data structures to use and why.
- debug early, test each piece as it's created (don't create a bunch of them and test later if you can avoid it). 
- use the print statement as much as you need to debug (in the next project I learned more about VScode debugging tools). 
- don't build a whole section based on IF statements, if I'm using that many IF statements in a code block, it might mean that I need to create some methods that return Boolean values instead.
- Don't create classes that aren't neccessary or don't add any real value. For example, I got a bit too creative and decided to create a Tools Class. This tools class held methods that were general and useful. 
In hindsght I could have just applied the methods to the main class (which is the records class in this case). 
- List comprehensions are powerful. Before this project I hadn't used comprehensions in a project. 
Also thinking in terms of comprehensions helped me think about how to design data structure in the next project (see PurePython_ReportGenerator)

There were also some positive experiments

- reusable verifications methods (see string_inputValidation) are execellent. They are efficient and infinitely reusable. They can designed flexibly. For example in the string_inputValidation method, it takes a lambda as a second
parameter which validates the input (first parameter) and if lambda returns false then it returns an error message (third parameter). This can be adjusted to handle different exceptions. 
- Use __str__ and __repr__  (unless there'a an equivalent or superior alternative) because they make development a heck of a lot easier. 

'''



##### PART 2: ASSIGNMENT SPECIFICATIONS/ PROVIDED USE CASES #####


'''
------------------------------------------- PASS Level (12 marks) ------------------------------------------ 
At this level, your program will have some basic classes with specifications as below. You may need 
to define methods wherever appropriate to support these classes. At the end of the PASS level, your 
program should be able to run with a menu described in the Operations. 
 
Customers: 1. Class Customer 
All customers have a unique ID, unique name (a name will not include any digit). You are 
required to write the class named Customer to support the following: 
i. Attributes ID and name 
ii. Attribute value to store the total money the customer spent to date. A new customer 
will have the value of value to be 0 before placing any order. 
iii. Constructor takes the values of ID, name, value as arguments 
iv. Appropriate getter methods for the attributes of this class 
v. A method get_discount(self, price) which returns (0, price) – where the first return 
value represents the discount rate associated with the customer and the second value 
represents the input price. This method serves as a super method and will have a more 
complex implementation in the subclasses. 
vi. A method display_info that prints the values of the Customer attributes and the 
discount rate associated with the customer. 
 
2. Class Member 
A member is a customer with a membership. When placing an order, a member will be 
offered a discount. All members are offered a discount of a flat rate (i.e., the discount rate is 
the same for all orders – this is to distinguish from the discount of VIPMember below). The 
class Member should have the following components: 
i. An attribute for discount rate, by default, it is 5%. 
ii. Constructor takes the appropriate parameters/arguments (be careful) 
iii. Appropriate getter methods for the attributes of this class 
iv. A method get_discount(self, price) that takes the price of the order and returns both 
the discount rate and the price after the discount. For example, this method returns 
(0.05, 950) when the discount rate is 5% and the order's price is 1000$. 
v. A method display_info(self) that prints the values of the Member attributes. 
vi. A method set_rate to adjust the flat rate of discount. This affects all members. 
 
3. Class VIPMember 
A VIP member is a customer with a VIP membership. All VIP members are offered a 
discount based on two rates: the first rate applies when the price of the order is smaller or 
equal to a threshold ($1000 by default), and the second rate applies when the order's price 
exceeds this threshold. For example, with the threshold being 1000$, then, when a VIP 
member named Sarah places an order that costs 800$, the discount rate for this order is the 1st 
discount rate; when Sarah places an order that costs 1200$, the discount rate for this order is 
the 2nd discount rate.  
NOTE for all VIP members, the 2nd discount rate is always 5% more than the 1st discount 
rate. The discount rates might be different among the VIP members. If not specified, the first 
and second discount rates are set as 10% and 15%, respectively. On the other hand, the 
threshold applies to all VIP members, i.e., all VIP members have the same threshold. 

The class VIPMember should support the following components 
i. Attributes to support the two discount rates and the threshold limit 
ii. Necessary constructors 
iii. Appropriate getter methods for the attributes of this class 
iv. A method get_discount(self, price) that takes the price of the order and returns both 
the discount rate and the price after the discount. 
v. A method display_info that prints the values of the VIPMember attributes. 
vi. A method set_rate to adjust the discount rates of each individual VIP member. 
vii.  A method set_threshold to adjust the threshold limit. This affects all VIP members. 
Products 
4. Class Product 
This class is to keep track of information on different products that the department store sells. 
This class supports the following information: 
• ID: A unique identifier of the product (e.g., P1, P2, P3) 
• Name: The name of the products (you can assume the product names are unique and 
they do not include any digit) 
• Price: The price of the product 
• Stock: the quantity of the product available in stock  
You need to define appropriate attributes and methods to support the class Product. Note the 
stock quantity obviously will be changed. The product's price may also be changed by users. 
 
Orders 
5. Class Order 
This class is to handle customers' orders. This class supports the following information of an 
order: 
• Customer: the one who place the order (can be a normal customer, a customer with a 
normal membership, or a customer with a VIP membership). Note you need to 
think/analyse if this should be an ID, name, or something else. 
• Product: the product of the order. Note you need to think/analyse if this should be an 
ID, name, or something else. 
• Quantity: the quantity of the product ordered by customers.  
• You need to think if there are any extra attributes and methods you want to define in 
this class 
Note that this class can update information in the corresponding customer and destination if 
necessary. For example, an object from the class Order can update the information of the 
corresponding customer (e.g., discount rate) or/and the product (e.g., stock). Therefore, you 
need to define appropriate variables and methods to support this class. 
 
Records 
6. Class Records 
This class is the central data repository of your program. It supports the following 
information: 
• A list of existing customers – you need to think what you should store in this list (ID, 
name, or something else?) 

• A list of existing products – you need to think about what you should store in this list 
(ID, name, or something else?) 
• This class has a method named read_customers that can read a comma-separated file 
called customers.txt and add the customers in this file to the customer list of the class. 
See an example of the customers.txt file below. 
 In this file, customers are always in this format: ID, name, discount rate, and value. 
For example, in the 1st line, the ID is C1, the name is James, the discount rate of this 
customer is 0, and the value is 500.2. Note that for VIP members, the first discount 
rates will be stored. A normal customer has an ID starting with the letter "C". A 
member (customer with a normal membership) has an ID starting with the letter "M". 
A VIP member (customer with a VIP membership) has an ID starting with the letter 
"V". The numbers in the ID after these characters (C, M, V) are all unique (i.e., 1, 2, 
3, 5... are unique; for example, if there is a customer with the ID of C1, there won't be 
a member with the ID of M1). In this part, you can assume there will be no error in 
this customers.txt file (e.g., the data format is always correct, and the values are 
always valid). 
• This class has another method named read_products that can read another comma-
separated value file called products.txt and add the products stored in that file to the 
product list of the class. See an example of the products.txt file below. 
 
In this file, products are always in this format: ID, name, price (unit price per each 
product), and the stock. The IDs of all products always start with the letter "P". All 
the product IDs are unique. You can assume there will be no error in this file (e.g., the 
data format is always correct, and the values are always valid). 
• This class also has two methods find_customer and find_product. These two 
methods are to search through the list of customers and products to find out whether a 
given customer or a given product exists or not. If found, the corresponding customer 
and product will be returned, otherwise, None will be returned. Note that both the 
customer and the product can be searched using either ID or name. 
• This class also has two methods list_customers and list_products. These two 
methods can list all the existing customers and products on screen. The display format 
is flexible, and note that you can display all necessary information, and make sure at 
least all the information as in the customers.txt and products.txt files should be 
displayed. These methods can be used to validate the reading from the .txt files 
customers.txt and products.txt. 

NOTE you are allowed to add extra attributes and methods in this class if these attributes and 
methods make your program more efficient. 
 
Operations 
This can be considered the main class of your program. It supports a menu with the following 
options: 
i. Place an order: this option allows users to place an order for a customer. Detailed 
requirements for this option are below (Requirements vi-viii). 
ii. Display existing customers: this option can display all the information: ID, name, discount 
rate (1st discount rate for VIP member), value, threshold limit (for VIP member) of all 
existing customers. 
iii. Display existing products: this option can display all the information: ID, name, price, stock 
of all existing products. 
iv. Exit the program: this option allows users to exit the program. 
Other requirements of the menu program are as follows: 
v. When the program starts, it looks for the files customers.txt and products.txt in the local 
directory (the directory that stores the .py file of the program). If found, the data will be read 
into the program accordingly, the program will then display a menu with the 4 options 
described above. If any file is missing, the program will quit gracefully with an error message 
indicating the corresponding file is missing. 
vi. Your menu program will allow the user to place an order as specified in PART 1 of 
Assignment 1. Note that in this assignment, the customer can choose to get a normal 
membership or a VIP membership (a VIP membership will cost 200$ more). More detailed 
information regarding the membership choice is in section vii below. Also, note that you do 
not need to handle errors in input in this part. For example, similar to PART 1 of Assignment 
1, you can assume users always enter valid products, valid product prices, and valid "y" or 
"n" answers. You can also assume users always enter the membership type correctly, for 
example, "M" for a normal membership, and "V" for a VIP membership. 
vii. When a customer finishes placing an order, 
a. If the customer is a new customer, you need to add the information of that customer 
into your data collection (think/analyse carefully which information you need to add 
to your data collection). If the customer answers "n" for the question of becoming a 
member, then the customer is just a normal customer. If the customer answers "y", 
then the program will ask what type of member the customer wants. If the answer is 
"M", then the customer will become a member (a customer with a normal 
membership). If the answer is "V", then the customer will become a VIP member (a 
customer with a VIP membership). Note that the customer will need to pay an extra 
200$ for becoming a VIP member. Discount is NOT applied to this 200$ membership 
fee. Again, you can assume the users enter the membership type correctly ("M" or 
"V"). 
b. If the customer is an existing customer, you need to update the information of that 
customer in your data collection (think/analyse carefully which information you need 
to update). Note, for existing customers, you DO NOT need to ask if they want a 
membership (normal or VIP membership). This is slightly different compared to the 
requirements in Assignment 1, so please be careful. 

c. Note that, be careful when you add a new customer to your data collection. As 
mentioned in the description of the class Customer, both the ID and the name of a 
customer are unique. 
d. The value of the customer will be increased by the total money they spent on the order 
(this includes the VIP membership fee). 
e. After each order, the stock of the chosen product will be reduced by the quantity in 
the order. At this level, you do not need to handle errors when the quantity in the 
order is larger than the stock quantity. 
viii. The total cost of an order can be displayed as a formatted message as below (for existing 
customers, new customers who are normal customers, or customers with normal 
membership): 
<customer name > purchases <quantity> x <product>. 
Unit price:                                   <the price of the product> (AUD) 
<customer name> gets a discount of <discount percentage>%. 
Total price:                                                  <the total price> (AUD) 
The formatted message is as below for new customers who register to be VIP members: 
<customer name > purchases <quantity> x <product>. 
Unit price:                                   <the price of the product> (AUD) 
     Membership price:           <the price of VIP membership> (AUD) 
<customer name> gets a discount of <discount percentage>%. 
Total price:                                                  <the total price> (AUD) 
ix. When a task is accomplished, the menu will appear again for the next task. The program 
always exits gracefully from the menu. 
 
---------- CREDIT level (3 marks, please do not attempt this level before completing 
the PASS level) ------------ 
At this level, you need to handle exceptions compared to the PASS level. At this level, you are 
required to define various custom exceptions to handle the below issues: 
i. Display an error message if the product entered by the user does not exist in the product list. 
When this error occurs, the user will be given another chance, until a valid product is entered.  
ii. Display an error message if the product quantity is 0, negative, not an integer, or larger than 
the stock quantity of the product. When this error occurs, the user will be given another 
chance, until a valid product quantity is entered. 
iii. Display an error message if the answer by the user is not y or n when asking if the customer 
wants a membership. When this error occurs, the user will be given another chance, until a 
valid answer (i.e., y, n) is entered. 
iv. Display an error message if the answer by the user is not M or V when asking the membership 
type. When this error occurs, the user will be given another chance, until a valid answer (i.e., 
M, V) is entered. 
v. Display an error message if there are any errors in the files customers.txt, products.txt, e.g., 
wrong data format, invalid customer IDs, etc. When an error occurs, the program will display 
a message indicating something wrong with the files, and then exit. 
 
Operations 
i. In this level, in the "Place an order" option, your program will allow ordering a Bundle, 
which is a special product. It means multiple products can be offered together as one product. 
For example, a bundle can consist of an oven, a kettle, and a microwave. You can assume all 
parts of a bundle are existing products in the system. 
The price of a bundle is 80% of the total price of all individual products. For example, if an 
oven costs 300$, a kettle costs 80$, pot costs 30$, and glass costs 15$, then the price of this 
bundle is 80% x (300 + 80 + 30 + 15) = 340$. 
To support this feature, you need to add one more class (Bundle) to your program.  
7. Class Bundle: Each bundle has a unique ID and name (as with Product). You need to 
define the appropriate attributes and methods to support the class Bundle.  
With this modification, the CSV file products.txt at this level may look like this: 
 
The ID of a Bundle always starts with the letter "B". Note that the data format of a bundle is 
different compared to a normal product; it includes the IDs of the product components, and at 
the end, it includes the stock quantity of the bundle. The IDs/names of the products and 
bundles are all unique. You can assume all the products in a bundle are existing products and 
unique (no duplicates). You can assume bundles are always stored at the end of a file, after 
all normal products. 
ii. Also, at this level, your program should display an error message if the product price is not 
set, 0, or negative when the user tries to order it. If this error occurs, your program will then 
go back to the main menu. You can assume the product prices in the products.txt file are 
always either empty or are valid numbers. 
iii. At this level, for the option "Display existing products", when displaying bundles, your 
program will display the ID, name, the IDs of the components, and the stock. On the other 
hand, the products information is the same as in the PASS level. 
iv. Finally, your program should support both products' IDs and names when placing an order. 
For example, instead of entering the product names like in the PASS level, now, users can 
enter the product IDs when placing an order. 
 
---------- DI Level (3 marks, please do not attempt this part before completing the 
CREDIT level) ----------- 
In this part, there are some additional main features for some classes in your program. Some features 
might be challenging. Details of these features are described as follows. 
Class Order: This class now supports date information, i.e., it now has an attribute name date that 
stores which date and time the order are made (you can use an external Python module for this 
feature).
Operations 
Your program now can: 
i. Automatically load previous orders that are stored in a comma-separated file named 
orders.txt that is located in the local directory (same directory with the .py file). Below is an 
example of the orders.txt file: 
 
Each line in the file is an order. The format is always customer name, product, product 
quantity, and date. You can assume all the customers in the orders.txt are existing customers 
(their names are inside the customers.txt file). You can assume all the products in the 
orders.txt are existing products (their names/IDs are inside the products.txt file). Both 
customers and products can be referred by IDs or by names in this orders.txt file. You can 
assume all other information (product quantity, date) in this orders.txt file is always valid. 
ii. Errors when loading the orders.txt file should also be handled. When there are any errors 
loading the file, your program will print a message saying "Cannot load the order file. Run as 
if there is no order previously." and run as if there is no order previously. 
iii. Your menu program should have an option "Adjust the discount rates of a VIP member" to 
adjust the discount rates of the VIP members. The option will ask for the name or ID of the 
VIP member, then ask for the new first discount rate (the second discount rate will then be 
adjusted accordingly). Invalid customers (non-existent or non-VIP customers) will cause the 
program to print a message saying: "Invalid customer!", and then go back to the main menu. 
Invalid discount rate inputs (non-number or negative discount rates) should be handled via 
exceptions, and the user will be given another chance until a valid input is entered. Also, your 
program should support both customers' IDs and names in this option, i.e., users can type 
either customer name or customer ID. 
iv. Your menu program should have an option "Adjust the threshold limit of all VIP members" to 
adjust the threshold limit of all the VIP members. This adjustment will affect all VIP 
members in all future orders. Invalid threshold inputs (non-number of 0 or negative 
threshold) should be handled via exceptions; the user will be given another chance until a 
valid input is entered. 
v. Your menu program should have an option "Display all orders" to display all previous 
orders. The formatted message should be similar to in the orders.txt file (can be slightly 
different but all the information as in the orders.txt file should be shown). 
vi. Your menu program should have an option "Display all orders of a customer" to display all 
previous orders of a particular customer. Users can pass in the name or ID of a customer. The 
formatted message is similar to the previous requirement on the option "Display all orders". 
Note if the name or the ID of the customer is invalid, your program should print a message 
saying: "Invalid customer!", then go back to the main menu. 
vii. Note, in this part, you need to analyse the requirements and update some classes so that your 
program can satisfy the requirements listed above. 

------------- HD level (6 marks, please do not attempt this level before completing 
the DI level) -------------- 
At this level, there are some additional features for some classes in your program. Note that some of 
them are very challenging (require you to optimize the class design and add components to support 
the features). Your program now can: 
• Your program now can use command line arguments to accept the three file names (the first 
being the customer file name, the second being the product file name, and the third being the 
order file name). Note the first two files are mandatory, and the third file is optional (i.e., if 
no order file is supplied, the program will run as if there are no previous orders). If no file 
names are provided, your program will look for customers.txt, products.txt, and orders.txt in 
the local directory. If a wrong number of arguments are provided, the program will display a 
message indicating the correct usage of arguments and exit. 
• At this level, your program will allow customers to purchase multiple items in each order. 
The requirements are as in Assignment 1 for this option (requirements 1 and 2 of Part 3). You 
can design extra classes or modify existing classes to support this requirement. Note that the 
order file format will be slightly different compared to previous levels to accommodate this 
requirement. Below is an example of the order file that supports orders with multiple items. 
 
Each line includes the customer name/ID, the product name/ID, the corresponding quantity, 
the product name/ID, the corresponding quantity, ..., and finally the ordered date. The items 
in each order can be repetitive, e.g., an order can have 2 P1, 3 P2, and 1 P1. 
• Your program will now have an option "Summarize all orders" to display detailed 
information about all previous orders. An example is as follows. OrderNum is the number of 
times the product is ordered (i.e., number of orders). OrderQty is the product quantity that is 
ordered. Note all existing products and customers are listed, although some of them did not 
appear in any orders. 
 P1 P2 P3 P4 P5 P6 P7 B8 B9 
James 0 0 1 0 0 0 0 0 0 
Lily 2 0 0 0 0 0 0 0 0 
Tom 0 0 0 0 1 0 1 0 0 
Annie 0 0 0 0 0 0 0 0 0 
----------------------------------------------------------------------------------------------- 
OrderNum 1 0 1 0 1 0 1 0 0 
OrderQty 2 0 1 0 1 0 1 0 0 
 
• The menu now has an option "Reveal the most valuable customer" to display the customer 
with the maximum total money they spent to date and the total money they've spent. If there 
are multiple customers with the same maximum money spent, you can just display only one 
customer (or all customers, it's your choice).  
• The menu also has an option "Reveal the most popular product" to reveal the product with 
the highest number of orders (based on orders, not on the quantity). 
• When your program terminates, it will update the all the files (customer, products, and 
orders) based on the information when the program executes. 
'''
