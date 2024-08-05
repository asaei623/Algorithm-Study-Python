# 더하고 빼는 모든 경우의 수를 순차적으로 체크하여 다음 경우의 수를 만들어야 하기 때문에 BFS를 사용할 수 있다.
# 각 수를 더하고 뺀 값을 트리로 만든 뒤 가장 마지막 노드들의 값이 target과 일치하는지 확인한다.
# 내가 트리를 만들어 가기 때문에 방문 표시가 필요없다.
def solution(numbers, target):
    # 1. 첫번째 값을 큐에 넣는다. 큐는 모든 경우의 수로 만들어지는 값들을 차례로 저장한다.
    queue = [0]
    
    for n in numbers :
        # 2. n를 더하고 빼는 경우를 큐에 추가한다.
        tmp = []
        # 3. 이전에 queue에 있던 모든 수들에 대해 n에 대한 경우의 수를 기록해야 되기 때문에, for문이 필요하다.
        for q in queue:
            tmp.append(q + n)
            tmp.append(q - n)
        queue = tmp
    
    # 3. queue에 남아있는 수들 중 target과 일치하는 것의 개수를 샌다.
    answer = 0
    for i in queue:
        if i == target:
            answer += 1
    
    return answer

