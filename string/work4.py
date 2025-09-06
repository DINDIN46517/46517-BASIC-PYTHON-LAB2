line = input()
at_pos = line.find('@')
space_pos = line.find(' ', at_pos)
print(line[at_pos+1:space_pos])
