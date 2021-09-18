def anagram_number(number):
    s = str(number)
    s_anagram = s[::-1]
    if(s_anagram == s):
        return True
    else:
        return False

def roman_to_int(s):
    map_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    s = s.upper()
    length = len(s)
    for i in range(length):
        num = map_roman.get(s[i])
        if(i < length - 1):
            num_next = map_roman.get(s[i+1])
            if(num < num_next):
                total -= num
            else:
                total += num
        else:
            total += num    
    return total    

      

