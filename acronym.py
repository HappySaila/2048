ignoreWords = input("Enter words to be ignored separated by commas:\n").split(", ")
title = input("Enter a title to generate its acronym:\n").split()

for i in range(len(title)):
    for x in range(len(ignoreWords)):
        if(title[i].lower() == ignoreWords[x].lower()):
            title[i] = ""
         
acron = ""
for y in range(len(title)):
    if title[y] is not "":
        acron += title[y][0]
        
print("The acronym is:",acron.upper())