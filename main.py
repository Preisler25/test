"""
stack = 

Írjunk egy osztályt ami a stack reprezentálja
van egy osztály ami egy stack osztály
a stackban lesz egy adat tag ami megmondja stack hossza
push berak
peek betekintés
pop kiveszi a legelső + retrun
konstruktor 

    nincs para méter
    csak genTömb

push metod 
    size of tömb * 2
    if only 40% fill /2
    
    

"""

class Stack:
    def __init__(self):
        self.array = [None]

    def getLen(self):
        return len(self.array)

    def push(self, data):
        for i in range(self.getLen()):
            self.array.append(None)
            
        i = self.findFirstNoneIndex()
        self.array[i] = data

        if (i+1)/self.getLen() < 0.4:
            self.array = self.array[0:int(self.getLen()/2)]

    def peek(self):
        i = self.findFirstNoneIndex()
        print(self.array[i-1])

    def pop(self):
        i = self.findFirstNoneIndex()
        temp = self.array[i-1]
        self.array[i-1] = None
        return temp

    def findFirstNoneIndex(self):
        for i in range(self.getLen()-1, -1, -1):
            if self.array[i] != None:
                return i+1
        return 0


def main():
    stack = Stack()
    stack.push(1)
    stack.peek()
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.peek()

main()