# PulseScript programming language
# TODO:
#   Make the function check function work for floats and strings

special_chars = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "[", "{", "]", "}", "\\", 
                 "|", ";", ":", ",", "<", ">", "/", "?"]  # removed "." to allow floats

# Make sure there's nothing wrong with the syntax of a variable
def var_check(variable: str) -> str:
    if not isinstance(variable, str): 
        raise SyntaxError(f"type({variable}) gave {type(variable)} and not <class 'str'>")

    # Convert string to list of characters
    L = [x for x in variable]
    has_equal = False
    place = 0
    space = False

    # Make sure the variable name has no invalid special characters
    # and find the '=' sign
    for i, v in enumerate(L):
        if v == "=":
            if "=" in L[i+1:]: 
                raise SyntaxError(f"{variable} has multiple '=' signs")
            has_equal = True
            place = i
            break
        elif v == " ":
            if space: raise SyntaxError(f"{variable} has invalid space in variable name")
            space = True
        elif v in special_chars or v == '"' or v == "'": 
            raise SyntaxError(f"{variable} has invalid character '{v}' in variable name")

    # Check if '=' exists
    if not has_equal: 
        raise SyntaxError(f"{variable} isn't equal to anything")

    # Get variable name (remove spaces at ends)
    name = "".join(L[:place]).strip()
    
    # Get value (still a list for now)
    Value = L[place+1:]
    value_str = "".join(Value).strip()  # convert list to string and strip spaces

    # Check value characters: allow strings in quotes or numeric values
    if not value_str:
        raise SyntaxError(f"{variable} has no value after '='")
    
    if (value_str[0] == '"' and value_str[-1] == '"') or (value_str[0] == "'" and value_str[-1] == "'"):
        # Value is a string, everything inside quotes is allowed
        pass
    else:
        # Value should be a number (int or float with optional leading +/-)
        dot_count = 0
        for i, char in enumerate(value_str):
            if char == ".":
                dot_count += 1
                if dot_count > 1:
                    raise SyntaxError(f"{variable} has invalid float value with multiple dots")
            elif char in "+-" and i == 0:
                continue  # allow leading + or -
            elif not char.isdigit():
                raise SyntaxError(f"{variable} has invalid character '{char}' in value")

    # Return detailed info for debugging
    return (f"variable: {variable}\nhas_equal: {has_equal}\nplace: {place}\n"
            f"name: {name}\nValue: {Value}\nvalue: {value_str}")

print(var_check("x = '35434tg4r'"))
# Make sure there's nothing wrong with the syntax of a function
def function_check(function: str) -> str:
    if not isinstance(function, str): raise SyntaxError(f"type({function}) gave {type(function)} and not <class 'int'>")
    L = [x for x in function]
    