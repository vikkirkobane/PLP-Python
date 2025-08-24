def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount."""
    if discount_percent >= 20:  # Check if the discount is 20% or higher
        discount_amount = price * (discount_percent / 100)  # Calculate the discount amount
        final_price = price - discount_amount  # Calculate the final price
        return final_price
    else:
        return price  # Return the original price if discount is less than 20%

# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the result
    if final_price < original_price:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${final_price:.2f}")

except ValueError:
    print("Please enter valid numeric values for price and discount percentage.")
