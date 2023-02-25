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
    st.write('This app allows you to calculate the probability density/mass function of different distributions.')
    
    # Create dropdown menu to select a distribution
    distribution = st.selectbox('Select a distribution:', list(distributions.keys()))
    
    # Get parameters for the selected distribution
    params = []
    for param in distributions[distribution].shapes:
        param_val = st.number_input(f'Enter value for {param}:', value=1)
        params.append(param_val)
    
    # Get x values for the probability density/mass function
    if distributions[distribution].name == 't':
        x_min = -10
        x_max = 10
    else:
        x_min = st.number_input('Enter minimum x value:', value=-10)
        x_max = st.number_input('Enter maximum x value:', value=10)
    
    x = np.linspace(x_min, x_max, 1000)
    
    # Calculate the probability density/mass function
    pdf = calc_prob_dist(distribution, params, x)
    
    # Plot the probability density/mass function
    st.line_chart(pd.DataFrame({'x': x, 'pdf': pdf}))
    
    # Allow the user to download a CSV of the probability density/mass function
    csv = pd.DataFrame({'x': x, 'pdf': pdf})
    csv_download = csv.to_csv(index=False)
    st.download_button('Download CSV', data=csv_download, file_name=f'{distribution}_pdf.csv', mime='text/csv')
    

if __name__ == '__main__':
    main()
