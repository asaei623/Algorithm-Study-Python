from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    #### 1. 시작 노드를 큐에 넣고 방문 처리한다.
    
    # 큐 구현을 위해 deque 라이브러리를 사용한다.
    queue = deque([start]) # [start] 리스트로 초기화된 큐를 생성한다.
    # 현재 노드를 방문 처리한다.
    visited[start] = True
    
    #### 4. 큐가 빌 때까지 반복한다.
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력한다.
        v = queue.popleft()
        print(v, end=' ')
        
        #### 2. 아직 방문하지 않은 인접한 원소들을 큐에 삽입한다.
        for i in graph[v]:
            if not visited[i]: #### 3. 처음 방문한 노드라면 큐에 넣고 방문 처리한다.
                queue.append(i)
                visited[i] = True 
    

# 각 노드가 연결된 정보를 표현한다.
# 1번 노드에는 2, 3, 8번 노드가 인접하고, 2번 노드에는 1, 7번 노드가 인접해있다.

graph = [
    [], # 1번 노드 - 배열 1번으로 맞추기 위해서 배열 0번은 넘어간다.
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
    ]

# 각 노드의 방문 표시를 위한 리스트
visited = [False] * 9 # 배열 0번은 넘기므로 9개를 만들어야 한다. 

# BFS 함수 호출
bfs(graph, 1, visited)
print(visited)

# 출력 결과
# 1 2 3 8 7 4 5 6
