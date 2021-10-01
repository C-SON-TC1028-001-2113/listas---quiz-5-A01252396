
def main():
    r=int(input())
    c=int(input())
    m=r*c
    Lista1=[]
    Lista2=[]
    index=0
    if r==c:
        for i in range (m):
            n=int(input())
            Lista1.append(n)
        while index <m:
            Elemento=Lista1[index]
            Lista2.append(Elemento)
            index=index+(r+1)
        print(Lista2)    
    else:
        print('La matriz no es cuadrada')





  

if __name__=='__main__':
    main()
