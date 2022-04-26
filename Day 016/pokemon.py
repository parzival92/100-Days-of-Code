# python -m pip install -U prettytable

from prettytable import PrettyTable

table = PrettyTable()
table.align = "l"
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])

print(table)