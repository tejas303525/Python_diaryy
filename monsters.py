string="pppppp@ppp@p$pp"
l=string.split('@')
min_length=float("inf")
for i in l:
    groups=i.split("$")
    length=[len(j) for j in groups]
print(min(min_length,min(length)))