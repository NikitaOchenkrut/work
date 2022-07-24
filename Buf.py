class buff:

    def fifo(matrix):
        for i in range(len(matrix)):
            matrix.pop(0)
            print(matrix)

        return matrix


size = int(input("Сколько элементов списка потребуется?: "))
matrixOne = []
for i in range(size):
    matrixOne.append(int(input(f"Введите {i} число списка: ")))

buff.fifo(matrix=matrixOne)
