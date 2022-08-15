room_t = int(input("Введите температуру в комнате"))
wish_t = int(input("Введите желаемую температуру"))
wet_level = int(input("Введите влажность"))
if room_t > wish_t and wet_level <= 80:
    print("on")
else:
    print("off")