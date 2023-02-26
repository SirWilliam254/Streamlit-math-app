import streamlit as st
import numpy as np
import scipy.stats as stats

# Define a dictionary of distribution names and their corresponding functions
distributions = {
    'Beta': {'func': stats.beta, 'params': ['alpha', 'beta']},
    'Binomial': {'func': stats.binom, 'params': ['n', 'p']},
    'Exponential': {'func': stats.expon, 'params': ['scale']},
    'Gamma': {'func': stats.gamma, 'params': ['k', 'theta']},
    'Geometric': {'func': stats.geom, 'params': ['p']},
    'Logistic': {'func': stats.logistic, 'params': ['loc', 'scale']},
    'Log Normal': {'func': stats.lognorm, 'params': ['s', 'loc', 'scale']},
    'Negative Binomial': {'func': stats.nbinom, 'params': ['n', 'p']},
    'Normal': {'func': stats.norm, 'params': ['loc', 'scale']},
    'Poisson': {'func': stats.poisson, 'params': ['mu']},
    'T': {'func': stats.t, 'params': ['df']},
    'Uniform': {'func': stats.uniform, 'params': ['loc', 'scale']},
    'Weibull': {'func': stats.weibull_min, 'params': ['c', 'scale']}
}

# Define a function to calculate the probability density/mass function
def calc_prob_dist(distribution, params, x, case):
    dist = distributions[distribution]['func'](*params)
    if case == 'p<x':
        prob = dist.cdf(x)
    elif case == 'p>x':
        prob = 1 - dist.cdf(x)
    elif case == 'p1<x<p2':
        prob = dist.cdf(x[1]) - dist.cdf(x[0])
    return prob

# Define the Streamlit app
def main():
    st.title('Probability Calculator')
    st.write('This app allows you to calculate the probability density/mass function of different distributions.')
    
    # Create dropdown menu to select a distribution
    distribution = st.selectbox('Select a distribution:', list(distributions.keys()))
    
    # Get parameter values for the selected distribution
    params = []
    for param in distributions[distribution]['params']:
        param_val = st.number_input(f'Enter value for {param}:', value=1)
        params.append(param_val)
    
    # Create dropdown menu to select the case
    case = st.radio('Select a case:', ['p<x', 'p>x', 'p1<x<p2'])
    
    # Get x value(s) for the probability density/mass function
    if case == 'p<x':
        x = st.number_input('Enter x value:', value=0.5)
    elif case == 'p>x':
        x = st.number_input('Enter x value:', value=0.5)
    elif case == 'p1<x<p2':
        x_min = st.number_input('Enter minimum x value:', value=0)
        x_max = st.number_input('Enter maximum x value:', value=1)
        x = [x_min, x_max]
    
    # Calculate the probability
    prob = calc_prob_dist(distribution, params, x, case)
    
    # Display the probability
    st.write(f'P({case}) = {prob}')
    

if __name__ == '__main__':
    main()
