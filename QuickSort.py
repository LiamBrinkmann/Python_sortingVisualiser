import winsound
import time

#splits the data up to then sort it
def partition(data, head, tail, visual):
    border = head
    pivot = data[tail]

    visual(data, Colour(len(data), head, tail, border, border))

    #sorting happens here
    for i in range(head, tail):
        if data[i] < pivot:
            visual(data, Colour(len(data), head, tail, border, i, True))
            data[border], data[i] = data[i], data[border]
            border += 1
        visual(data, Colour(len(data), head, tail, border, i))
        winsound.Beep(((data[i]*2) + i*10 + 100), 10)

    visual(data, Colour(len(data), head, tail, border, tail, True))
    winsound.Beep(((data[i]*2) + i*10 + 100), 10)
    data[border], data[tail] = data[tail], data[border]

    return border

#keeps running the sorting method until it sees head is not below the tail
def quickSort(data, head, tail, visual):
    if head < tail:
        part = partition(data, head, tail, visual)

        quickSort(data, head, part-1, visual)
        quickSort(data, part+1, tail, visual)


#Adds the colours to the bars, so it helps see whats happening a bit better
def Colour(dataLen, head, tail, border, Curr, isSwapping=False):
    ColourArray = []

    for i in range(dataLen):
        if i >= head and i <= tail:
            ColourArray.append('#A79986')
        else: 
            ColourArray.append('#803E2F')
        


    if i == tail:
        ColourArray[i] = '#803E2F'
    elif i == border:
        ColourArray[i] = '#803E2F'
    elif i == Curr:
        ColourArray[i] = '#803E2F'

    if isSwapping:
        if i == border or i == Curr:
            ColourArray[i] = '#803E2F'
    return ColourArray