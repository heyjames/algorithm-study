length, depth = map(int, input().split())
visit = [False]length
result = [0]depth

def dfs(length, depth, cursor):
    global visit, result
    
    if cursor == depth:
        for a in result:
            print(a,end=' ')
        print()
        return

    for i in range(length):
        if visit[i] == False:
            visit[i] = True
            result[cursor] = i+1
            dfs(length, depth, cursor + 1)
            visit[i] = False
    return

dfs(length, depth, 0)