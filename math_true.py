#неправильное деление
import math
from math import inf

def divide(first, second):
    if second == 0:
       #print(math.inf)
        result = math.inf
    else:
        result = first / second
        #print(result)
    return result

# divide(1, 2)