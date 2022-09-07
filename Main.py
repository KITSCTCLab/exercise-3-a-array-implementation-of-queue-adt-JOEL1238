class Solution:
# Write your code here
def _init_(self, size):
self.stack = []
self.queue = []
self.size = size
self.top = -1
self.rear = -1
self.front = -1
def is_stack_empty(self):
return self.top == -1
def is_queue_empty(self):
return self.front == -1 or self.front &gt; self.rear
def is_stack_full(self):
return self.top == self.size - 1
def is_queue_full(self):
return self.rear == self.size - 1
def push_character(self, character):
if not self.is_stack_full():
self.stack.append(character)
self.top += 1
def enqueue_character(self, character):
if not self.is_queue_full():
if self.front == -1:
self.front = 0
self.rear += 1
self.queue.append(character)
def pop_character(self):
if not self.is_stack_empty():
self.top -= 1
return self.stack.pop(self.top + 1)
def dequeue_character(self):
if not self.is_queue_empty():
self.front += 1
return self.queue[self.front - 1]
# read the string text
text = input()
# find the length of text
length_of_text = len(text)
