from room import Room

r1 = Room(6, 3, 2.7) 
#print(r1.square) #общая  площадь квартиры
r1.addWD(1, 1)  #площадь окна
r1.addWD(1, 1) #площадь окна
r1.addWD(1, 2) #площадь двери
print(r1.workSurface()) 
print(r1.wallpapers(2, 3))