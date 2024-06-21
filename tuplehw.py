# Formatting Flight Itineraries

#(travelers_name, origin, destination)

itinerary = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

def itinerary_printout(itinerary):  
    
    for name, origin, destination in itinerary:
        print(f"{name} is traveling from {origin} to {destination}!")


itinerary_printout(itinerary)

# Library System Enhancement

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
new_books = library.append(input("what book would you like to add to your library:")), library.append(("The Miseducation of the Negro", "Carter G Woodson"))

if ("1984","Brave New World","A whole new world", "The Miseducation of the Negro") in library:
    print("These titles are already in library") 

print(library)
