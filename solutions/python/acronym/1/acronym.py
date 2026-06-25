def abbreviate(words):
    word_list = words.replace('-',' ').replace("_", "").split( )
    result = ''
    for i in range(len(word_list)):
        result += word_list[i][0].upper()
    return result
    
