from guitar import Guitar
CURRENT_YEAR = 2022

gibson = Guitar("Gibson L-5 CES",1922, 16035., CURRENT_YEAR)
another = Guitar("Another Guitar", 2013, 8000, CURRENT_YEAR)
print(f"Expected True. Got {gibson.is_vintage()}")
print(f"Expected False. Got {another.is_vintage()}")

