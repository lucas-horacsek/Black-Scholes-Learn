# ------------------------------------------------------------
# Example usage of the Black–Scholes pricer
# ------------------------------------------------------------
# This script imports the functions from black_scholes.py
# and calculates the price of a call and a put option.
# ------------------------------------------------------------

from black_scholes import black_scholes_call, black_scholes_put

# Example input values:
S = 100      # Current stock price
K = 110      # Strike price
T = 0.5      # Time to maturity (0.5 years = 6 months)
r = 0.02     # 2% risk-free rate
sigma = 0.25 # 25% volatility

# Calculate prices
call_price = black_scholes_call(S, K, T, r, sigma)
put_price  = black_scholes_put(S, K, T, r, sigma)

# Print results
print("Call option price:", call_price)
print("Put option price:", put_price)
