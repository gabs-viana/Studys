# "r" = Read (ler)
# "w" = Write (escrever)
# "a" = Append (anexar)


file = open("cah.txt", 'r')

print(file.read())
print(file.readline())
print(file.readlines())


# tip
# while len(line := file.readline()):
#     print(line)

file.close()