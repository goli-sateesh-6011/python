#import split
def splitting(n):
    li = []
    for i in range(len(n)):
        if len(n) > 7:
            continue
        elif n[i] == " ":
            continue
        else:
            li.append(n[i]) 
    print(li)

splitting("satishG")