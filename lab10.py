#Siddhartha Jain
#2016269

def recursive_sum(n):
    n=str(n)
    if len(n)==1: return n
    n=sum(int(s) for s in n)
    return recursive_sum(n)

if __name__=='__main__':
    n=int(input())
    print(recursive_sum(n))
