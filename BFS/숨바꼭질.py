from collections import deque

def bfs(n, k):
    q = deque([n])
    ans = {n:0} # n의 위치까지 걸린 시간 0초

    while(q):
        curx = q.popleft()

        if curx == k:
            return ans[curx]
            
        for nx in (curx - 1, curx + 1, curx * 2): # 곱셈이 있으므로 기존 방식(curx + dx[i])은 쓸 수 없다.
            if nx not in ans and 0 <= nx <= 100000: # 방문 여부 확인 and 범위 확인
                ans[nx] = ans[curx] + 1
                q.append(nx)
    
    

# 입력
n, k = map(int, input().split())

# 출력
print(bfs(n, k))
