# PulseScript programming language
# TODO:
#   Make the function store_function work

special_chars = ["~", "`", "!", "@", "#", "$", '%', "^", "&", "*", "(", ")", "_", "-", "+", "=", "[", "]", "{", "}", "|", "\\",
                 ":", ";", "<", ">", ",", ".", "/", "?"] # removed "'" and '"' to allow strings

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Store the variables and functions in a dictionary
Variables = {} # {name : value}
Functions = {} # {name : inside_function}

# Store the variable you input into a dictionary (the variable has to be valid or else it'll give an SyntaxError)
def store_variable (variable: str, variables = Variables) -> None:
    # Make sure variable is a string
    if not isinstance(variable, str): raise SyntaxError(f"type({variable}) gave {type(variable)} and not <class 'str'>")
    # Make sure the variable is not an enpty string
    if len(variable) == 0: return "No variable to be found"
    # Make sure variable starts with 'Bind'
    if not variable.startswith("Bind("): raise SyntaxError(f"Variable {variable} doesn't start with 'Bind'")

    # Make sure the variable end with ')'
    if not variable.endswith(")"): raise SyntaxError(f"Variable {variable} did not end with ')'")
    # Define the name and value of the variable
    name  = None
    value = None

    # Loops through the elements in the Bind()
    for v in variable[5:]:
        if v == ",":
            # Store the name and strip any whitespace
            name = variable[5:variable.find(v)].strip()
            string = False
            # Loop through the variable but after the comma
            for i in variable[variable.find(v)+1:]:
                if i == ")":
                    # Store the value and strip any whitespace
                    value = variable[variable.find(v)+1:-1].strip()
                    break
                # If i begins with " or ' then everything inside is ignored
                elif i == "'" or i == '"': string = True
                elif i in special_chars and not string: raise ValueError(f"Variable {variable} is not equal to something valid")
                elif i in alphabet and not string: raise ValueError(f"Variable {variable} is not equal to something valid")
            break
        elif v in special_chars or v == "'" or v == '"':
            raise NameError(f"Variable {variable}'s name is not something valid")

    variables[name] = value

#store_variable('Bind(x, "he)llo")')
#print(Variables)

# Store the function you input into a dictionary
def store_function (function: str) -> None:
    # Make sure function is a string
    if not isinstance(function, str): raise SyntaxError(f"type({function}) gave {type(function)} and not <class 'str'>")
    # Make sure the function isn't an empty string
    if len(function) == 0: raise SyntaxError(f"No function to be found")
    # Make sure the function starts with 'Func'
    if not function.startswith('Func ['): raise SyntaxError(f"Function {function} doesn't start with 'Func ['")

    # Define the name and value of the function
    name = None
    value = None

    # Loop through the elements in the function
    for (i, v) in enumerate(function[5:]):
        if v == "]":
            # Make sure the bracket is not in the name of the function
            if "]" in function[5:function.find(v)]: raise NameError(f"Function {function} has a special character {v} in it's name")
        elif v in special_chars or v == '"' or v == '"': raise NameError(f"Function {function} has a special character {v} in it's name")

