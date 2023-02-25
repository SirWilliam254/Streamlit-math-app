import streamlit as st
from decimal import Decimal
import math as math

# Define a function to convert a decimal to a fraction
def decimal_to_fraction(decimal_num):
    decimal_str = str(decimal_num)
    decimal_places = 0 if '.' not in decimal_str else len(decimal_str) - decimal_str.index('.') - 1
    fraction_num = int(decimal_num * 10**decimal_places)
    gcd_num = math.gcd(fraction_num, 10**decimal_places)
    numerator = fraction_num // gcd_num
    denominator = 10**decimal_places // gcd_num
    return f"{numerator}/{denominator}" # Return the fraction as a string in the format "numerator/denominator"

# Define the Streamlit app
def app():
    # Add a title to the app
    st.title("Decimal to Fraction Converter")

    # Add a text input to allow the user to enter a comma-separated list of decimal numbers
    decimal_input = st.text_input("Enter decimal numbers separated by commas:")

    # Split the input string into a list of decimal numbers
    try:
        decimal_list = [
            float(d) for d in decimal_input.split(",")
        ]
    except ValueError:
        st.write("Invalid input format. Please enter a comma-separated list of decimal numbers.")
        return
    
    # Convert each decimal number to a fraction using the decimal_to_fraction function
    fraction_list = [decimal_to_fraction(Decimal(str(d))) for d in decimal_list]

    # Display the list of fractions
    st.write("Fractions:")
    st.write(fraction_list)

# Run the app
if __name__ == '__main__':
    app()

