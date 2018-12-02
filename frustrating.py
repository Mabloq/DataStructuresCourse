# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def find(self, key, root):
        if root.key == key:
            return root
        elif root.key > key:
            if root.left != None:
                return self.find(key, root.left)
            return root
        elif root.key < key:
            return self.find(key, root.right)

    def insert(self, node, root):
        # if root is none then we can return the node as the root
        if root is None:
            return node
        elif node.key == root.key:
            return root
        # otherwise continue looking for a root that is None in the left or right three
        elif node.key < root.key:
            root.left = self.insert(node, root.left)
        else:
            root.right = self.insert(node, root.right)

        # return root and any of its modifications to its children
        return root


class TreeOrders:

    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        self.root = None
        self.tree = BST()

        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []
        # Set current to root of binary tree
        current = 0
        stack = []  # initialze stack
        done = 0

        # [0,
        while not done:
            if current is not -1:
                stack.append(current)
                current = self.left[current]
            else:
                if (len(stack) > 0):
                    current = stack.pop()
                    self.result.append(self.key[current])
                    current = self.right[current]
                else:
                    done = 1

        return self.result

    def preOrder(self):
        self.result = []
        current = 0
        stack = []
        stack.append(current)

        while(len(stack) > 0):
            current = stack.pop()
            self.result.append(self.key[current])

            if self.right[current] is not -1:
                stack.append(self.right[current])
            if self.left[current] is not -1:
                stack.append(self.left[current])

        return self.result

    def peek(self, stack):
        if len(stack) > 0:
            return stack[-1]
        return None

    def postOrder(self):
        self.result = []
        current = 0

        stack = []
        while True:
            while current != -1:
                if self.right[current] is not -1:
                    stack.append(self.right[current])
                stack.append(current)
                current = self.left[current]

            current = stack.pop()

            if self.right[current] is not -1 and self.peek(stack) == self.right[current]:
                stack.pop()
                stack.append(current)
                current = self.right[current]
            else:
                self.result.append(self.key[current])
                # right after append skip the inner while loop to get the next item in the stack
                current = -1
            if len(stack) <= 0:
                break


        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
