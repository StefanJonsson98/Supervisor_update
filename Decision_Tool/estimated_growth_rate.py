import numpy as np
from scipy.stats import mode


###### only  an approach to be discussed later ######
# list of growth rates corresponding to different markets
markets = ['Global SaaS Market', 'HR Management SaaS Segment', 'Global HR Software Market', 'Global Compensation Software Market',]
growth_rates = ['18.82%', '13%', '10.10%', '10.86%']

# the company's current growth rate
company_current_growth_rate = 1.02 # as a decimal

# projection period in years
projection_period = 6

# function that generates a random growth rate for each market 
def generate_growth_rate(growth_rates, weights):
    growth_rate = np.random.choice(growth_rates, p=weights)
    return float(growth_rate[:-1])/100 + 1

# a function that gives each market and its growth rate weights depending on the most relevant markets
def market_weights(growth_rates):
    weights = []
    for i in range(len(growth_rates)):
        if growth_rates[i] == '18.82%':
            weights.append(0.1)
        elif growth_rates[i] == '13%':
            weights.append(0.3)
        elif growth_rates[i] == '10.10%':
            weights.append(0.4)
        elif growth_rates[i] == '10.86%':
            weights.append(0.2)
    return weights

# function that simulates growth for one projection period
def simulate_growth(starting_revenue, weights, projection_period):
    revenues = [starting_revenue]
    for i in range(projection_period):
        growth_rate = generate_growth_rate(growth_rates, weights)
        revenue = revenues[-1] * growth_rate
        revenues.append(revenue)
    final_growth_rate = (revenues[-1]/starting_revenue)**(1/projection_period) - 1
    return final_growth_rate

# function that simulates growth for multiple times
def simulate_growth_multiple(starting_revenue, weights, projection_period, num_simulations):
    final_growth_rates = []
    for i in range(num_simulations):
        final_growth_rate = simulate_growth(starting_revenue, weights, projection_period)
        final_growth_rates.append(final_growth_rate)
    return final_growth_rates

# calculate weights for each market
weights = market_weights(growth_rates)

# simulate growth for multiple times with original weights
starting_revenue = 96.35
num_simulations = 1000
final_growth_rates = simulate_growth_multiple(starting_revenue, weights, projection_period, num_simulations)

# calculate the most common final average growth rate with original weights
mode_growth_rate = mode(final_growth_rates)[0][0]

print('Most common final average growth rate with original weights:', round(mode_growth_rate, 4))

# simulate growth for multiple times with tweaked weights
tweaked_weights = [0.2, 0.3, 0.3, 0.2]
tweaked_final_growth_rates = simulate_growth_multiple(starting_revenue, tweaked_weights, projection_period, num_simulations)

# calculate the most common final average growth rate with tweaked weights
tweaked_mode_growth_rate = mode(tweaked_final_growth_rates)[0][0]

print('Most common final average growth rate with tweaked weights:', round(tweaked_mode_growth_rate, 4))

# use the final growth rate that you are happy with
final_growth_rate = (tweaked_mode_growth_rate+mode_growth_rate)/2

print('Final growth rate:', round(final_growth_rate, 4))