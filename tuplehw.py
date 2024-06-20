# Formatting Flight Itineraries

#(travelers_name, origin, destination)

itinerary = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

def itinerary_printout(itinerary):  
    
    for name, origin, destination in itinerary:
        print(f"{name} is traveling from {origin} to {destination}!")


itinerary_printout(itinerary)