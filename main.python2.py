import numpy as np

#definisikan matriks a
A = np.array([[2, 5], [-3, 1]])

#hitungkan invers matriks A 
#np.linalg.inv() kita hitunng A^-1
A_inv = np.linalg.inv(A)

#cetak yang di atas ini 
print("Matriks A:")
print(A)

#cetak invers matriks A
print("\nInvers Matriks A (A^-1):") 
print(A_inv)

#verifikasi mencetak hasil dalam benar 
# (1/17) * [[1, -5], [3, 2]]
#n1/17 = 0.05882353
print("\nVerifikasi A * A^-1 = I (Matriks Identitas):")
print(1/17 * np.array([[1, -5], [3, 2]]))




            