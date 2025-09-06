s = input()

num_str = ''.join([c for c in s if c.isdigit() or c=='.'])
word = ''.join([c for c in s if not (c.isdigit() or c=='.')])

num = float(num_str)
years = int(num)
fraction = num - years

print(f"In {years} years I have spotted {fraction} {word}.")
