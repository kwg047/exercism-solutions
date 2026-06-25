def is_isogram(string):
    seen = set()
    string = string.lower()
    
    for char in string:
        if char == " " or char == "-":
            continue

        if char in seen:
            return False
        seen.add(char)
    
    return True