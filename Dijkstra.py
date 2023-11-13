import sys
import time

temp=[]
node=[]
NO_PARENT=-1

INF=int(99999)

def Value_input():
    numbers_list = []

    while True:
        user_input = input()

        if user_input.strip() == ';':
            break

        try:
            # 입력 문자열에서 숫자 부분만 추출하여 리스트에 저장
            numbers = [num for num in user_input.strip('()').split(',')]

            if len(numbers) != 3:
                print("올바른 형태로 입력하세요.")
            else:
                temp.append(numbers[0])
                temp.append(numbers[1])
                numbers[2]=(int)(numbers[2])
                numbers_list.append(numbers)
        except ValueError:
            print("올바른 형태로 입력하세요.")
    
    return numbers_list

def adjacency(edges, n):
    graph=[[0]*n for _ in range(n)]
    
    for u,v,weight in edges:
        graph[u][v]=weight
        graph[v][u]=weight
        
    return graph


def dijkstra(adjacency_matrix,start_vertex):
    n_vertices = len(adjacency_matrix[0])
    shortest_distances = [sys.maxsize] * n_vertices
    added = [False] * n_vertices
    for vertex_index in range(n_vertices):
        shortest_distances[vertex_index] = sys.maxsize
        added[vertex_index] = False
    shortest_distances[start_vertex] = 0
    parents = [-1] * n_vertices
    parents[start_vertex] = NO_PARENT
    
    for i in range(1, n_vertices):
        nearest_vertex = -1
        shortest_distance = sys.maxsize
        for vertex_index in range(n_vertices):
            if not added[vertex_index] and shortest_distances[vertex_index] < shortest_distance:
                nearest_vertex = vertex_index
                shortest_distance = shortest_distances[vertex_index]
        added[nearest_vertex] = True
        for vertex_index in range(n_vertices):
            edge_distance = adjacency_matrix[nearest_vertex][vertex_index]
             
            if edge_distance > 0 and shortest_distance + edge_distance < shortest_distances[vertex_index]:
                parents[vertex_index] = nearest_vertex
                shortest_distances[vertex_index] = shortest_distance + edge_distance
 

        
    print_solution(start_vertex, shortest_distances)
    
def print_solution(start_vertex, distances):
    n_vertices = len(distances)

     
    for vertex_index in range(n_vertices):
            print(distances[vertex_index], "\t",end="")
    print()

            
if __name__ == '__main__':
    start_time=time.time()
    G=Value_input()
    node=list(dict.fromkeys(temp))

    
    Graph=dict((n,i) for i, n in enumerate(node,start=0))
    for i in range(len(G)):
        num=G[i][0]
        G[i][0]=Graph.get(num)
        num=G[i][1]
        G[i][1]=Graph.get(num)


    adma=adjacency(G,10)
    
    print("\t",end="")
    for i in node:
        print(i,"\t",end="")
    print()
    for i in range(len(node)):
        print(node[i],"\t",end="")
        
        dijkstra(adma,i)
    
    end_time = time.time()
    execution_time = end_time - start_time
    print(execution_time)

