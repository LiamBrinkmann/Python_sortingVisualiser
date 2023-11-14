import winsound

#Merge Sort implementation
def mergeSort(data, left, right, visual):

    if left < right:
        middle = (left+right)//2

        mergeSort(data, left, middle, visual)
        mergeSort(data, middle+1, right, visual)

        join = middle + 1
        if(data[middle] < data[middle + 1]):
            return
        
        while left <= middle and join <= right:
            visual(data, ['#A79986' if x >= left and x <= right else '#803E2F' for x in range(len(data))])

            if data[left] <= data[join]:
                left += 1
            else: 
                winsound.Beep(((data[join]*2) + left*10 + 100), 10) #making the sound as it is sorted
                visual(data, ['#A79986' if x >= left and x <= right else '#803E2F' for x in range(len(data))])
                temp = data[join]

                i = join
                while i != left:
                    data[i] = data[i-1]
                    visual(data, ['#A79986' if x >= left and x <= right else '#803E2F' for x in range(len(data))])
                    i -= 1
                
                data[left] = temp

                visual(data, ['#A79986' if x >= left and x <= right else '#803E2F' for x in range(len(data))])

                left += 1
                middle += 1
                join += 1