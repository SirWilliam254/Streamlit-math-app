import streamlit as st
import numpy as np
import scipy.stats as stats

# Define a dictionary of distribution names and their corresponding functions
distributions = {
    'Beta': stats.beta,
    'Binomial': stats.binom,
    'Exponential': stats.expon,
    'Gamma': stats.gamma,
    'Geometric': stats.geom,
    'Logistic': stats.logistic,
    'Log Normal': stats.lognorm,
    'Negative Binomial': stats.nbinom,
    'Normal': stats.norm,
    'Poisson': stats.poisson,
    'T': stats.t,
    'Uniform': stats.uniform,
    'Weibull': stats.weibull_min
}

# Define a function to calculate the probabilities
def calc_probs(distribution, params, x1, x2=None):
    dist = distributions[distribution](*params)
    if x2 is None:
        p1 = dist.cdf(x1)
        p2 = dist.sf(x1)
        p3 = None
    else:
        p1 = dist.cdf(x1)
        p2 = dist.sf(x1)
        p3 = dist.sf(x2) - dist.sf(x1)
    return p1, p2, p3

# Define the Streamlit app
def main():
    st.title('Probability Calculator')
    st.write('This app allows you to calculate the probabilities for different distributions.')
    
    # Create dropdown menu to select a distribution
    distribution = st.selectbox('Select a distribution:', list(distributions.keys()))
    
    # Get parameters for the selected distribution
    params = []
    for param in distributions[distribution].shapes:
        param_val = st.number_input(f'Enter value for {param}:', value=1)
        params.append(param_val)
    
    # Get x1 and x2 values for the probabilities
    x1 = st.number_input('Enter value for x:', value=0)
    if st.checkbox('Calculate p>x>p2'):
        x2 = st.number_input('Enter value for x2:', value=1)
    else:
        x2 = None
    
    # Calculate the probabilities
    p1, p2, p3 = calc_probs(distribution, params, x1, x2)
    
    # Display the probabilities
    st.write(f'p < x: {p1:.4f}')
    st.write(f'p > x: {p2:.4f}')
    if p3 is not None:
        st.write(f'p > x > p2: {p3:.4f}')
    
# Run the Streamlit app
if __name__ == '__main__':
    main()
