import streamlit as st
import sympy as sym

# Define a function to calculate the definite integral of the input function
def calculate_integral(function_str, lower_bound, upper_bound):
    # Parse the input string as a SymPy expression
    x = sym.symbols('x')
    f = sym.sympify(function_str)
    
    # Calculate the definite integral of the input function
    integral = sym.integrate(f, (x, lower_bound, upper_bound))
    
    # Convert the SymPy expression to a LaTeX string for display
    integral_latex = sym.latex(integral)
    
    # Return the integral and the steps as a tuple
    return integral, integral_latex

# Define the Streamlit app
def app():
    st.title("Integral Calculator")
    st.write(
        """
    `refining in progress...`
    """)
    # Add a text input for the user to enter a function
    function_str = st.text_input("Enter a function:", value='x**2')

    # Add number inputs for the lower and upper bounds
    lower_bound = st.number_input("Enter the lower bound:", value=0.0, step=0.1)
    upper_bound = st.number_input("Enter the upper bound:", value=1.0, step=0.1)

    # Add a button to calculate the integral
    if st.button("Calculate Integral"):
        # Call the calculate_integral function to get the integral and steps
        integral, integral_latex = calculate_integral(function_str, lower_bound, upper_bound)

        # Display the result and steps
        st.write(f"The definite integral of {function_str} from {lower_bound} to {upper_bound} is:")
        st.latex(integral_latex)
        st.write("Steps:")
        st.latex(sym.latex(integral))

if __name__ == '__main__':
    app()
