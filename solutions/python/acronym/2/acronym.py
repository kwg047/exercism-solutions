def abbreviate(words):
    word_list = words.replace('-',' ').replace('_', '').split( )
    result = ''
    
    for word in word_list:
        result += word[0].upper()
        
    return result
    
