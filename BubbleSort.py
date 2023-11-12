import winsound
import time

def bubbleSort(data, visual):
    for i in range(len(data)):
        winsound.Beep((((i)*2) + i*10 + 100), 10)
        for j in range(len(data) - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                visual(data, ['#A79986' if x == j or x == j+1 else '#803E2F' for x in range(len(data))])
                time.sleep(0.005)
        winsound.Beep((((i)*2) + i*10 + 100), 10)
    visual(data, ['#803E2F' for x in range(len(data))])