n_labels = [str(num+1) + '\n' for num in range(649)]
s_labels = [str(num+1) + '_s\n' for num in range(649)]
string1 = ''.join(n_labels)
string2 = ''.join(s_labels)
with open("labels.txt", "w") as text_file:
    print(string1 + string2, file=text_file)
