items = []
orders = []
customers = []
cart = []

low_stock_alert = 5  # Set the default low-stock alert threshold


# This simple function to display the items available in inventory
def view_items():
    print('------------------View Items------------------')
    print('The number of items in the inventory are: ', len(items))
    for item in items:
        for key, value in item.items():
            print(key, ':', value)
        print('----------------------------------------------')


# add_product function add the product by asking details like name quantity and price
def add_product():
    print('------------------Add Product------------------')
    product = {}
    product['name'] = input('Product name: ')
    while True:
        try:
            product['quantity'] = int(input('Product quantity: '))
            break
        except ValueError:
            print('Quantity should only be in digits')
    while True:
        try:
            product['price'] = float(input('Price $: '))
            break
        except ValueError:
            print('Price should be a numeric value')
    print('Product has been successfully added.')
    items.append(product)


# In this is used for modifying the existing products like name or price a quantity
def update_product():
    print('-----------------Update Product----------------')
    update_product_name = input('Enter the name of the product that you want to update: ')
    for product in items:
        if update_product_name.lower() == product['name'].lower():
            print('Here are the current details of ' + update_product_name)
            print(product)
            product['name'] = input('Product name: ')
            while True:
                try:
                    product['quantity'] = int(input('Product quantity: '))
                    break
                except ValueError:
                    print('Quantity should only be in digits')
            while True:
                try:
                    product['price'] = float(input('Price $: '))
                    break
                except ValueError:
                    print('Price should be a numeric value')
            print('Product has been successfully updated.')
            print(product)
            return
    print('Product not found in inventory.')


# remove_product function used to remove any product from inventory
def remove_product():
    print('-----------------Remove Product----------------')
    remove_product_name = input('Enter the name of the product that you want to remove: ')
    for product in items:
        if remove_product_name.lower() == product['name'].lower():
            print('Product ' + remove_product_name + ' has been removed from the inventory.')
            items.remove(product)
            return
    print('Product not found in inventory.')


# This function use to buy the items from seller or from available in th inventory
def purchase_product():
    print('-----------------Purchase Product-----------------')
    purchase_product_name = input('Which product do you want to purchase? Enter name: ')
    for product in items:
        if purchase_product_name.lower() == product['name'].lower():
            if product['quantity'] != 0:
                print(f'Pay ${product["price"]} at the checkout counter.')
                product['quantity'] -= 1
                print('Product purchased successfully.')
                return
            else:
                print('Product out of stock.')
                return
    print('Product not found in inventory.')


# This place_order function is to buy multiple products at one by adding them to in order
def place_order():
    print('------------------Place Order-------------------')
    order = {}
    order['items'] = []
    while True:
        item_name = input('Enter the name of the item to add to the order (type "done" to finish): ')
        if item_name.lower() == 'done':
            break
        for product in items:
            if item_name.lower() == product['name'].lower():
                order['items'].append(product)
                print(f'{item_name} added to the order.')
                break
        else:
            print('Item not found in inventory.')

    orders.append(order)
    print('Order placed successfully.')


# A simple function show the ordered items list for verifying  the items
def view_order():
    print('-------------------View Order-------------------')
    for i, order in enumerate(orders, start=1):
        print(f'Order {i}:')
        for item in order['items']:
            print(item)
        print('----------------------------------------------')


# This update written for making any change with the in order add any product or item
def update_order():
    print('------------------Update Order------------------')
    view_order()
    order_number = int(input('Enter the number of the order you want to update: '))
    if 1 <= order_number <= len(orders):
        order = orders[order_number - 1]
        order['items'] = []
        while True:
            item_name = input('Enter the name of the item to add to the order (type "done" to finish): ')
            if item_name.lower() == 'done':
                break
            for product in items:
                if item_name.lower() == product['name'].lower():
                    order['items'].append(product)
                    print(f'{item_name} added to the order.')
                    break
            else:
                print('Item not found in inventory.')
        print(f'Order {order_number} updated successfully.')
    else:
        print('Invalid order number.')



# add_customer function use add new customer in grocery management system
def add_customer():
    print('-----------------Add Customer-----------------')
    customer = {}
    customer['name'] = input('Customer name: ')
    customer['email'] = input('Customer email: ')
    customers.append(customer)
    print('Customer added successfully.')


# view_customer function used show the existing customer in grocery management system
def view_customer():
    print('------------------View Customers------------------')
    for customer in customers:
        for key, value in customer.items():
            print(key, ':', value)
        print('----------------------------------------------')


# update_customer function called to  modify the customer name or email in grocery management system application
def update_customer():
    print('-----------------Update Customer-----------------')
    update_customer_email = input('Enter the email of the customer you want to update: ')
    for customer in customers:
        if update_customer_email.lower() == customer['email'].lower():
            print('Here are the current details of ' + update_customer_email)
            print(customer)
            customer['name'] = input('Customer name: ')
            customer['email'] = input('Customer email: ')
            print('Customer has been successfully updated.')
            print(customer)
            return
    print('Customer not found.')


# Function to view purchase history for a customer
def view_purchase_history():
    print('-----------------View Purchase History-----------------')
    view_customer()
    customer_email = input('Enter the email of the customer to view purchase history: ')
    for order in orders:
        for item in order['items']:
            for customer in customers:
                if customer_email.lower() == customer['email'].lower():
                    if 'purchase_history' not in customer:
                        customer['purchase_history'] = []
                    customer['purchase_history'].append(item)
                    print(f'{item} added to the purchase history of {customer_email}.')
                    return
    print('Customer not found or no purchase history for the given email.')


