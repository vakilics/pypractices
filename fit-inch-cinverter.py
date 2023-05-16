feet_inches = input("give the size (feed and inch): ")

def convert(feet_inches):
    #HERE is "Docs-Strings"
    """ This Func, converts feet and inches """       #HERE is "Docs-Strings"

    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    meters = feet *0.3048 + inches * 0.0254
    #return f"{feet} feet and {inches} inches is equal to {meters} meters."
            ###OR###
    return {"feed": feet, "inches": inches}

print(help(convert))
print(convert(feet_inches))
