s = int(input("ระยะทาง: "))
if s<1:
    s=1
print(s, "กิโลเมตร")
t = int(input("เวลา(ชั่วโมง): "))
print(t, "ชั่วโมง")
v = s//t
print("Velocity:", v,"กิโลเมตร/ชั่วโมง")
