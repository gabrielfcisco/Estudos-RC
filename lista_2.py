from xml.etree.ElementTree import PI
import numpy as np
import RobPy as rp

# Exercício 01

r1 = rp.matriz_rotacao_z(30 * np.pi / 180)
r2 = rp.matriz_rotacao_y(-45 * np.pi / 180)

r = r2 @ r1

T_B_A = rp.cria_operador4(r)

T_A_B = np.linalg.inv(T_B_A)

print(r1)
print(r2)
print(r)
print(T_A_B)
print(T_B_A)

v0 = rp.cria_vetor3([1, 1, 1])

v = rp.cria_vetor4(v0)

w = T_B_A @ v

print(v)
print(w)

# Exercício 02

print("\n\nExercício 02\n")

v_ob_a = rp.cria_vetor3([2, 0, 3])

T2_b_a = rp.cria_operador4(v_o_a=v_ob_a)

print("Matriz de transformação B -> A\n", T2_b_a)

v_b = rp.cria_vetor3([1, 2, 3])

v_a = T2_b_a @ rp.cria_vetor4(v_b)
print("\nVetor no frame A:\n", v_a)

# Exercício 03

print("\n\nExercício 03\n")

v_ob_a3 = rp.cria_vetor3([2, 0, 3])

r1 = rp.matriz_rotacao_z(30 * np.pi / 180)
r2 = rp.matriz_rotacao_y(-45 * np.pi / 180)
r_ex3 = r2 @ r1

T3_A_B = rp.cria_operador4(r_ex3, v_ob_a3)

print("Matriz de transformação A -> B\n", T3_A_B, "\n")

vb = rp.cria_vetor4(rp.cria_vetor3([1, 1, 1]))
T3_B_A = np.linalg.inv(T3_A_B)

print("Matriz de transformação B -> A\n", T3_B_A, "\n")

va = T3_B_A @ vb

print("Vetor w\n", va)

# Exercício 04

# a)
print("\n\nExercício 04\nA)")

ra_1 = rp.matriz_rotacao_z(30 * np.pi / 180)
ra_2 = rp.matriz_rotacao_y(-90 * np.pi / 180)
ra_3 = rp.matriz_rotacao_z(-20 * np.pi / 180)

ra_3_0 = np.linalg.inv(ra_3 @ ra_2 @ ra_1)
ra_3_1 = np.linalg.inv(ra_3 @ ra_2)
ra_3_2 = np.linalg.inv(ra_3)

va_3 = rp.cria_vetor3([0, -1, 0])
va_0 = ra_3_0 @ va_3
va_1 = ra_3_1 @ va_3
va_2 = ra_3_2 @ va_3

print("Vetores:\nV na base 0:\n", va_0, "\nV na base 1:\n", va_1, "\nV na base 2:\n", va_2)

# b)
print("\nB)")

rb_1 = rp.matriz_rotacao_x(15 * np.pi / 180)
rb_2 = rp.matriz_rotacao_y(-10 * np.pi / 180)
rb_3 = rp.matriz_rotacao_z(40 * np.pi / 180)

rb_3_0 = np.linalg.inv(rb_3 @ rb_2 @ rb_1)
rb_3_1 = np.linalg.inv(rb_3 @ rb_2)
rb_3_2 = np.linalg.inv(rb_3)

vb_3 = rp.cria_vetor3([2, 0, 0])
vb_0 = rb_3_0 @ vb_3
vb_1 = rb_3_1 @ vb_3
vb_2 = rb_3_2 @ vb_3

print("Vetores:\nV na base 0:\n", vb_0, "\nV na base 1:\n", vb_1, "\nV na base 2:\n", vb_2)

# c)

print("\nC)")

rc_1 = rp.matriz_rotacao_y(-30 * np.pi / 180)
rc_2 = rp.matriz_rotacao_z(315 * np.pi / 180)
rc_3 = rp.matriz_rotacao_x(100 * np.pi / 180)

