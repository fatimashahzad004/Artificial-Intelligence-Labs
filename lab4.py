# Question:1 
# Implement Stack using Python. 

class Stack:
   
    def _init_(self):
        self.noe=0
        self.list=[]

    def total_elements(self):
        return self.noe
    
    def is_empty(self):
        return self.noe==0
    
    def peek(self):
        if (self.noe-1 >=0):
            return self.list[self.noe-1]
        else:
            raise ValueError
    
    def push(self,ele):
        self.list+=[ele]    #python lists cannot add values on the indexes which do not exist instead we merge them with new lists
        self.noe+=1

    def pop(self):
        if (self.noe-1 < 0):
            raise ValueError
        else:
            deleted=self.list[self.noe-1]
            self.noe-=1
            return deleted
    

s1=Stack()


s1.push(10)
s1.push(20)
s1.push(30)


try:
    popped=s1.pop()
   
except ValueError :
    print("stack is already empty") 
else:
    print("Popped value is",popped)



try:
    print("Top item",s1.peek())
except ValueError:
    print("Empty stack cannot be peeked")




try:
    popped=s1.pop()
   
except ValueError :
    print("stack is already empty") 
else:
    print("Popped value is",popped)




try:
    popped=s1.pop()
   
except ValueError :
    print("stack is already empty") 
else:
    print("Popped value is",popped)




try:
    popped=s1.pop()
   
except ValueError :
    print("stack is already empty") 
else:
    print("Popped value is",popped)




try:
    print("Top item",s1.peek())
except ValueError:
    print("Empty stack cannot be peeked")



print("Is stack empty?",s1.is_empty())
print("Current size is ",s1.total_elements())




# Q2
# Implement queue using python

#array/list implementation

class Queue:

    def _init_(self):
        self.list=[]
        self.noe=0
        self.front=-1
        self.rear=-1

    def enqueue(self,ele):
        if self.noe==0:
            self.front+=1
            self.rear+=1
            self.list.append(ele)
            self.noe+=1

        else:
            self.front+=1  
            self.list.append(ele)
            self.noe+=1


    def dequeue(self):
        if self.rear==-1 or self.rear > self.front :
            raise ValueError
        else:
            deleted=self.list[self.rear]
            self.rear+=1
            self.noe-=1
            return deleted
        
    def peek(self):
        if self.front==-1 or self.rear > self.front:
            raise ValueError
        else:
            return self.list[self.front]
        

    def isempty(self):
        if self.front==-1 or self.rear > self.front:
            return True
        else:
            return False
        

    def total_elements(self):
        return self.noe
    



q1=Queue()

q1.enqueue(10)

q1.enqueue(20)

q1.enqueue(30)



try:
    dequeued=q1.dequeue()
except ValueError:
    print("queue is already empty. nothing can be dequeued any further")
else:
    print(dequeued ,"is eliminated from our queue")



try:
    dequeued=q1.dequeue()
except ValueError:
    print("queue is already empty. nothing can be dequeued any further")
else:
    print(dequeued ,"is eliminated from our queue")



try:
    dequeued=q1.dequeue()
except ValueError:
    print("queue is already empty. nothing can be dequeued any further")
else:
    print(dequeued ,"is eliminated from our queue")




try:
    front=q1.peek()
except ValueError:
    print("No element in the queue")
else:
    print("the front element in the queue is",front)



print("Is queue empty?",q1.isempty())

print("current size of the queue is ",q1.total_elements())