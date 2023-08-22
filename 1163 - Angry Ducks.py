import math
while True:
    try:
        altura = float(input())
        scope_start, scope_end = map(int, input().split())
        tentativas = int(input())
        g = 9.80665
        for _ in range(tentativas):
            angulo, velocidade = map(float, input().split())
            a = -(g/2)
            b = velocidade*math.sin(angulo*3.14159/180)
            c = altura
            tempo = 0
            v_x = velocidade*math.cos(angulo*3.14159/180)
            bhaskara_1 = (-b+((b**2-a*c*4)**0.5))/(2*a)
            bhaskara_2 = (-b-((b**2-a*c*4)**0.5))/(2*a)
            if (bhaskara_1>bhaskara_2):
                tempo = bhaskara_1
            else:
                tempo = bhaskara_2
            resultado = tempo*v_x
            if(resultado>=scope_start and resultado<=scope_end):
                print(f"{resultado:.5f} -> DUCK")
            else:
                print(f"{resultado:.5f} -> NUCK")
    except EOFError:
        break
