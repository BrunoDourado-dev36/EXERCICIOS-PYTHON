# Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. 
# A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).

X, Y = map(float, input().split())

if X == 0 and Y == 0:
    print('Origem')
elif Y == 0:
    print('Eixo X')
elif X == 0:
    print('Eixo Y')
elif X > 0 and Y > 0:
    print('Q1')
elif X < 0 and Y > 0:
    print('Q2')
elif Y < 0 and X < 0:
    print('Q3')
elif X > 0 and Y < 0:
    print('Q4')