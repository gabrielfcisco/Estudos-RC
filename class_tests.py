import numpy as np
import RobPy as rp

a = rp.cria_vetor3([1,2,3])
b = rp.cria_vetor3([4,5,6])

print(rp.produto_escalar(a,b))
print(rp.tamanho_proj_vetores(a,b))

v = rp.cria_vetor3([1,1,1])
vo = rp.cria_vetor3([0.2,0.3,0.4])

print(rp.matriz_rotacao_x(1.222))

# Função para inverter matrizes:
# np.linalg.inv()

# Para produto matricial usar @

# O determinante de qualquer matriz de rotação é sempre igual a 1:
# np.linalg.det()