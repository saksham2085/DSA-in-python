class node:
    def __init__(self,info,next=None):
        self.data=info
        self.next=next
class singlylinkedlist:
    def __init__(self,head=None):
        self.head=head

    def insert_at_end(self,value):
        temp=node(value)
        if (self.head!=None):
            t1=self.head
            while(t1.next!=None):
                t1=t1.next
            t1.next=temp  
        else:
            self.head=temp
    def insert_at_begin(self,value):
        temp=node(value)
        temp.next=self.head
        self.head=temp

    def insertinmiddle(self,value,x):
        temp=node(value)
        t1=self.head
        while(t1.next !=None):
            if(t1.data==x):
                temp.next=t1.next
                t1.next=temp
            t1=t1.next    
                
    def delete_value(self,value):
        t1=self.head
        prev = t1
        if(t1.data==value):
            self.head=t1.next
            return
        while(t1.next !=None):
            if(t1.data==value):
                prev.next=t1.next
                break
            else:
                prev=t1
            t1=t1.next    
        if(t1.data==value):
            prev.next=None    
    def printll(self):
        t1=self.head
        while(t1.next !=None):
            print(t1.data,end=" ")
            t1=t1.next    
        print(t1.data)
obj=singlylinkedlist()            
obj.insert_at_end(10)
obj.insert_at_end(20)
obj.insert_at_end(30)
obj.insert_at_begin(5)
obj.insertinmiddle(40,20)
obj.delete_value(20)
obj.printll()         