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

# Define a function to calculate the probability density/mass function
def calc_prob_dist(distribution, params, prob_type, x1=None, x2=None):
    dist = distributions[distribution](*params)
    
    if prob_type == 'P(X < x)':
        prob = dist.cdf(x1)
    elif prob_type == 'P(X > x)':
        prob = 1 - dist.cdf(x1)
    elif prob_type == 'P(x1 < X < x2)':
        prob = dist.cdf(x2) - dist.cdf(x1)
    
    return prob

# Define the Streamlit app
def main():
    st.title('Probability Calculator')
    st.write('This app allows you to calculate probabilities of different distributions.')
    
    # Create dropdown menu to select a distribution
    distribution = st.selectbox('Select a distribution:', list(distributions.keys()))
    
    # Get parameters for the selected distribution
    params = []
    for param in distributions[distribution].shapes:
        param_val = st.number_input(f'Enter value for {param}:', value=1)
        params.append(param_val)
    
    # Create radio button to select the type of probability calculation
    prob_type = st.radio('Select the type of probability calculation:',
                         ['P(X < x)', 'P(X > x)', 'P(x1 < X < x2)'])
    
    # Get x values for the probability calculation (if applicable)
    if prob_type == 'P(X < x)' or prob_type == 'P(X > x)':
        x1 = st.number_input('Enter x value:', value=0)
        x2 = None
    else:
        x1 = st.number_input('Enter x1 value:', value=0)
        x2 = st.number_input('Enter x2 value:', value=1)
    
    # Calculate the probability
    prob = calc_prob_dist(distribution, params, prob_type, x1, x2)
    
    # Display the result
    st.write(f'{prob_type} = {prob:.4f}')

if __name__ == '__main__':
    main()

