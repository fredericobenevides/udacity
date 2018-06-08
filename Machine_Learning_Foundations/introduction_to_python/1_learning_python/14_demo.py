f = open("./my_file.txt", 'r')
file_data = f.read()
f.close()

print(file_data)

# files = []
# for i in range(100000):
#     files.append(open('./my_file.txt', 'r'))
#     print(i)

f = open("./my_file.txt", 'w')
f.write('Hello world!')
f.close()

with open("./my_file.txt", 'r') as f:
    file_data = f.read()

print(file_data)
