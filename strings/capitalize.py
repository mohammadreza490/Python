def capitalize(sentence) -> str:
    """
    This function will capitalize the first character of a sentence

    if it starts with a 
    >>> capitalize("hello world") 
        "Hello world"
    >>> capitalize("123 hello world)
        "123 hello world"
    >>> capitalize(" hello world")
        " hello world"
    """
    
    first_char = sentence[0]
    new_sentence = str.upper(first_char) + sentence[1:]
    return new_sentence

if "__name__" == __main__:
  from doctest import testmod
  
  testmode()
    
