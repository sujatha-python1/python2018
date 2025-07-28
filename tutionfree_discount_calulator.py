def calculate_tuition_discount(base_tuition, discount_percentage):
    """
    Calculates the discount amount and the final tuition fee after applying a discount.

    Args:
        base_tuition (float): The original tuition fee without any discounts.
        discount_percentage (float): The percentage of discount to be applied (e.g., 10 for 10%).

    Returns:
        tuple: A tuple containing the discount amount and the final tuition fee.
    """
    if not isinstance(base_tuition, (int, float)) or base_tuition < 0:
        raise ValueError("Base tuition must be a non-negative number.")
    if not isinstance(discount_percentage, (int, float)) or not (0 <= discount_percentage <= 100):
        raise ValueError("Discount percentage must be between 0 and 100.")

    discount_amount = (base_tuition * discount_percentage) / 100
    final_tuition = base_tuition - discount_amount
    return discount_amount, final_tuition

if __name__ == "__main__":
    try:
        # Get user input for base tuition and discount percentage
        base_tuition_input = float(input("Enter the base tuition fee: "))
        discount_percentage_input = float(input("Enter the discount percentage (e.g., 10 for 10%): "))

        # Calculate the discount and final tuition
        discount, final_tuition = calculate_tuition_discount(base_tuition_input, discount_percentage_input)

        # Display the results
        print(f"\nOriginal Tuition: ${base_tuition_input:.2f}")
        print(f"Discount Applied: ${discount:.2f}")
        print(f"Final Tuition after Discount: ${final_tuition:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")