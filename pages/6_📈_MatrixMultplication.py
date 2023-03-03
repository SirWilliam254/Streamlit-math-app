import streamlit as st
import pandas as pd
import numpy as np

def read_csv(file):
    df = pd.read_csv(file, header=None)
    matrix = np.array(df)
    return matrix

def write_csv(matrix):
    df = pd.DataFrame(matrix)
    csv_string = df.to_csv(index=False, sep='\t', header=False, encoding='utf-8-sig')
    return csv_string.encode('utf-8')

def is_numeric(matrix):
    # Check if all variables in the matrix are numeric
    try:
        matrix.astype(float)
        return True
    except ValueError:
        return False

def multiply_matrices(matrix1, matrix2):
    if matrix1.shape[1] != matrix2.shape[0]:
        st.warning("Matrices cannot be multiplied due to incompatible dimensions.")
        return None
    else:
        return np.matmul(matrix1, matrix2)

st.title("Matrix Multiplication App")
st.write("""Upload only csv data that does not contain missing values and also no title rows, just matrix data in each cell from cell A1""")

file1 = st.file_uploader("Upload CSV file for matrix 1:", type=["csv"])
file2 = st.file_uploader("Upload CSV file for matrix 2:", type=["csv"])

if file1 is not None and file2 is not None:
    st.write("Matrix 1:")
    matrix1 = read_csv(file1)
    if not is_numeric(matrix1):
        st.warning("Matrix 1 contains non-numeric values.")
        st.stop()
    st.write(matrix1)

    st.write("Matrix 2:")
    matrix2 = read_csv(file2)
    if not is_numeric(matrix2):
        st.warning("Matrix 2 contains non-numeric values.")
        st.stop()
    st.write(matrix2)

    if st.button("Multiply Matrices"):
        st.write("Resultant Matrix:")
        result = multiply_matrices(matrix1, matrix2)
        if result is not None:
            csv_data = write_csv(result)
            st.download_button(label="Download Resultant Matrix as CSV", data=csv_data, file_name="result.csv")
            st.write(result)
