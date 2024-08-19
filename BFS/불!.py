from collections import deque

# 불 BFS; 응용2:시작점이 여러 개일 때 유형
def bfs_fire(fired):
    q = deque(fired.keys()) #.keys() 메서드는 키 값 리스트를 반환한다.
    
    while(q):
        curx, cury = q.popleft()
        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]

            if 0 <= nx < r and 0 <= ny < c and maze[nx][ny] in ('J','.'):
                if (nx, ny) not in fired: # 방문 여부 확인
                    q.append((nx, ny))
                    fired[(nx, ny)] = fired[(curx, cury)] + 1
    return
    

# 지훈 BFS; 기본 유형
def bfs_jh(start):
    ans = {}  # 지훈이 각 좌표에 가기까지 걸린 시간을 저장
    ans[tuple(start)] = 0
    
    q = deque([tuple(start)])

    while(q):
        curx, cury = q.popleft()
        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]
                    
            if 0 <= nx < r and 0 <= ny < c:
                if (maze[nx][ny] != '#' and (nx, ny) not in fired) or ((nx, ny) in fired and fired[(nx, ny)] > ans[(curx, cury)]+1):
                    if (nx, ny) not in ans: # 방문 여부 확인
                        q.append((nx, ny))
                        ans[(nx, ny)] = ans[(curx, cury)]+1
            else:
                # 지훈이 미로를 탈출한 경우
                return ans[(curx, cury)]+1

    # 지훈이 미로를 탈출하지 못했을 경우
    return 'IMPOSSIBLE'

# 입력
r, c = map(int, input().split()) # r = 미로의 세로 길이
maze = [list(input().strip()) for _ in range(r)]

# 변수들
fired = {}
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
jh = []

# 불이 난 곳들을 fired에, 지훈의 위치를 jh에 저장한다.
for i in range(r):
    for j in range(c):
        if maze[i][j] == 'F':
            fired[(i, j)] = 0
        if maze[i][j] == 'J':
            jh = [i, j]

# 미로의 각 좌표에 불이 번지기까지의 시간을 저장한다.            
bfs_fire(fired)

# 출력
print(bfs_jh(jh))
