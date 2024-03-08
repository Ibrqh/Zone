def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

def main():
    # Allowing the user to input price and discount percentage
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate final price using calculate_discount function
    final_price = calculate_discount(price, discount_percent)

    # Displaying the final price
    print("Final Price after discount:", final_price)

# Calling the main function to start the program
main()
