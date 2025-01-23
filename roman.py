#I = 1
#V = 5
#X = 10
#L = 50
#C = 100
#D = 500
#M = 1000


def roman_to_int(s):
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    sum = 0
    i = 0 

    while i < len(s):
        # look at current value
        current = values[s[i]]

        #look at next value
        if i + 1 < len(s): 
            next = values[s[i+1]]

            #comapre next value with current
            if current < next:
                sum += (next-current)
                i += 2
                continue 

        sum += current
        i += 1
    return sum

s = "MCMXCIV"
print(roman_to_int(s)) 


    



    

    
