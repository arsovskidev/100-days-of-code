# Functions with Outputs


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    else:
        return f"{f_name} {l_name}".title()


print(format_name("filip", "arsovski"))
