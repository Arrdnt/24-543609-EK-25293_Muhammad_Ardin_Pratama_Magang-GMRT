import math

#NIM = 24/543609/EK/25293
#Femur = 9 #x1
#Tibia = 93 #x2
#Theta1 = 40 
#Theta2 = 30
#Absolute = 70

#Meminta input dinamis
Femur = float(input("Masukkan nilai x1: "))
Tibia = float(input("Masukkan nilai x2: "))
Theta1 = float(input("Masukkan nilai Theta1: "))
Theta2 = float(input("Masukkan nilai Theta2: "))
Absolute_theta = Theta1 + Theta2

print("============================")
#Konversi radian Theta 1
Cos_Theta1 = math.cos(math.radians(Theta1))
Sin_Theta1 = math.sin(math.radians(Theta1))

print("Cos Theta1: ", Cos_Theta1)
print("Sin Theta1: ", Sin_Theta1)
print("============================")

#Hitung Femur atau x1
x1 = Femur * Cos_Theta1
y1 = Femur * Sin_Theta1

print("Posisi x1: ", x1)
print("Posisi y1: ", y1)
print("============================")

#Konversi radian absolute theta
Cos_AbsTheta = math.cos(math.radians(Absolute_theta))
Sin_AbsTheta = math.sin(math.radians(Absolute_theta))

print("Cos Absolute Theta: ", Cos_AbsTheta)
print("Sin Absolute Theta: ", Sin_AbsTheta)
print("============================")

#Hitung Tibia based on x1 dan absolute theta
x2 = Tibia * Cos_AbsTheta
y2 = Tibia * Sin_AbsTheta

print("Posisi x2: ", x2)
print("Posisi y2: ", y2)
print("============================")

# Cari posisi end effector
# x = (x1 + x2) dan y = (y1 + y2)

x = x1 + x2
y = y1 + y2

print("Posisi x: ", x)
print("Posisi y: ", y)
print("============================")
print("Atau nilai x : ", round(x,3))
print("Atau nilai y : ", round(y,3))
