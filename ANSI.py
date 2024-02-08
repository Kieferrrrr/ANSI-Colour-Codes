# https://github.com/Kieferrrrr/ANSI-Colour-Codes

print("\n ANSI Colour Chart\n")

for i in range (1, 255):
	colour = f"\x1b[38;5;{i}m"
	print (f"{colour}{i}", end=" ")