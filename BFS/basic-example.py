# class collections.deque([iterable[, maxlen]])
## iterable을 지정하지 않을 경우 빈 deque를 반환한다.
## append(오른쪽 추가), copy(얉은 복사), popleft(왼쪽에서 제거 후 반환), reverse(순서를 뒤집고 None을 반환)
# iterable이란 list str, tuple, dict, file objects 처럼 for문을 순회할 수 있는 객체
# collections 모듈은 dict, list, set, tuple에 대한 대안을 제공한다.
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    #### 1. 시작 노드를 큐에 넣고 방문 처리한다.
    
    # 큐 구현을 위해 deque 라이브러리를 사용한다.
    queue = deque([start]) # [start] 리스트로 초기화된 큐를 생성한다.

    # ---
    # 직접 큐 구현하는 법
    Class Queue:
        def __init__(self):
            self.front = None
            self.rear = None
        def enqueue(self, data):
            # 데이터 삽입
            # 데이터가 아무것도 없을 경우, front에 data 노드를 단다.
            if self.front is None:
                self.front = self.rear = Node(data)
            else:
                # 데이터가 있을 경우, data 노드를 새로 만든 뒤, rear.next와 rear가 추가된 노드를 가리키게 한다.
                node = Node(data)
                self.rear.next = node
                self.rear = node
        def dequeue(self):
            # 데이터 삭제
            # 데이터가 아무것도 없을 경우 None을 반환한다.
            if self.front is None:
                return None
            # 현재 노드를 front로 놓는다.
            node = self.front
            # 데이터가 단 하나 있을 경우 큐를 None으로 비운다.
            if self.front == self.rear:
                self.front = self.rear = None
            # 데이터가 여러 개 있을 경우 현재 노드를 next(이전 노드)로 놓는다.
            else:
                self.front = self.front.next
            # 삭제된 노드의 데이터를 리턴한다.
            return node.data
    # ---

    
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
