L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# L=[t for t in L if t]
li=L        
for t in L:
    if t:
        li.append(t)

print(L)