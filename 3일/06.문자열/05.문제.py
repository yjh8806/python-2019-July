cm = int(input("몇 센티 : "))
row = "┌" + "─" * (cm - 1) + "┐"
column = "│" * (cm + 1)
print(row + "\n" + column)
