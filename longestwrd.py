new_word=[]
count=0
N=int(input("Enter the size of wordlist "))
word_list=[]
for i in range(N):
    word_list.append(input())
for i in word_list:
    if i not in new_word:
        new_word.append(i)
print(len(new_word))
