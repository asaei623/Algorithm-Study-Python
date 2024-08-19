from collections import deque

# 불 BFS
# BFS 응용2:시작점이 여러 개일 때 유형
def bfs_fire(fired):
    # 처음에 불이 나 있는 좌표들을 리스트로 받는다.
    # 모든 좌표를 큐에 동시에 넣고 BFS를 실행한다.
    q = deque([])
    for key in fired.keys():
        q.append(key)

    while(q):
        curx, cury = q.popleft()
        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]

            if 0<=nx<c and 0<=ny<r and maze[nx][ny] in ('J','.'):
                q.append((nx, ny))
                # 해당 좌표에 불이 번지기까지 걸린 시간을 저장한다.
                fired[(nx, ny)] = fired[(curx, cury)] + 1
                # 불이 났음을 표시한다.
                maze[nx][ny] = 'F'

    return
    

# 지훈 BFS
def bfs_jh(start):
    # 지훈이 각 좌표에 가기까지 걸린 시간을 ans에 저장한다.
    ans = {}
    ans[tuple(start)] = 0
    
    q = deque([tuple(start)])

    while(q):
        curx, cury = q.popleft()
        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]
                    
            if 0<=nx<c and 0<=ny<r:
                if (maze[nx][ny] == 'F' and fired[(nx, ny)] > ans[(curx, cury)]+1) or maze[nx][ny] == '.':
                    q.append((nx, ny))
                    # 이동하는데까지 걸린 시간을 저장한다.
                    ans[(nx, ny)] = ans[(curx, cury)]+1
                    # 방문 처리를 위해 좌표값을 J로 바꾼다.
                    maze[nx][ny] = 'J'
            else:
                # 지훈이 미로를 탈출한 경우
                # 지훈이 배열 밖을 벗어나면
                # 그때까지 걸린 시간을 리턴한다.
                return ans[(curx, cury)]+1

    # 지훈이 불에 탔을 경우
    # while문이 끝났는데도 탈출하지 못했다면
    # IMPOSSIBLE을 리턴한다.
    return 'IMPOSSIBLE'

# 입력
r, c = map(int, input().split())
maze = [list(input().strip()) for _ in range(c)]

# 변수들
fired = {}
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
jh = []

# 불 BFS를 먼저 실행해서 각 좌표에 불이 번지기까지의 시간이 기록되게 한다.
# 불이 나 있는 좌표들을 리스트로 만들어 매개변수로 넘긴다.
for i in range(c):
    for j in range(r):
        if maze[i][j] == 'F':
            fired[(i, j)] = 0
        if maze[i][j] == 'J':
            jh = [i, j]
            
bfs_fire(fired)
# 지훈 BFS를 실행해서 지훈이 탈출할 수 있는지 확인한다.
# 지훈의 위치를 매개변수로 넘긴다.
# 출력
print(bfs_jh(jh))
