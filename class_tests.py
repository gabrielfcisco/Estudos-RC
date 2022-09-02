import numpy as np
import RobPy as rp

a = rp.cria_vetor3([1,2,3])
b = rp.cria_vetor3([4,5,6])

print(rp.produto_escalar(a,b))
print(rp.tamanho_proj_vetores(a,b))