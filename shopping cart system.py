# shopping cart system

admin_menu = False
user_menu = False

product_list = []
cart_list = []
user_name = []

while True:
    print('\n----------ENTER YOUR ROLE----------')
    print('1.Admin')
    print('2.User')
    print('3.Exit')

    ch = int(input('Enter your choice: '))

    if ch == 3:
        print('\n----------Thank you----------')
        break

    while True:

        # ---------------- ADMIN SECTION ----------------

        if ch == 1:

            print('\n------Admin menu------')
            admin_menu = True

            admin_section = [
                '1.Add products',
                '2.View products',
                '3.Update products',
                '4.Remove products',
                '5.Back to previous menu'
            ]

            for i in admin_section:
                print(i)

            ah = int(input('Select operation to perform: '))

            # ADD PRODUCTS
            if ah == 1:
                print('\n---Add products---')

                product = input('Enter product name: ')
                quantity = int(input('Enter quantity of item: '))
                price = int(input('Enter product price: '))

                if quantity <= 0:
                    print('Quantity must be greater than 0')
                elif price < 0:
                    print('Price cannot be negative')
                else:
                    product_list.append([product, quantity, price])
                    print('Product added successfully')

            # VIEW PRODUCTS
            elif ah == 2:
                print('\n---View products---')

                if len(product_list) == 0:
                    print('No products available')
                else:
                    for i in range(len(product_list)):
                        print(
                            i + 1,
                            product_list[i][0],
                            'Quantity:', product_list[i][1],
                            'Price:', product_list[i][2]
                        )

            # UPDATE PRODUCTS
            elif ah == 3:
                print('\n---Update products---')

                if len(product_list) == 0:
                    print('No products available to update')
                else:
                    for i in range(len(product_list)):
                        print(
                            i + 1,
                            product_list[i][0],
                            'Quantity:', product_list[i][1],
                            'Price:', product_list[i][2]
                        )

                    uh = int(input('Enter product number to update: '))
                    index = uh - 1

                    if index < 0 or index >= len(product_list):
                        print('Invalid product number')
                    else:
                        new_product = input('New product name: ')
                        new_quantity = int(input('New product quantity: '))
                        new_price = int(input('New product price: '))

                        if new_quantity <= 0:
                            print('Quantity must be greater than 0')
                        elif new_price < 0:
                            print('Price cannot be negative')
                        else:
                            product_list[index] = [
                                new_product,
                                new_quantity,
                                new_price
                            ]

                            print('Product updated successfully')

            # REMOVE PRODUCTS
            elif ah == 4:
                print('\n---Remove products---')

                if len(product_list) == 0:
                    print('No products available to remove')
                else:
                    for i in range(len(product_list)):
                        print(
                            i + 1,
                            product_list[i][0],
                            'Quantity:', product_list[i][1],
                            'Price:', product_list[i][2]
                        )

                    rh = int(input('Enter product number to remove: '))
                    index = rh - 1

                    if index < 0 or index >= len(product_list):
                        print('Invalid product number')
                    else:
                        product_list.pop(index)
                        print('Product removed successfully')

            # BACK
            elif ah == 5:
                break

            else:
                print('\n---Invalid input---')


        # ---------------- USER SECTION ----------------

        elif ch == 2:

            print('\n------User menu-------')
            user_menu = True

            user_section = [
                '1.View products',
                '2.Add to cart',
                '3.View cart',
                '4.Remove from the cart',
                '5.Checkout',
                '6.Back to previous menu'
            ]

            for i in user_section:
                print(i)

            bh = int(input('Select operation to perform: '))

            # VIEW PRODUCTS
            if bh == 1:
                print('\n---View products---')

                if len(product_list) == 0:
                    print('No products available')
                else:
                    for i in range(len(product_list)):
                        print(
                            i + 1,
                            product_list[i][0],
                            'Quantity:', product_list[i][1],
                            'Price:', product_list[i][2]
                        )

            # ADD TO CART
            elif bh == 2:
                print('\n---Add to cart---')

                if len(product_list) == 0:
                    print('No products available')
                else:
                    for i in range(len(product_list)):
                        print(
                            i + 1,
                            product_list[i][0],
                            'Quantity:', product_list[i][1],
                            'Price:', product_list[i][2]
                        )

                    ah = int(input('Choose the product number to add to cart: '))
                    index = ah - 1

                    if index < 0 or index >= len(product_list):
                        print('Invalid product number')
                    else:
                        ph = int(input('Choose product quantity: '))

                        if ph <= 0:
                            print('Quantity must be greater than 0')

                        elif ph > product_list[index][1]:
                            print('Item quantity not available')

                        else:
                            # Add selected quantity to cart
                            cart_list.append([
                                product_list[index][0],
                                ph,
                                product_list[index][2]
                            ])

                            # Reduce stock quantity
                            product_list[index][1] = (
                                product_list[index][1] - ph
                            )

                            print('Product added to cart successfully')

            # VIEW CART
            elif bh == 3:
                print('\n---View cart---')

                if len(cart_list) == 0:
                    print('Cart is empty')
                else:
                    for i in range(len(cart_list)):
                        print(
                            i + 1,
                            cart_list[i][0],
                            'Quantity:', cart_list[i][1],
                            'Price:', cart_list[i][2],
                            'Subtotal:',
                            cart_list[i][1] * cart_list[i][2]
                        )

            # REMOVE FROM CART
            elif bh == 4:
                print('\n---Remove from the cart---')

                if len(cart_list) == 0:
                    print('Cart is empty')
                else:
                    for i in range(len(cart_list)):
                        print(
                            i + 1,
                            cart_list[i][0],
                            'Quantity:', cart_list[i][1],
                            'Price:', cart_list[i][2]
                        )

                    rh = int(
                        input('Choose the product number to remove from cart: ')
                    )

                    index = rh - 1

                    if index < 0 or index >= len(cart_list):
                        print('Invalid product number')
                    else:
                        # Return quantity back to product stock
                        product_name = cart_list[index][0]
                        removed_quantity = cart_list[index][1]

                        for i in range(len(product_list)):
                            if product_list[i][0] == product_name:
                                product_list[i][1] = (
                                    product_list[i][1] + removed_quantity
                                )
                                break

                        cart_list.pop(index)

                        print('Product removed successfully')

            # CHECKOUT
            elif bh == 5:
                print('\n---Checkout---')

                if len(cart_list) == 0:
                    print('Cart is empty. Cannot checkout')

                else:
                    total = 0

                    print('\n----------BILL----------')

                    for i in range(len(cart_list)):

                        product_name = cart_list[i][0]
                        quantity = cart_list[i][1]
                        price = cart_list[i][2]

                        subtotal = quantity * price

                        print(
                            i + 1,
                            product_name,
                            'Quantity:', quantity,
                            'Price:', price,
                            'Subtotal:', subtotal
                        )

                        total = total + subtotal

                    print('\nTotal bill:', total)

                    print('Order placed successfully')
                    print('\n---Thank you for shopping!---')

                    cart_list.clear()

            # BACK
            elif bh == 6:
                break

            else:
                print('\n---Invalid input---')

        # INVALID ROLE
        else:
            print('\n---Invalid choice. Try Again---')
            break
