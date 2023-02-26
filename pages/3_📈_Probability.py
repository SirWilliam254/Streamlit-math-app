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
def calc_prob_dist(distribution, params, x):
    dist = distributions[distribution](*params)
    if dist.shapes:
        pdf = dist.pdf(x)
    else:
        pdf = dist.pmf(x)
    return pdf

# Define the Streamlit app
def main():
    st.title('Probability Calculator')
    st.write('This app allows you to calculate probabilities for different distributions.')
    
    # Create dropdown menu to select a distribution
    distribution = st.selectbox('Select a distribution:', list(distributions.keys()))
    
    # Define dictionary of parameter names and their valid ranges
    param_ranges = {
        'Beta': {'a': (0, np.inf), 'b': (0, np.inf)},
        'Binomial': {'n': (0, np.inf), 'p': (0, 1)},
        'Exponential': {'scale': (0, np.inf)},
        'Gamma': {'a': (0, np.inf), 'scale': (0, np.inf)},
        'Geometric': {'p': (0, 1)},
        'Logistic': {'loc': (-np.inf, np.inf), 'scale': (0, np.inf)},
        'Log Normal': {'s': (0, np.inf), 'scale': (0, np.inf)},
        'Negative Binomial': {'n': (0, np.inf), 'p': (0, 1)},
        'Normal': {'loc': (-np.inf, np.inf), 'scale': (0, np.inf)},
        'Poisson': {'mu': (0, np.inf)},
        'T': {'df': (0, np.inf)},
        'Uniform': {'loc': (-np.inf, np.inf), 'scale': (0, np.inf)},
        'Weibull': {'c': (0, np.inf), 'scale': (0, np.inf)}
    }
    
    # Get allowable parameters for the selected distribution
    allowable_params = list(distributions[distribution].shapes.keys())
    param_ranges = {k: v for k, v in param_ranges[distribution].items() if k in allowable_params}
    
    # Get values for the selected parameters
    params = {}
    for param in param_ranges.keys():
        value = st.number_input(f"Enter a value for '{param}'", min_value=param_ranges[param][0], max_value=param_ranges[param][1])
        params[param] = value
    
    # Select a probability case
    prob_type = st.selectbox('Select a probability case:', ['P(X < x)', 'P(X > x)', 'P(x1 < X < x2)'])
    # Get the value(s) of x for the selected probability case
if case == 'P(x1 < X < x2)':
    x1 = st.number_input('Enter the value of x1:', value=0, step=0.01)
    x2 = st.number_input('Enter the value of x2:', value=0, step=0.01)
else:
    x = st.number_input('Enter the value of x:', value=0, step=0.01)

# Calculate the probability
if case == 'P(X < x)':
    prob = distributions[distribution].cdf(x, **params)
elif case == 'P(X > x)':
    prob = 1 - distributions[distribution].cdf(x, **params)
else:
    prob = distributions[distribution].cdf(x2, **params) - distributions[distribution].cdf(x1, **params)

# Display the results
st.write(f'The probability of {case} is {prob:.4f}')

if __name__ == '__main__':
    main()