rc_3_0 = np.linalg.inv(rc_3 @ rc_2 @ rc_1)
rc_3_1 = np.linalg.inv(rc_3 @ rc_2)
rc_3_2 = np.linalg.inv(rc_3)

vc_3 = rp.cria_vetor3([3, 0, -5])
vc_0 = rc_3_0 @ vc_3
vc_1 = rc_3_1 @ vc_3
vc_2 = rc_3_2 @ vc_3

print("Vetores:\nV na base 0:\n", vc_0, "\nV na base 1:\n", vc_1, "\nV na base 2:\n", vc_2)

# d)

print("\nD)")

rd_1 = rp.matriz_rotacao_z(200 * np.pi / 180)
rd_2 = rp.matriz_rotacao_z(-60 * np.pi / 180)
rd_3 = rp.matriz_rotacao_y(-95 * np.pi / 180)

rd_3_0 = np.linalg.inv(rd_3 @ rd_2 @ rd_1)
rd_3_1 = np.linalg.inv(rd_3 @ rd_2)
rd_3_2 = np.linalg.inv(rd_3)

vd_3 = rp.cria_vetor3([2, 2, 4])
vd_0 = rd_3_0 @ vd_3
vd_1 = rd_3_1 @ vd_3
vd_2 = rd_3_2 @ vd_3

print("Vetores:\nV na base 0:\n", vd_0, "\nV na base 1:\n", vd_1, "\nV na base 2:\n", vd_2)

# e)

print("\nE)")

re_1 = rp.matriz_rotacao_y(90 * np.pi / 180)
re_2 = rp.matriz_rotacao_x(90 * np.pi / 180)
re_3 = rp.matriz_rotacao_y(120 * np.pi / 180)

re_3_0 = np.linalg.inv(re_3 @ re_2 @ re_1)
re_3_1 = np.linalg.inv(re_3 @ re_2)
re_3_2 = np.linalg.inv(re_3)

ve_3 = rp.cria_vetor3([0, 0, 2])
ve_0 = re_3_0 @ ve_3
ve_1 = re_3_1 @ ve_3
ve_2 = re_3_2 @ ve_3

print("Vetores:\nV na base 0:\n", ve_0, "\nV na base 1:\n", ve_1, "\nV na base 2:\n", ve_2)

# Exercício 05

print("\n\nExercício 05\n")

r5_0_1 = rp.matriz_rotacao_x(150 * np.pi / 180)
r5_1_2 = rp.matriz_rotacao_y(-20 * np.pi / 180)
r5_2_3 = rp.matriz_rotacao_z(55 * np.pi / 180)

r5_0_3 = r5_2_3 @ r5_1_2 @ r5_0_1

u_o_a = rp.cria_vetor3([12, 5, 8])

T_F3_F0 = np.linalg.inv(rp.cria_operador4(r5_0_3, u_o_a))

print("Matriz de transformação F3 -> F0\n", T_F3_F0, "\n")

# a)

v5a_3 = rp.cria_vetor4(rp.cria_vetor3([2, -1, 0]))

print("A)\nV no frame 0:\n", T_F3_F0 @ v5a_3)

# b)

v5b_3 = rp.cria_vetor4(rp.cria_vetor3([0, -1, 5]))

print("B)\nV no frame 0:\n", T_F3_F0 @ v5b_3)

# c)

v5c_3 = rp.cria_vetor4(rp.cria_vetor3([2, 3, -1]))

print("C)\nV no frame 0:\n", T_F3_F0 @ v5c_3)

# d)

v5d_3 = rp.cria_vetor4(rp.cria_vetor3([4, 1, 7]))

print("D)\nV no frame 0:\n", T_F3_F0 @ v5d_3)

# e)

v5e_3 = rp.cria_vetor4(rp.cria_vetor3([0, 0, 6]))

print("E)\nV no frame 0:\n", T_F3_F0 @ v5e_3)