import streamlit as st
from scipy.stats import beta, hypergeom, binom, expon, gamma, geom, nbinom, norm, poisson, uniform, weibull_min

def main():
    st.title("Probability Calculator...in progress...........")
    st.write("Choose a distribution and input the required information to calculate the probability.")

# create a dropdown menu for selecting the distribution
dist = st.selectbox("Select a distribution", ["Beta", "Hypergeometric", "Binomial", "Exponential", "Gamma", "Geometric", "Negative Binomial", "Normal", "Poisson", "Uniform", "Weibull"])

# Defining Functions
def beta_prob():
    a = st.number_input("Enter a value for a", step=0.1)
    b = st.number_input("Enter a value for b", step=0.1)
    x = st.number_input("Enter a value for x", step=0.1)
    return beta.pdf(x, a, b)

def hypergeom_prob():
    N = st.number_input("Enter a value for N", step=1)
    K = st.number_input("Enter a value for K", step=1)
    n = st.number_input("Enter a value for n", step=1)
    x = st.number_input("Enter a value for x", step=1)
    return hypergeom.pmf(x, N, K, n)

def binom_prob():
    n = st.number_input("Enter a value for n", step=1)
    p = st.number_input("Enter a value for p", step=0.1)
    x = st.number_input("Enter a value for x", step=1)
    return binom.pmf(x, n, p)

def expon_prob():
    scale = st.number_input("Enter a value for the scale", step=0.1)
    x = st.number_input("Enter a value for x", step=0.1)
    return expon.pdf(x, scale=scale)

def gamma_prob():
    shape = st.number_input("Enter a value for the shape", step=0.1)
    scale = st.number_input("Enter a value for the scale", step=0.1)
    x = st.number_input("Enter a value for x", step=0.1)
    return gamma.pdf(x, shape, scale=scale)

def geom_prob():
    p = st.number_input("Enter a value for p", step=0.1)
    x = st.number_input("Enter a value for x", step=1)
    return geom.pmf(x, p)


# map the distribution to its corresponding probability function
dist_dict = {
    "Beta": beta_prob,
    "Hypergeometric": hypergeom_prob,
    "Binomial": binom_prob,
    "Exponential": expon_prob,
    "Gamma": gamma_prob,
    "Geometric": geom_prob
    "Negative Binomial": nbinom_prob,
    "Normal": norm_prob,
    "Poisson": poisson_prob,
    "Uniform": uniform_prob,
    "Weibull": weibull_prob
    }


    # call the correct probability function based on the selected distribution
if dist in dist_dict:
    prob = dist_dict[dist]()
else:
    st.write("Invalid distribution selected.")

    # display the probability
st.write(f"The probability is {prob:.4f}")


"""
def nbinom_prob():
    r = st.number_input("Enter a value for r", step=1)
    p = st.number_input("Enter a value for p", step=0.1)
    x = st.number_input("Enter a value for x", step=1)
    return nbinom_dist(r, p, x)

def normal_prob():
    mu = st.number_input("Enter a value for mu", step=0.1)
    sigma = st.number_input("Enter a value for sigma", step=0.1)
    x = st.number_input("Enter a value for x", step=0.1)
    return normal_dist(mu, sigma, x)

def poisson_prob():
    mu = st.number_input("Enter a value for mu", step=0.1)
    x = st.number_input("Enter a value for x", step=1)
    return poisson_dist(mu, x)

def uniform_prob():
    a = st.number_input("Enter a value for a", step=0.1)
    b = st.number_input("Enter a value for b", step=0.1)
    x = st.number_input("Enter a value for x", step=0.1)
    return uniform_dist(a, b, x)

def weibull_prob():
    k = st.number_input("Enter a value for k", step=0.1)
    lambd = st.number_input("Enter a value for lambda", step=0.1)
    x = st.number_input("Enter a value for x", step=0.1)
    return weibull_dist(k, lambd, x)
"""
    # Calculate probability based on selected distribution
if dist == "Beta":
    p = st.beta.cdf(x, a, b)
elif dist == "Hypergeometric":
    p = st.hypergeom.pmf(x, N, K, n)
elif dist == "Binomial":
    p = st.binom.cdf(x, n, p)
elif dist == "Exponential":
    p = st.expon.cdf(x, loc, scale)
elif dist == "Gamma":
    p = st.gamma.cdf(x, a, loc, scale)
elif dist == "Geometric":
    p = st.geom.cdf(x, p)

"""
elif dist == "Negative Binomial":
    p = st.nbinom.cdf(x, n, p)
elif dist == "Normal":
    p = st.norm.cdf(x, loc, scale)
elif dist == "Poisson":
    p = st.poisson.cdf(x, mu)
elif dist == "Uniform":
    p = st.uniform.cdf(x, loc, scale)
elif dist == "Weibull":
    p = st.weibull_min.cdf(x, c, loc, scale)
"""    
# Display probability
st.write("The probability is:", round(p, 4))
