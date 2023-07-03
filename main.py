import random as rand
import itertools

def IN(elem1, elem2):
    for elem in elem1:
        if elem not in elem2:
            return False
    return True

def numofSame(elem1, elem2):
    return sum([1 for i in range(len(elem1)) if elem1[i] == elem2[i]])

def compare(T1, T2):
    retArr = [0,0]
    for i in range(len(T1)):
        if T1[i] == T2[i]:
            retArr[0] += 1
        elif T1[i] in T2:
            retArr[1] += 1
    return retArr

if __name__ == "__main__":
    colors = ["Red", "White", "Orange", "Grey", "Pink", "Blue", "Green", "Yellow"]
    searchSpace = list(itertools.permutations(colors, 4))
    newSearchSpace = searchSpace
    i = 0
    PRO = rand.choice(newSearchSpace)
    while True:
        if len(newSearchSpace) == 0:
            print("Something is off...")
            break
        guessState = rand.choice(newSearchSpace)
        i += 1
        print(f"Guess state is:{guessState}, with a confidence of {100/len(newSearchSpace)}%")
        guessVal = input()
        guessVal = guessVal.split()
        guessVal = [int(elem) for elem in guessVal]
        if guessVal[0] == 4:
            print(f"I won in {i} turns!")
            break
        else:
            arrofPoss = list(itertools.combinations(guessState, sum(guessVal)))
            if sum(guessVal) == 0:
                arrofPoss = [temp for temp in colors if temp not in guessState]
                arrofPoss = list(itertools.combinations(arrofPoss, 4))
            tempArr1 = []
            for elem1 in newSearchSpace:
                for elem2 in arrofPoss:
                    if IN(elem2, elem1):
                        tempArr1.append(elem1)
                        break
            tempArr2 = []
            for elem in tempArr1:
                if numofSame(guessState, elem) == guessVal[0]:
                    tempArr2.append(elem)
            newSearchSpace = tempArr2