from collections.abc import Iterable, Iterator
import math
import heapq

def log2(x):
    return math.log2(x)

class Heap:

    def __init__(self,items):
        self.items=items
        self.size=len(items)
    
    def parent(self,id):
        if id==0:
            return None
        return (id-1)//2

    def lchild(self,id):
        if(2*id+1<self.size):
            return 2*id+1
        return None

    def rchild(self,id):
        if(2*id+2<self.size):
            return 2*id+2
        return None
    
    def max(self):
        if(self.size==0):
            return None
        return self.items[0]
    
    def min(self):
        if(self.size==0):
            return None
        return self.items[2**int(log2(self.size))-1]

    
    def fix(self,i):
        error=i
        lchild = self.lchild(i)
        rchild = self.rchild(i)
        if rchild is not None and self.items[rchild] > self.items[error]:
            error=rchild
        if lchild is not None and self.items[lchild] > self.items[error]:
            error=lchild
        if error==i:
            return
        temp=self.items[error]
        self.items[error]=self.items[i]
        self.items[i]=temp
        self.fix(error)

    def makeMax(self):
        if(self.size==1 or self.size==0):
            return
        for i in range(self.size//2-1,-1,-1):
            self.fix(i)
    
    def insert(self,x):
        self.items.append[x]
        self.size +=1
        check=(self.size-1)//2
        while check>=0:
            self.fix(check)
            check=(check-1)//2
    
    def __repr__(self):
        return str(self.items)


def BinarySearch(l,x):
    left=0
    right=len(l)-1
    mid=0

    while left <= right:
        mid=(left+right)//2
        if l[mid]<x:
            left=mid+1
        elif l[mid]>x:
            right=mid-1
        else:
            return mid
    return -1


class Stack:

    def __init__(self):
        self.items=[]
    
    def push(self,k):
        self.items.append(k)
    
    def pop(self):
        if(len(self.stack)==0):
            return Exception
        return self.stack.pop()

    def find(self,i):
        if(len(self.stack)<i):
            return Exception
        return self.stack[i-1]
    
    def peek(self):
        if (len(self.stack)==0):
            return Exception
        return self.stack[0]

class Node:
    def __init__(self,head, next):
        self.head=head
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
        self.size=0
    
    def add(self,x):
        self.head = Node(x,self.head)
        self.size+=1
    
    def remove(self):
        if self.head is None:
            return None
        ans=self.head.head
        self.head=self.head.next
        self.size=self.size-1
        return ans
    def __len__(self):
        return self.size

class Leaf:

    def __init__(self,x):
        self.root=x
        self.left=None
        self.right=None
def depth(leaf):
    if(leaf.left is None):
        a=0
    else:
        a=depth(leaf.left)
    if(leaf.right is None):
        b=0
    else:
        b=depth(leaf.right)
    return 1+max(a,b)

def mergesort(c):
    if len(c)>1:
        mid=len(c)//2
        left = c[:mid]
        right = c[mid:]
        mergesort(left)
        mergesort(right)
        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                c[k] = left[i]
                i += 1
            else:
                d[k] = right[j]
                j += 1
            k += 1
 
        while i < len(lefr):
            c[k] = left[i]
            i += 1
            k += 1
 
        while j < len(R):
            c[k] = right[j]
            j += 1
            k += 1




            


