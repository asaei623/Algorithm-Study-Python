# 오답노트 : 리스트를 사용해서 방문 표시를 하지 않고 방문한 원소의 값을 1로 바꾸는 방법을 사용한다.
from collections import deque

def bfs(y, x):
    area = 1 # 1에서 시작해야 한다.
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    # 시작 원소의 값을 방문 표시를 위해 0으로 바꾸고, 큐에 넣는다.
    canvas[y][x] = 0
    queue = deque([(y, x)])
    
    while queue:
        # 큐에서 원소를 빼내고 상하좌우 원소가 1인지 검사
        cury, curx = queue.popleft()
        
        for i in range(4):
            ny = cury + dy[i]
            nx = curx + dx[i]
            # nx, ny가 배열 범위를 넘지 않는지 확인
            if 0 <= ny < col and 0 <= nx < row:
                # 값이 1이면 그림 넓이를 1 추가하고, 큐에 넣는다.
                if canvas[ny][nx] == 1:
                   area += 1
                   queue.append((ny, nx))
                   # 방문 표시를 위해 값을 0으로 바꾼다.
                   canvas[ny][nx] = 0

    return area

# 입력
col, row = map(int, input().split())
# 그림의 정보는 2차원 배열에 입력 받는다.
canvas = [list(map(int, input().split())) for _ in range(col)]

# 변수들
num_of_pntings = 0
max_area = 0

# 값이 1인 원소를 만나면 BFS를 시작하고, 그림의 개수를 1 추가한다.
for i in range(col):
    for j in range(row):
        if canvas[i][j] == 1:
            num_of_pntings += 1
            max_area = max(bfs(i, j), max_area) # 최댓값을 max_area에 저장한다.

# 출력
# 그림의 개수, 가장 넓은 그림의 넓이를 순서대로 출력한다.
print(num_of_pntings)
print(max_area)
