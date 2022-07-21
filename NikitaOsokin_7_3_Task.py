mac_adress = ['100         01bb.c580.7000      Gi0/1\n',
              '200         0a4b.c380.7c00      Gi0/2\n',
              '300         a2ab.c5a0.700e      Gi0/3\n',
              '10          0a1b.1c80.7000      Gi0/4\n',
              '500         02b1.3c80.7b00      Gi0/5\n',
              '200         1a4b.c580.7000      Gi0/6\n',
              '300         0a1b.5c80.70f0      Gi0/7\n',
              '10          01ab.c5d0.70d0      Gi0/8\n',
              '1000        0a4b.c380.7d00      Gi0/9\n']
file = open("CAM_table.txt", "w+")
file.writelines(mac_adress)
file.seek(0)
print(file.read())
file.seek(0)
file.close()
