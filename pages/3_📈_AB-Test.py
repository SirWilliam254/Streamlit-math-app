import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

def perform_ab_test(df, group_col, metric_col, alpha, test_type):
    """
    Perform A/B test on two groups using a specified significance level and test type.

    Parameters:
    -----------
    df : pandas DataFrame
        Data containing the two groups to be compared
    group_col : str
        Column name representing the group variable
    metric_col : str
        Column name representing the metric variable
    alpha : float
        Significance level for the test
    test_type : str
        Type of test to be performed (either 'two-tail' or 'one-tail')

    Returns:
    --------
    test_result : str
        Result of the test (either 'Reject Null' or 'Fail to Reject Null')
    test_statistic : float
        Test statistic value
    p_value : float
        P-value for the test
    test_significance : float
        Significance level used for the test
    """
    # Split the data into the two groups
    group1 = df[df[group_col] == df[group_col].unique()[0]][metric_col]
    group2 = df[df[group_col] == df[group_col].unique()[1]][metric_col]

    # Perform the A/B test
    if test_type == 'two-tail':
        test_result, p_value = stats.ttest_ind(group1, group2)
        test_significance = alpha / 2
    elif test_type == 'one-tail':
        test_result, p_value = stats.ttest_ind(group1, group2, alternative='greater')
        test_significance = alpha
    else:
        raise ValueError("Invalid test type. Must be either 'two-tail' or 'one-tail'.")

    # Determine whether to reject the null hypothesis
    if p_value < test_significance:
        test_result = 'Reject Null'
    else:
        test_result = 'Fail to Reject Null'

    # Calculate the test statistic
    if test_type == 'two-tail':
        test_statistic = np.abs(test_result)
    else:
        if group1.mean() > group2.mean():
            test_statistic = stats.t.ppf(1 - p_value, len(group1) + len(group2) - 2)
        else:
            test_statistic = stats.t.ppf(p_value, len(group1) + len(group2) - 2)

    # Generate a plot of the distribution of the metric variable in the two groups
    fig, ax = plt.subplots()
    sns.histplot(df, x=metric_col, hue=group_col, kde=True, ax=ax)
    ax.set_title(f"Distribution of {metric_col} by {group_col}")
    st.pyplot(fig)

    return test_result, test_statistic, p_value, test_significance

# Set up the Streamlit app
st.set_page_config(page_title="A/B Test Calc")
st.title("A/B Test App")

# Allow the user to upload a CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file is not None:
    # Load the data into a pandas DataFrame
    df = pd.read_csv(uploaded_file)

    # Allow the user to specify the input parameters
    alpha = st.number_input("Significance level for the test", value=0.05, step=0.01)
    test_type = st.selectbox("Type of test", options=['two-tail', 'one-tail'])

# Perform the A/B test and display the results
if st.button("Run A/B Test"):
    result, statistic, p_value, significance = perform_ab_test(df, group_col, metric_col, alpha, test_type)
    st.write(f"Test result: {result}")
    st.write(f"Test statistic: {statistic}")
    st.write(f"P-value: {p_value}")
    st.write(f"Significance level: {significance}")
