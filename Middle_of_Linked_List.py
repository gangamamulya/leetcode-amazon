# Definition for singly-linked list.
import collections
class Node:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object): 
    def __init__(self,nodes=None):
        self.head = None
        
    def middleNode(self, head):
        node = [head]
        while node[-1].next:
            node.append(node[-1].next)
        return node[len(node)//2]
        
