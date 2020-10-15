import cv2 

image = cv2.imread('mypo.jpg') 

window_name = 'Image'  # Window name in which image is displayed 

start_point = (15, 45) # Awal koordinat, dimulai dari sudut kiri atas
end_point = (30, 60)   # Akhir koordinat, kanan bawah dari awal koordinat

color = (0, 255, 255)  # Warna BGR (Blue,Green,Red)

thickness = -1  # Ketebalan

image = cv2.rectangle(image, start_point, end_point, color, thickness) 

cv2.imshow(window_name, image) # Menampilkan gambar
