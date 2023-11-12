import winsound

def bubbleSort(data, visual):
    for i in range(len(data)):
        for j in range(len(data) - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                visual(data, ['#A79986' if x == j or x == j+1 else '#803E2F' for x in range(len(data))])
                winsound.Beep((1000 - data[j]*10 + 37), 25)
    visual(data, ['#803E2F' for x in range(len(data))])