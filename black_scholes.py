import math

# ------------------------------------------------------------
# Normal CDF function
# ------------------------------------------------------------
# The Black–Scholes formula needs the "cumulative distribution
# function" (CDF) of a standard normal distribution.
#
# This basically tells us: "What is the probability a random
# value drawn from a bell curve is less than x?"
#
# Python doesn't have this built-in, so we compute it using
# the erf() function, which is mathematically related.
# ------------------------------------------------------------
def N(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


# ------------------------------------------------------------
# Black–Scholes Call Option Formula
# ------------------------------------------------------------
# Inputs:
#   S = current stock price
#   K = strike price (the price you can buy at)
#   T = time until expiration, in years (e.g. 0.5 = 6 months)
#   r = risk-free interest rate (as a decimal, like 0.02)
#   sigma = volatility (how much the stock tends to move yearly)
#
# Output:
#   The fair theoretical price of a European call option.
#
# What the formula does:
#   - Calculates d1 and d2 (mathematical ingredients)
#   - Uses the normal CDF to weigh probabilities
#   - Combines everything to get the option price
# ------------------------------------------------------------
def black_scholes_call(S, K, T, r, sigma):

    # d1 is a measure of how far "in the money" the option is
    # after adjusting for time, volatility, and interest rates.
    d1 = (math.log(S/K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))

    # d2 is just d1 minus one "volatility step"
    d2 = d1 - sigma * math.sqrt(T)

    # Black–Scholes call price formula:
    # S * N(d1)  → the stock's value, weighted by probability
    # K * e^{-rT} * N(d2) → discounted strike price, weighted by probability
    return S * N(d1) - K * math.exp(-r*T) * N(d2)


# ------------------------------------------------------------
# Black–Scholes Put Option Formula
# ------------------------------------------------------------
# Very similar to the call formula, but flips some signs because
# a put increases in value when the stock price goes down.
# ------------------------------------------------------------
def black_scholes_put(S, K, T, r, sigma):

    # Same d1 and d2 as the call option
    d1 = (math.log(S/K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    # Put price formula:
    # K * e^{-rT} * N(-d2) → discounted strike, probability stock ends below strike
    # S * N(-d1) → stock price weighted by probability of finishing lower
    return K * math.exp(-r*T) * N(-d2) - S * N(-d1)
