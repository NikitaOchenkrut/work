# Запрашиваем ввод  ip адреса.
ip = input("Введите ip адрес:")

# С помощью split формируем список.
you_ip = ip.split(".")

# Проверяем условия вывода.
if 223 > int(you_ip[0]) > 1:
    print("unicast")
elif 239 > int(you_ip[0]) > 224:
    print("multicast")
elif ip == "255.255.255.255":
    print("local broadcast")
elif ip == "0.0.0.0":
    print("unassigned")
else:
    print("unused")
