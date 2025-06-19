file = open('youtube.txt', 'w')

try:
    file.write('Hello, World!')
finally:
    file.close()


with open('youtube.txt', 'w') as file:
    file.write('Hello, World!')