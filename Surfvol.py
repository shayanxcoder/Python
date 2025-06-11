print ("Hello I am a calculator who calculates the surface area and volume for u bcuz the rencho told me to to")

print("Select a shape:")
choice = int(input("Press 1 for cylinder, Press 2 for cuboid, Press 3 for cube"))
if choice == 1:
    Radius = int(input("Enter the Radius:"))
    Height = int(input("Enter the Height:"))
    def cylinder(R,H):
         int(volume = 3.14*R*R*H)
         int(Larea = 2*3.14*R*H)
         int(Tarea = 2*3.14*R*(R+H))
         return print(f"volume = {volume}, Lateral surface area = {Larea}, Total surface area = {Tarea}")

    cylinder(Radius, Height)

if choice == 2:
    Legnth = int(input("Enter the Legnth:"))
    Width = int(input("Enter the Width:"))
    Height = int(input("Enter the Height"))
    def cuboid(l,b,h):
        volume = l*b*h
        area1 = 2*l*b
        area2 = 2*b*h
        area3 = 2*h*l
        area = area1 + area2 + area3
        return print(area,volume)

    cuboid(Legnth, Width, Height)

if choice == 3:
    side = int(input("Enter the side"))
    def cube(s):
        volume = s*s*s
        area = 6*s*s
        larea = 4*s*s
        return print(volume,area)
    cube(side)