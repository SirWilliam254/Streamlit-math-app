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

def multiply_matrices(matrix1, matrix2):
    if matrix1.shape[1] != matrix2.shape[0]:
        st.warning("Matrices cannot be multiplied due to incompatible dimensions.")
        return None
    else:
        result = np.zeros((matrix1.shape[0], matrix2.shape[1]))
        for i in range(matrix1.shape[0]):
            for j in range(matrix2.shape[1]):
                for k in range(matrix1.shape[1]):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
        return result

st.title("Matrix Multiplication App")

file1 = st.file_uploader("Upload CSV file for matrix 1:", type=["csv"])
file2 = st.file_uploader("Upload CSV file for matrix 2:", type=["csv"])

if file1 is not None and file2 is not None:
    st.write("Matrix 1:")
    matrix1 = read_csv(file1)
    st.write(matrix1)

    st.write("Matrix 2:")
    matrix2 = read_csv(file2)
    st.write(matrix2)

    if st.button("Multiply Matrices"):
        st.write("Multiplication Process:")
        process = np.zeros((matrix1.shape[0], matrix2.shape[1]), dtype=object)
        for i in range(matrix1.shape[0]):
            for j in range(matrix2.shape[1]):
                temp = []
                for k in range(matrix1.shape[1]):
                    temp.append(f"{matrix1[i][k]} x {matrix2[k][j]}")
                process[i][j] = ' + '.join(temp)
        st.write(process)
        
        st.write("Resultant Matrix:")
        result = multiply_matrices(matrix1, matrix2)
        if result is not None:
            csv_data = write_csv(result)
            st.download_button(label="Download Resultant Matrix as CSV", data=csv_data, file_name="result.csv")
            st.write(result)
