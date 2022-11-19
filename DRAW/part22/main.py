# DRAW IMAGE


import cv2

gambar = cv2.imread(r'D:\APLIKASIKU\DRAW-PYTHON\DRAW\part22\aing.jpg')
gambar_abu = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)
warna_gambar = 255-gambar_abu
blur = cv2.GaussianBlur(warna_gambar, (21, 21), 0)
warnagambar_blur = 255-blur

sketsa = cv2.divide(gambar_abu, warnagambar_blur, scale=256.0)
cv2.imwrite('sketsa_aing.png', sketsa)
cv2.imshow('Gambar', sketsa)