from xml.etree.ElementTree import PI
import numpy as np
import RobPy as rp

# Exercício 01

r1 = rp.matriz_rotacao_z(30*np.pi/180)
r2 = rp.matriz_rotacao_y(-45*np.pi/180)

r = r2 @ r1

T_B_A = rp.cria_operador4(r)

T_A_B = np.linalg.inv(T_B_A)

print(r1)
print(r2)
print(r)
print(T_A_B)
print(T_B_A)

v0 = rp.cria_vetor3([1,1,1])

v = rp.cria_vetor4(v0)

w = T_B_A @ v

print(v)
print(w)

# Exercício 02

v_ob_a = rp.cria_vetor3([2,0,3])

T2_b_a = rp.cria_operador4(v_o_a = v_ob_a)

print(T2_b_a)

v_b = rp.cria_vetor3([1,2,3])

v_a = T2_b_a @ v_b