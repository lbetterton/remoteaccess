import random
 
# The limit for the extended ASCII Character set
MAX_FLOOR = 97
MAX_LIMIT = 122
 
random_string = ''
 
for _ in range(5000):
    random_integer = random.randint(MAX_FLOOR, MAX_LIMIT)
    # Keep appending random characters using chr(x)
    random_string += (chr(random_integer))
 
print(random_string, len(random_string))
