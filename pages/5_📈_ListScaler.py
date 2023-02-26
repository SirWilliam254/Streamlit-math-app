import streamlit as st
import pandas as pd
import base64

def standardize(num_list):
    """
    Standardizes a list of numbers to the range 0-1.
    """
    min_num = min(num_list)
    max_num = max(num_list)
    return [(num - min_num) / (max_num - min_num) for num in num_list]

def download_link(df, filename, link_text):
    """
    Generates a link to download a DataFrame as a CSV file.
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f"data:text/csv;base64,{b64}"
    st.markdown(f'<a href="{href}" download="{filename}">{link_text}</a>', unsafe_allow_html=True)

def main():
    st.title("List Scaler to the range (0,1)")
    st.subheader("Notes")
    st.write(
        """
        Scaling generally refers to the process of transforming features to have the same scale or range. This can be useful when some features have a much larger range than others and you want to ensure that they all have a similar impact on the model. Some common scaling techniques include min-max scaling and max-abs scaling.
        """
    )
    option = st.sidebar.selectbox("Choose option", ("Direct Input", "Upload CSV"))
    
    if option == "Direct Input":
        st.write("Enter a list of numbers separated by commas:")
        num_input = st.text_input("List of numbers")
        num_list = num_input.split(",")
        if st.button("Scale"):
            try:
                num_list = [float(num.strip()) for num in num_list]
            except ValueError:
                st.error("Error: Could not convert values to floats.")
                return
            standardized_list = standardize(num_list)
            st.write("Standardized Numbers:")
            st.write(", ".join([str(num) for num in standardized_list]))
        
    elif option == "Upload CSV":
        file = st.file_uploader("Upload CSV", type=["csv"])
        if file is not None:
            df = pd.read_csv(file)
            st.write("Original DataFrame:")
            st.write(df.head())
            columns = df.columns.tolist()
            selected_columns = st.multiselect("Select columns to scale", columns)
            if selected_columns:
                for column in selected_columns:
                    if df[column].dtype == "float64" or df[column].dtype == "int64":
                        df[column+"_scaled"] = standardize(df[column].tolist())
                    else:
                        st.warning(f"Warning: {column} is not numeric and cannot be scaled.")
                st.write("Scaled DataFrame:")
                st.write(df.head())
                download_link(df, "scaled_data.csv", "Download Scaled CSV")
            else:
                st.warning("Please select at least one column to scale.")
            

if __name__ == "__main__":
    main()
