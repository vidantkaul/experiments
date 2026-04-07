# PulseScript programming language
# TODO:
#   Make the function check function work

special_chars = ["~", "`", "!", "@", "#", "$", '%', "^", "&", "*", "(", ")", "_", "-", "+", "=", "[", "]", "{", "}", "|", "\\",
                 ":", ";", "<", ">", ",", ".", "/", "?"] # removed "'" and '"' to allow strings

Variables = {}

# Store the variable you input into a dictionary (the variable has to be valid or else it'll give an SyntaxError)
def store_variable (variable: str, variables = Variables) -> None:
    if not isinstance(variable, str): raise SyntaxError(f"type({variable}) gave {type(variable)} and not <class 'str'>")

    if len(variable) == 0: return "No variable to be found"
    # Make sure variable starts with Bind
    if not variable.startswith("Bind("): raise SyntaxError(f"Variable {variable} doesn't start with 'Bind'")

    # Define the name and value of the variable
    name  = None
    value = None

    # Loops through the elements in the Bind()
    for v in variable[5:]:
        if v == ",":
            # Store the name and strip any whitespace
            name = variable[5:variable.find(v)].strip()
            #starting = (False, None)
            # Loop through the variable but after the comma
            for i in variable[variable.find(v)+1:]:
                if i == ")":
                    # Store the value and strip any whitespace
                    value = variable[variable.find(v)+1:variable.find(i)].strip()
                    break
                elif i in special_chars: raise SyntaxError(f"Variable {variable} is not equal to something valid")
            break
        elif v in special_chars or v == "'" or v == '"':
            raise SyntaxError(f"Variable {variable}'s name is not something valid")

    variables[name] = value

#store_variable('Bind(x, 5)')
#print(Variables)


def function_check (function: str) -> None: pass