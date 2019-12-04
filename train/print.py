labels = [str(num+1) + '\n' for num in range(649)]
string = ''.join(labels)
with open("labels.txt", "w") as text_file:
    print(string, file=text_file)
