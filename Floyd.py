import time
_inf = 99999
temp=[]
node=[]

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

def floyd_warshall(graph,nodes):
    n = len(graph)
    for k in range(n): 
        for i in range(n):
           for j in range(n):
               graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    print_solution(graph,nodes)

def print_solution(graph,nodes):
    n_vertices = len(graph)

     
    for vertex_index in range(n_vertices):
        print(nodes[vertex_index],"\t",end="")
        for value in graph[vertex_index]:
            print(value, "\t", end="")
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
    

    for i in range(len(adma)):
        n=len(adma[i])
        for j in range(n):
            if i!=j and adma[i][j]==0:
                adma[i][j]=_inf
    
    print("\t",end="")
    for i in node:
        print(i,"\t",end="")
    print()
    floyd_warshall(adma,node)
    
    end_time=time.time()
    
    excution_time=end_time
    print(excution_time)