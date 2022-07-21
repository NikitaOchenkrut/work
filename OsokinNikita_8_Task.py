def func(items):
    result = []
    for i in items:
        result.append(i*100)
    print(result)
    return result
func([1, 7, 8])


from datetime import datetime

import time

def print_current_datetime(ptime=datetime.now()):
    print(f">>> {ptime}")


for i in range(3):
   print("Имитируем долгое выполнение...")
   time.sleep(1)
   print_current_datetime()

import time

for num in range(10):
    print(num, end=' ')
    time.sleep(1)