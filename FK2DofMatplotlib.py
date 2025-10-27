#Dijalankan dan diuji menggunakan google colab
import matplotlib.pyplot as plt

x0, y0 = 0, 0
x1, y1 = 6.894, 5.785
x2, y2 = 31.806, 87.392
x_end, y_end = x1 + x2, y1 + y2

plt.figure(figsize=(8, 8)) #bentuk kanvas persegi

plt.plot([x0, x1, x_end], [y0, y1, y_end], 'b-', linewidth=4, label='Robot Leg (Femur + Tibia)')

plt.scatter([x0, x1, x_end], [y0, y1, y_end], s=100, color=['green', 'orange', 'red'], zorder=5)

plt.xlabel('X ', fontsize=12)
plt.ylabel('Y ', fontsize=12)
plt.title('Visualisasi Forward Kinematics 2-DoF\n(L1=9, L2=93, θ1=40°, θ2=30°)', fontsize=12)

plt.legend(loc='upper right', fontsize=10)
plt.grid(True, alpha=0.3)
plt.axis('equal')

plt.xlim(-5, x_end + 10)
plt.ylim(-5, y_end + 10)

plt.text(0.05, 0.85, 'Rumus FK:\nx = L1 cosθ1 + L2 cos(θ1+θ2) ≈ 38.702\ny = L1 sinθ1 + L2 sin(θ1+θ2) ≈ 93.177', 
         transform=plt.gca().transAxes, fontsize=11, bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow"))

plt.show()

print("Hasil plot menunjukkan L1 yang sangat pendek dibandingkan L2 akibat variabel nim yang berbeda jauh 09 dan 93 sehingga tampak tidak biasa")
