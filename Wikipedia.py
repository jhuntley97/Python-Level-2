#Jwaun Huntley
#4/16/19
#problem 5

Wikipedia = {}

def conjunction(d):
    for x in d:
        if x in Wikipedia:
            Wikipedia[x]+=1
        else:
            Wikipedia[x]=1
    print(Wikipedia)

R="iapdorined"

conjunction(R)
