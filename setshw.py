# **Task 1: Flight Route Comparison** Imagine you work for an airline and need to compare the flight routes of your
#  airline with a competitor. You have two sets of flight destinations, one for each airline.
#  Write a Python program to find out: 
# 1. Destinations that both airlines fly to.
# 2. Destinations unique to your airline. 
# 3. Whether there are any destinations that neither airline shares. **Example Code:**


ateam_universal_airlines = {'ATL', "MIA", 'TAX', 'NYJ','NYC'}
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

united_routes = our_routes.intersection(competitor_routes )
unique_routes = our_routes.symmetric_difference(competitor_routes)
print(ateam_universal_airlines)
print(united_routes)


# Custom ID numbers 

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
set_IDs = set(customer_ids)
print(set_IDs)
customer_ids = list(set_IDs)
print(customer_ids)