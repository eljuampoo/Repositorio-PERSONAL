friends = ["Esmeralda", "Laurenao", "Marianela", "Sofia", "Celeste"]

print(f"La cantidad de componentes son: {len(friends)}")
print("Y cada componente de forma individual:")

for friend in friends:
    print(friend)

#########################

friends = ["Esmeralda", "Laurenao", "Marianela", "Sofia", "Celeste"]
x = 0
z = len(friends)
print(f"La cantidad de componentes son: {z}")
print("Y cada componente de forma individual:")
while z > x:
    print(f"{friends[x]}")
    x += 1