# Function to add a product to the shopping cart
def add_to_cart():
    print('-----------------Add to Cart-----------------')
    view_items()
    product_name = input('Enter the name of the product to add to the cart: ')
    for product in items:
        if product_name.lower() == product['name'].lower():
            cart.append(product)
            print(f'{product_name} added to the cart.')
            return
    print('Product not found in inventory.')


# Function to view the contents of the shopping cart
def view_cart():
    print('-----------------View Cart-----------------')
    for item in cart:
        print(item)
    print('----------------------------------------------')


# Function to simulate the checkout process
def checkout():
    print('-----------------Checkout-----------------')
    if not cart:
        print('Cart is empty. Add items to the cart first.')
        return

    total_price = sum(product['price'] for product in cart)
    print('Items in the cart:')
    view_cart()
    print(f'Total Price: ${total_price}')

    customer_email = input('Enter customer email to associate with the purchase: ')
    for customer in customers:
        if customer_email.lower() == customer['email'].lower():
            if 'purchase_history' not in customer:
                customer['purchase_history'] = []
            customer['purchase_history'].extend(cart)
            print(f'Purchase successful. Items added to the purchase history of {customer_email}.')
            cart.clear()
            return
    print('Customer not found.')


# Function to view current stock levels
def view_stock():
    print('------------------View Stock------------------')
    for product in items:
        print(f'{product["name"]} - Quantity: {product["quantity"]}, Price: ${product["price"]}')


# Function to receive additional stock for a product
def receive_stock():
    print('-----------------Receive Stock-----------------')
    view_items()
    product_name = input('Enter the name of the product to receive stock: ')
    for product in items:
        if product_name.lower() == product['name'].lower():
            while True:
                try:
                    additional_quantity = int(input('Enter the quantity to receive: '))
                    break
                except ValueError:
                    print('Quantity should only be in digits')
            product['quantity'] += additional_quantity
            print(f'{additional_quantity} units of {product_name} received. New quantity: {product["quantity"]}')
            return
    print('Product not found in inventory.')


# Function to set a low-stock alert threshold
def set_low_stock_alert():
    print('-----------------Set Low-Stock Alert-----------------')
    global low_stock_alert
    while True:
        try:
            low_stock_alert = int(input('Enter the new low-stock alert threshold: '))
            break
        except ValueError:
            print('Threshold should only be in digits')
    print(f'Low-stock alert threshold set to {low_stock_alert} units.')


# Function to display the main menu
def main_menu():
    print('================ Grocery Management System ================')
    print('1. Product Management\n2. Order Management\n3. Customer Management\n4. Point of Sale (POS) System\n5. '
          'Inventory Control\n6. Exit')


def product_management_menu():
    print('---------------- Product Management ---------------')
    print('1. Add Product\n2. View Product\n3. Update Product\n4. Remove Product\n5. Purchase Product\n6. Back')


def order_management_menu():
    print('---------------- Order Management ---------------')
    print('1. Place Order\n2. View Order\n3. Update Order\n4. Back')


def customer_management_menu():
    print('---------------- Customer Management ---------------')
    print('1. Add Customer\n2. View Customer\n3. Update Customer\n4. View Purchase History\n5. Back')


def pos_menu():
    print('---------------- Point of Sale (POS) System ---------------')
    print('1. Add to Cart\n2. View Cart\n3. Checkout\n4. Back')


def inventory_control_menu():
    print('---------------- Inventory Control ---------------')
    print('1. View Stock\n2. Receive Stock\n3. Set Low-Stock Alert\n4. Back')


# Main loop for the application
while True:
    display = input('Press enter to continue.')
    main_menu()
    main_choice = input('Enter the number of your choice: ')

    if main_choice == '1':
        while True:
            product_management_menu()
            product_choice = input('Enter the number of your choice (6 to go back to main menu): ')
            if product_choice == '1':
                add_product()
            elif product_choice == '2':
                view_items()
            elif product_choice == '3':
                update_product()
            elif product_choice == '4':
                remove_product()
            elif product_choice == '5':
                purchase_product()
            elif product_choice == '6':
                break
            else:
                print('You entered an invalid option.')

    elif main_choice == '2':
        while True:
            order_management_menu()
            order_choice = input('Enter the number of your choice (4 to go back to main menu): ')
            if order_choice == '1':
                place_order()
            elif order_choice == '2':
                view_order()
            elif order_choice == '3':
                update_order()
            elif order_choice == '4':
                break
            else:
                print('You entered an invalid option.')

    elif main_choice == '3':
        while True:
            customer_management_menu()
            customer_choice = input('Enter the number of your choice (5 to go back to main menu): ')
            if customer_choice == '1':
                add_customer()
            elif customer_choice == '2':
                view_customer()
            elif customer_choice == '3':
                update_customer()
            elif customer_choice == '4':
                view_purchase_history()
            elif customer_choice == '5':
                break
            else:
                print('You entered an invalid option.')

    elif main_choice == '4':
        while True:
            pos_menu()
            pos_choice = input('Enter the number of your choice (4 to go back to main menu): ')
            if pos_choice == '1':
                add_to_cart()
            elif pos_choice == '2':
                view_cart()
            elif pos_choice == '3':
                checkout()
            elif pos_choice == '4':
                break
            else:
                print('You entered an invalid option.')

    elif main_choice == '5':
        while True:
            inventory_control_menu()
            inventory_choice = input('Enter the number of your choice (4 to go back to main menu): ')
            if inventory_choice == '1':
                view_stock()
            elif inventory_choice == '2':
                receive_stock()
            elif inventory_choice == '3':
                set_low_stock_alert()
            elif inventory_choice == '4':
                break
            else:
                print('You entered an invalid option.')

    elif main_choice == '6':
        print('------------------Exited------------------')
        break

    else:
        print('You entered an invalid option.')
