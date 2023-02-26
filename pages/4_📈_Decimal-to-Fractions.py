import streamlit as st

def to_fraction(x, max_denominator=1000):
    """Converts a float to a fraction."""
    if x == 0:
        return 0, 1
    a = int(x)
    frac = x - a
    numerator, denominator = 0, 1
    while abs(frac - float(numerator) / denominator) > 0 and denominator <= max_denominator:
        if frac > float(numerator) / denominator:
            numerator += 1
        else:
            denominator += 1
    return f"{a * denominator + numerator}/{denominator}"

def main():
    st.title("Decimal to Fraction Converter")
    st.write("Enter a list of decimal numbers separated by commas:")
    st.subheader("NB")
    st.write(
        """
         it's important to note that not all decimals can be represented exactly as a fraction, especially if the decimal has repeating decimals or goes on indefinitely. In these cases, the app will give an approximation of the fraction that is as close as possible to the original decimal, but not exact. Currently converting decimals that are of the form (0. ).
        """
    )
    decimals = st.text_input("Decimals")
    decimals_list = decimals.split(",")
    fractions_list = []
    if st.button("Calculate Fractions"):
        for decimal in decimals_list:
            try:
                decimal = float(decimal.strip())
                if decimal >= 1 or decimal <= -1:
                    a, b = to_fraction(decimal)
                    fractions_list.append(f"{a} {b}/{abs(b)}")
                else:
                    fractions_list.append(f"{to_fraction(decimal)}")
            except ValueError:
                st.error(f"Error: Could not convert {decimal.strip()} to float.")

        st.write("Fractions:")
        st.write(", ".join(fractions_list))

if __name__ == "__main__":
    main()
