import streamlit as st
import sympy as sym

# Define a function to calculate the derivative of the input function
def calculate_derivative(function_str):
    # Parse the input string as a SymPy expression
    x = sym.symbols('x')
    f = sym.sympify(function_str)
    
    # Calculate the derivative of the input function
    df = sym.diff(f, x)
    
    # Convert the SymPy expression to a LaTeX string for display
    df_latex = sym.latex(df)
    
    # Return the derivative and the steps as a tuple
    return df, df_latex

# Define the Streamlit app
def app():
    st.title("Derivative Calculator")
    st.write(
        """
    `refining in progress...`
    """)
    # Add a text input for the user to enter a function
    function_str = st.text_input("Enter a function:", value='x**2')

    # Add a button to calculate the derivative
    if st.button("Calculate Derivative"):
        # Call the calculate_derivative function to get the derivative and steps
        df, df_latex = calculate_derivative(function_str)

        # Display the result and steps
        st.write(f"The derivative of {function_str} is:")
        st.latex(df_latex)
        st.write("Steps:")
        st.latex(sym.latex(df.doit()))

if __name__ == '__main__':
    app()
