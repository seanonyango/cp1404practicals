COLOR_NAME_TO_CODE = {
    "ABSOLUTE ZERO": "#0048ba",
    "ACID GREEN": "#b0bf1a",
    "ALICEBLUE": "#f0f8ff",
    "ALIZARIN CRIMSON": "#e32636",
    "AMARANTH": "#e52b50",
    "AMBER": "#ffbf00",
    "AMETHYST": "#9966cc",
    "ANTIQUEWHITE": "#faebd7",
    "APRICOT": "#fbceb1",
    "AQUA": "#00ffff"
}
color_name = input("Enter a color name: ").upper()
while color_name not in COLOR_NAME_TO_CODE:
    print("Color is not available")
    color_name = input("Enter a color name: ").upper()
print(f"The code for {color_name} is {COLOR_NAME_TO_CODE[color_name]}")


