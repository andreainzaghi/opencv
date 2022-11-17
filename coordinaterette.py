import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import json


XY = './coordinate_quadratoXY.json'
YZ = './coordinate_quadratoYZ.json'
ZX = './coordinate_quadratoZX.json'


datixy = json.load(open(XY))
datiyz = json.load(open(YZ))
datizx = json.load(open(ZX))


# def display_img(img):
#     fig = plt.figure(figsize=(6, 6))
#     ax = fig.add_subplot(111)
#     ax.imshow(img, cmap='gray')


# gradient1 = cv2.imread('white_cube.png', 0)
# img = gradient1
# contenuto = []
# px = np.array(img)


# for i in range(500):
#     for j in range(500):
#         if(px[i, j] == 255 & px[i, j] == 255 & px[i, j] == 255):
#             # la retta sara' perpendicolare all'asse z
#             contenuto.append({"x": 0, "y": i, "z": j})
# print(contenuto)


def punto_di_intersezione_rette(xy, yz, zx):

    for i in range(len(xy)):
        primo = xy[i]
        x1, y1, z1 = primo["x"], primo["y"], primo["z"]
        secondo = yz[i]
        x2, y2, z2 = secondo["x"], secondo["y"], secondo["z"]
        terzo = zx[i]
        x3, y3, z3 = terzo["x"], terzo["y"], terzo["z"]
        A = np.array([[x1, y1, z1], [x2, y2, z2], [x3, y3, z3]])
        B = np.array([0, 0, 0])
        x = np.linalg.solve(A, B)
        print(x)


punto_di_intersezione_rette(datixy, datiyz, datizx)
