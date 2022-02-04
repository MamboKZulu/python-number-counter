#a python program for counting all the ones from 1 to n
#please forgive my messy commenting
# author mambo zulu....
storage = []
num_strings = []
count = 0
n = eval (input("how many numbers are you entering: "))

for i in range (1,n+1):
    storage.append(i)

for item in storage:
    string_i = str(item)
    num_strings.append(string_i)

for num in num_strings:
    for c in num:
        if c == "1":
            count +=1
print ("there are", count," ones between 1 and ", n)
            
    
