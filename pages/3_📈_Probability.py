import streamlit as st
import numpy as np
from scipy.stats import *


# Define the list of available distributions
distributions = ['Beta', 'Binomial']

# Define the list of available probability cases
prob_cases = ['Less than', 'Greater than', 'Between']

# Define the UI for the app
st.title("Probability Calculator")

distribution = st.selectbox("Select a distribution", distributions)

if distribution == 'Beta':
    a = st.number_input("a (shape parameter)", value=1.0, step=0.1)
    b = st.number_input("b (shape parameter)", value=1.0, step=0.1)
elif distribution == 'Binomial':
    n = st.number_input("Number of trials", value=10, step=1)
    p = st.number_input("Probability of success", value=0.5, step=0.01, min_value=0.0, max_value=1.0)

prob_case = st.radio("Select a probability case", prob_cases)

if prob_case == 'Less than':
    value = st.number_input("Value", value=0.0, step=0.1)
elif prob_case == 'Greater than':
    value = st.number_input("Value", value=1.0, step=0.1)
else:
    value1 = st.number_input("Lower value", value=0.0, step=0.1)
    value2 = st.number_input("Upper value", value=1.0, step=0.1)

# Calculate the probability based on the selected distribution and probability case
if distribution == 'Beta':
    if prob_case == 'Less than':
        prob = beta.cdf(value, a, b)
    elif prob_case == 'Greater than':
        prob = 1 - beta.cdf(value, a, b)
    else:
        prob = beta.cdf(value2, a, b) - beta.cdf(value1, a, b)
elif distribution == 'Binomial':
    if prob_case == 'Less than':
        prob = binom.cdf(value, n=n, p=p)
    elif prob_case == 'Greater than':
        prob = 1 - binom.cdf(value-1, n=n, p=p)
    else:
        prob = binom.cdf(value2, n=n, p=p) - binom.cdf(value1-1, n=n, p=p)

# Display the calculated probability to the user
    st.write(f"Probability of {prob_case} {value}" + (f" and {value2}" if prob_case == 'Between' else "") + f" is {prob}")
    
