from typing import List

def bubblesort(list: List[str]):

    # defines strict ordering
    def lessthan(i: int, j: int):
        if len(list[i]) == len(list[j]):
           return list[i] < list[j]
        else:
           return len(list[i]) < len(list[j])
           
    bottom: int = 0
    top: int = len(list)-1
    i = 0

    #while not done
    while bottom < top:
        #bubble biggest element up
        while i < top:
            i += 1
            if lessthan(i, i-1):
                #swap
                list[i], list[i-1] = list[i-1], list[i]
        #remove largest element from sort
        top -= 1
        i -= 1

        #bubble smallest element down
        while i > bottom:
            i -= 1
            if lessthan(i+1, i):
                #swap
               list[i], list[i+1] = list[i+1], list[i]
               
        #remove smallest element from sort
        bottom += 1
        i += 1

if __name__ == "__main__":
    sep = '\n'
    filename = "oving11.py"

    strings = []
    with open(filename, 'r') as file:
        for line in file.read().split(sep):
            strings.append(line)

    bubblesort(strings)
    print("\n".join(strings))
