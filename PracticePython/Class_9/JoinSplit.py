# String Arrays/Lists & Join/Split
csv = "red,green,blue"
colors = csv.split(",")          # ["red","green","blue"]
for c in colors:
    print(c)

line = " | ".join(colors)        # "red | green | blue"
print(line)