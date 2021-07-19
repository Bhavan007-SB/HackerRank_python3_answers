N = int(input())
    lst = []
    for i in range(0, N):
        elements = input()
        elements_lst = elements.strip().split(" ")
        cmd = elements_lst[0]
        if cmd == "print":
            print(lst)
        elif cmd == "sort":
            lst.sort()
        elif cmd == "reverse":
            lst.reverse()
        elif cmd == "pop":
            lst.pop()
        elif cmd == "count":
            val = int(elements_lst[1])
            lst.count(val)
        elif cmd == "index":
            val = int(elements_lst[1])
            lst.index(val)
        elif cmd == "remove":
            val = int(elements_lst[1])
            lst.remove(val)
        elif cmd == "append":
            val = int(elements_lst[1])
            lst.append(val)
        elif cmd == "insert":
            pos = int(elements_lst[1])
            val = int(elements_lst[2])
            lst.insert(pos, val
