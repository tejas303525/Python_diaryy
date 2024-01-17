InputStr="a5b6c5d3a2"

h={}

for i in range(len(InputStr)):
    if InputStr[i] not in h:
        if InputStr[i].isalpha():
            h[InputStr[i]]=int(InputStr[i+1])
print(h)
for k,v in h.items():
    print(k*v,end="")