# Function with Outputs

def format_name(f_name,l_name):
    #Docstring
    """Take a first and last name and format it to return
    the title case version of the name"""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    formatted_f_name=f_name.title()
    formatted_l_name=l_name.title()
    name = formatted_f_name + " " + formatted_l_name
    return name

print(format_name(input("What is you first name? "),input("What is you last name?")))

