# Diwas Lamsal - st122324
# 2021 - September - 22 -- Data Structures and Algorithms Week 7
# Question: Stack homework to check parenthesis


# ----------------------------------------------------------------------------------------------------- #
# ----------------------------------------- IMPLEMENTING STACK ---------------------------------------- #
# ----------------------------------------------------------------------------------------------------- #


class Stack:
    def __init__(self):
        self.top = -1
        self.slist = []


def stack_empty(S):
    if S.top == -1:
        return True
    else:
        return False


def push(S, x):
    S.top = S.top + 1
    S.slist.append(0)
    S.slist[S.top] = x


def pop(S):
    if stack_empty(S):
        print("Stack already empty")
    else:
        S.top = S.top - 1
        popped = S.slist[S.top + 1]
        del S.slist[-1]
        return popped


def test_stack_push(st, elem):
    print("Before push: \n-----------------------------")
    print("Stack:", st.slist)
    print("Top:", st.top)
    push(st, elem)
    print("After push: \n-----------------------------")
    print("Stack:", st.slist)
    print("Top:", st.top, '\n')


def test_stack_pop(st):
    print("Before pop: \n-----------------------------")
    print("Stack:", st.slist)
    print("Top:", st.top)
    popped = pop(st)
    print("After pop: \n-----------------------------")
    print("Stack:", st.slist)
    print("Top:", st.top, '\n')
    return popped


opening_list = ["(", "{", "["]
closing_list = [")", "}", "]"]


# Some reference taken from
# https://www.youtube.com/watch?v=WTzjTskDFMg&ab_channel=NeetCode
def checkStackValidInput(inputStr):
    st = Stack()
    print("------------------------------\n", inputStr)
    strlist = list(inputStr)
    for elem in strlist:
        if elem in opening_list:
            push(st, elem)
        else:
            if elem not in closing_list:
                print("Invalid characters, must be brackets")
                return
            if st.top == -1:
                print("Invalid! ending bracket encountered before start")
                return
            else:
                popped = pop(st)
                if popped == "(" and elem == ")":
                    flag = True
                elif popped == "{" and elem == "}":
                    flag = True
                elif popped == "[" and elem == "]":
                    flag = True
                else:
                    flag = False
                if not flag:
                    print("Invalid")
                    return

    if st.top == -1:
        print("Valid! The parenthesis test passed, OK")
    else:
        print("Invalid, Not OK")


print("\n------------------------------")
print("------- TESTING STACK --------")
checkStackValidInput("{[[]]{()}}")
checkStackValidInput("[{}")
checkStackValidInput("TESTING")
checkStackValidInput("[({})]{}{}[]({}){()()}")
checkStackValidInput("[(}}{()}}]")


# ----------------------------------------------------------------------------------------------------- #
# ----------------------------------------- IMPLEMENTING QUEUE ---------------------------------------- #
# ----------------------------------------------------------------------------------------------------- #

# ATTEMPT SOLVING THE PROBLEM USING QUEUE

class Queue:
    def __init__(self):
        self.head = -1
        self.tail = -1
        self.qlist = []


# The implementation is not the same as the pseudocode because
# I am using python list instead of array
def enqueue(Q, x):
    Q.qlist.append(x)
    Q.tail = Q.tail + 1
    if Q.head == -1:
        Q.head = 0


# The implementation is not the same as the pseudocode because
# I am using python list instead of array
def dequeue(Q):
    if len(Q.qlist) > 0:
        x = Q.qlist[Q.head]
        del Q.qlist[Q.head]
        Q.tail -= 1  # doing this because we are keeping the head at 0
        if len(Q.qlist) == 0:
            # Setting head to -1 when queue is empty
            Q.head = -1
        return x
    else:
        print("Queue is empty")


def checkQueueValidInput(inputStr):
    q = Queue()
    print("------------------------------\n", inputStr)
    strlist = list(inputStr)
    for elem in strlist:
        if elem in opening_list:
            enqueue(q, elem)
        else:
            if elem not in closing_list:
                print("Invalid characters, must be brackets")
                return
            if q.head == -1:
                print("Invalid! ending bracket encountered before start")
                return
            else:

                # The implementation using queue is not as efficient as
                # with stacks as we have to remove all the elements
                # previously added up to the last element to compare
                # whether the parenthesis match
                temp = []
                while q.tail > 0:
                    temp.append(dequeue(q))
                popped = dequeue(q)
                for t in temp:
                    enqueue(q, t)

                if popped == "(" and elem == ")":
                    flag = True
                elif popped == "{" and elem == "}":
                    flag = True
                elif popped == "[" and elem == "]":
                    flag = True
                else:
                    flag = False
                if not flag:
                    print("Invalid")
                    return

    if q.head == -1:
        print("Valid! The parenthesis test passed, OK")
    else:
        print("Invalid, Not OK")


print("\n------------------------------")
print("------- TESTING QUEUE --------")
checkQueueValidInput("{[[]]{()}}")
checkQueueValidInput("[{}")
checkQueueValidInput("TESTING")
checkQueueValidInput("[({})]{}{}[]({}){()()}")
checkQueueValidInput("[(}}{()}}]")


# ----------------------------------------------------------------------------------------------------- #
# -------------------------------------- IMPLEMENTING NORMAL ARRAY ------------------------------------ #
# ----------------------------------------------------------------------------------------------------- #

def checkArrayValidInput(inputStr):
    arr = [None] * len(inputStr)
    print("------------------------------\n", inputStr)
    strlist = list(inputStr)

    counter = -1
    for elem in strlist:
        if elem in opening_list:
            counter += 1
            arr[counter] = elem
        else:
            if elem not in closing_list:
                print("Invalid characters, must be brackets")
                return
            if arr[counter] is None:
                print("Invalid! ending bracket encountered before start")
                return
            else:
                last = arr[counter]
                if last == "(" and elem == ")":
                    flag = True
                elif last == "{" and elem == "}":
                    flag = True
                elif last == "[" and elem == "]":
                    flag = True
                else:
                    flag = False

                if not flag:
                    print("Invalid")
                    return
                else:
                    arr[counter] = None
                    counter -= 1

    if arr[0] is None:
        print("Valid! The parenthesis test passed, OK")
    else:
        print("Invalid, Not OK")


print("\n------------------------------")
print("------- TESTING ARRAY --------")
checkArrayValidInput("{[[]]{()}}")
checkArrayValidInput("[{}")
checkArrayValidInput("TESTING")
checkArrayValidInput("[({})]{}{}[]({}){()()}")
checkArrayValidInput("[(}}{()}}]")
