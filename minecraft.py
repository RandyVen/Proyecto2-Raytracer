from raytracer import *
from gl import *
from plane import *
from cube import *
from bush import *

cuality = int(input("Ingrese el nivel de detalle (100 - 1000): "))

r = Raytracer(cuality, cuality)

r.light = Light(
    position=V3(-20, 20, 20),
    intensity=2
)

water = Material(diffuse=color(51, 83, 152), albedo=(
    0.6, 0.3, 0.1, 0), spec=50, refractive_index=2)
dirt = Material(diffuse=color(97, 51, 24), albedo=(
    0.9, 0.1, 0, 0), spec=50)
grass = Material(diffuse=color(34,139,34), albedo=(
    0.9, 0.1, 0, 0), spec=50)
darkWood = Material(diffuse=color(149, 69, 53), albedo=(
    0.9, 0.1, 0, 0), spec=50)
sgreen = Material(diffuse=color(34,139,34), albedo=(
    0.9, 0.1, 0, 0), spec=50)


r.scene.append(Cube(V3(0, -3, -2), 4, water))
r.scene.append(Cube(V3(0, -0.75, -4), 0.5, dirt))
r.scene.append(Cube(V3(0.5, -0.75, -4), 0.5, dirt))
r.scene.append(Cube(V3(1, -0.75, -4), 0.5, dirt))
r.scene.append(Cube(V3(1.5, -0.75, -4), 0.5, dirt))
r.scene.append(Cube(V3(2, -0.75, -4), 0.5, dirt))
r.scene.append(Cube(V3(2.5, -0.75, -4), 0.5, dirt))
r.scene.append(Cube(V3(-0.5, -0.75, -4), 0.5, dirt))
r.scene.append(Cube(V3(-1, -0.75, -4), 0.5, dirt))
r.scene.append(Cube(V3(-1.5, -0.75, -4), 0.5, dirt))
r.scene.append(Cube(V3(-2, -0.75, -4), 0.5, dirt))

r.scene.append(Cube(V3(0, -0.75, -4.25), 0.5, dirt))
r.scene.append(Cube(V3(0.5, -0.75, -4.25), 0.5, dirt))
r.scene.append(Cube(V3(1, -0.75, -4.25), 0.5, dirt))
r.scene.append(Cube(V3(1.5, -0.75, -4.25), 0.5, dirt))
r.scene.append(Cube(V3(2, -0.75, -4.25), 0.5, dirt))
r.scene.append(Cube(V3(2.5, -0.75, -4.25), 0.5, dirt))
r.scene.append(Cube(V3(-0.5, -0.75, -4.25), 0.5, dirt))
r.scene.append(Cube(V3(-1, -0.75, -4.25), 0.5, dirt))
r.scene.append(Cube(V3(-1.5, -0.75, -4.25), 0.5, dirt))
r.scene.append(Cube(V3(-2, -0.75, -4.25), 0.5, dirt))

r.scene.append(Cube(V3(-2.5, -0.75, -3.75), 0.5, dirt))
r.scene.append(Cube(V3(-2.5, -0.75, -3.5), 0.5, dirt))
r.scene.append(Cube(V3(-2.5, -0.75, -3.25), 0.5, dirt))
r.scene.append(Cube(V3(-2, -0.75, -3.75), 0.5, dirt))
r.scene.append(Cube(V3(-2, -0.75, -3.5), 0.5, dirt))
r.scene.append(Cube(V3(-1.5, -0.75, -3.75), 0.5, dirt))
r.scene.append(Cube(V3(2.5, -0.75, -3.75), 0.5, dirt))
r.scene.append(Cube(V3(2.5, -0.75, -3.5), 0.5, dirt))
r.scene.append(Cube(V3(2.5, -0.75, -3.25), 0.5, dirt))
r.scene.append(Cube(V3(2, -0.75, -3.75), 0.5, dirt))
r.scene.append(Cube(V3(2, -0.75, -3.5), 0.5, dirt))
r.scene.append(Cube(V3(1.5, -0.75, -3.75), 0.5, dirt))

r.scene.append(Cube(V3(-2.5, -1.25, -3.75), 0.5, dirt))
r.scene.append(Cube(V3(-2.5, -1.25, -3.5), 0.5, dirt))
r.scene.append(Cube(V3(-2.5, -1.25, -3.25), 0.5, dirt))
r.scene.append(Cube(V3(-2, -1.25, -3.75), 0.5, dirt))
r.scene.append(Cube(V3(-2, -1.25, -3.5), 0.5, dirt))
r.scene.append(Cube(V3(-1.5, -1.25, -3.75), 0.5, dirt))
r.scene.append(Cube(V3(2.5, -1.25, -3.75), 0.5, dirt))
r.scene.append(Cube(V3(2.5, -1.25, -3.5), 0.5, dirt))
r.scene.append(Cube(V3(2.5, -1.25, -3.25), 0.5, dirt))
r.scene.append(Cube(V3(2, -1.25, -3.75), 0.5, dirt))
r.scene.append(Cube(V3(2, -1.25, -3.5), 0.5, dirt))
r.scene.append(Cube(V3(1.5, -1.25, -3.75), 0.5, dirt))

# Arbol 1
r.scene.append(Cube(V3(1.5, -0.50, -4.25), 0.5, darkWood))
r.scene.append(Cube(V3(1.5, 0, -4.25), 0.5, darkWood))
r.scene.append(Cube(V3(1.5, 0.50, -4.25), 0.5, darkWood))
r.scene.append(Cube(V3(1.5, 1, -4.25), 0.5, grass))
r.scene.append(Cube(V3(1.5, 1.50, -4.25), 0.5, grass))
r.scene.append(Cube(V3(1, 0.50, -4.25), 0.5, grass))
r.scene.append(Cube(V3(1, 1, -4.25), 0.5, grass))
r.scene.append(Cube(V3(2, 0.50, -4.25), 0.5, grass))
r.scene.append(Cube(V3(2, 1, -4.25), 0.5, grass))

#Arbol 2
r.scene.append(Cube(V3(-1.5, -0.50, -4.25), 0.5, darkWood))
r.scene.append(Cube(V3(-1.5, 0, -4.25), 0.5, darkWood))
r.scene.append(Cube(V3(-1.5, 0.50, -4.25), 0.5, darkWood))
r.scene.append(Cube(V3(-1.5, 1, -4.25), 0.5, grass))
r.scene.append(Cube(V3(-1.5, 1.50, -4.25), 0.5, grass))
r.scene.append(Cube(V3(-1, 0.50, -4.25), 0.5, grass))
r.scene.append(Cube(V3(-1, 1, -4.25), 0.5, grass))
r.scene.append(Cube(V3(-2, 0.50, -4.25), 0.5, grass))
r.scene.append(Cube(V3(-2, 1, -4.25), 0.5, grass))
#Arbusto
r.scene.append(bush(V3(0, -0.50, -4.5), 0.5, sgreen))
r.envmap = None
r.render()
r.write("Minecraft.bmp")
