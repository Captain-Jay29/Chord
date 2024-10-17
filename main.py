import sys
from utility import *


func_map = {}



# To load the test case file and read its content
with open(sys.argv[-1], 'r') as f:
    file = f.read()


inputs = file.split('\n')


for i in inputs:
    
    cmd = i.split(" ")[0]
    args = i.split(" ")[1:]


    
    if cmd == "addNode":
        func_map[args[0]] = addNode(args[1])



    
    elif cmd == "join":
        if args[1] != 'None':

            newNode = func_map[args[0]]
            existingNode = func_map[args[1]]
            joinNodes(newNode, existingNode)

   

    # Finger Table
    elif cmd == "ppft":
        prettyPrintFT(func_map[args[0]])

    

    
    elif cmd == "insert":

        node = func_map[args[0]]
        key = args[1]
        value = None

        if len(args)==3:
            value = args[2]

        insertKeyValues(node, key, value)

    

    # Node
    elif cmd == "ppn":
        prettyPrintNode(func_map[args[0]])

    

    
    elif cmd == "findall":
        findall(func_map[args[0]])

    

    
    elif cmd == "leave":
        leaveNode(func_map[args[0]])
    
    

    
    elif cmd == "find":

        node = func_map[args[0]]
        find(node, args[1])

    

    # remove_function
    elif cmd == "remove":

        node = node = func_map[args[0]]
        remove(node, args[1])



exit()