# PulseScript programming language
# TODO:
#   Make the function check function work

special_chars = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "[", "{", "]", "}", "\\", 
                 "|", ";", ":", ",", "<", ">", "/", "?"]  # removed "." to allow floats in variables and "=" 
                                                          # to allow a variable be equal to something

# Make sure there's nothing wrong with the syntax of a variable
def var_check(variable: str, debug: bool = False) -> None:
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
        # Value should be a binary value or a number (int or float with optional leading +/-)
        if value_str.startswith('0b'):
            if len(value_str) <= 2: raise SyntaxError(f"{variable} has invalid binary code in it")
            for b in value_str[2:]:
                if b not in ["0", "1"]: raise SyntaxError(f"{variable} has invalid binary code in it")
        else:
            dot_count = 0
            for i, char in enumerate(value_str):
                if char == ".":
                    dot_count += 1
                    if dot_count > 1: raise SyntaxError(f"{variable} has invalid float value with multiple dots")
                elif char in "+-" and i == 0: continue
                elif not char.isdigit(): raise SyntaxError(f"{variable} has invalid character '{char}' in value")

    # Return detailed info for debugging
    if debug: return (f"variable: {variable}\nhas_equal: {has_equal}\nplace: {place}\n"
            f"name: {name}\nValue: {Value}\nvalue: {value_str}")
    else: return None

#print(var_check("x = 0b01", True))
# Make sure there's nothing wrong with the syntax of a function
def function_check(function: str) -> str:
    if not isinstance(function, str): raise SyntaxError(f"type({function}) gave {type(function)} and not <class 'str'>")

    # Convert the string into a list
    L = [x for x in function]

    # Make sure the start begins with 'Func '
    for (i, v) in enumerate(L[:4]):
        if ["F", "u", "n", "c", " "][i] != v: raise SyntaxError(f"Function {function} doesn't begin with 'Func'")
    # Make sure the function has a name
    for (index, value) in enumerate(L[5:]):
        if value == " ":
            if L[index+6] != "[": raise SyntaxError(f"Function {function} has a space in the name")
            break
        elif value in special_chars or value in ["=", "."]: raise SyntaxError(f"Function {function} has special characters in its name")
    return "worked"
print(function_check("Func testing []"))
