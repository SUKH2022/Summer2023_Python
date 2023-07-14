# COMP1112 Mid-Term
# Part2_A.py
# Name: Sukhpreet Saini
# Student #: 200520246
#
# Fixed version should output:
# The capital of Alberta is Calgary.
# The capital of Ontario is Toronto.
# The capital of Quebec is Montreal.
# The capital of British Colombia is Vancouver.
# The capital of Nova Scotia is Halifax.

# it is the functions in which we r making a provinces dictionary with key value-pair 
def part2_A():
    provinces = {
        "Alberta": "Calgary",
        "Ontario": "Toronto",
        "Quebec": "Montreal",
        "British Columbia": "Vancouver",
        "Nova Scotia": "Halifax"
    }
    # it is iterate the dict. and putting all the keys in the provinces and value in the city
    for province, city in provinces.items():
        # it is printing the province and city in the terminal 
        print(f"The capital of {province} is {city}.")

# it is calling the func.
part2_A()

"""
The capital of Alberta is Calgary.
The capital of Ontario is Toronto.
The capital of Quebec is Montreal.
The capital of British Columbia is Vancouver.
The capital of Nova Scotia is Halifax.  
"""