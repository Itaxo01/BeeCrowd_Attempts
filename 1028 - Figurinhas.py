n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    def Euclides(a, b):
        while(a!=b):
            if(a>b):
                a = a-b
            else:
                b = b-a
        return a
        Euclides(a, b)
    MCD = Euclides(a, b)
    print(MCD)