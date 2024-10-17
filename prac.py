def make_balance(arr):
    def BFS(start, end, depth, depth_based_arr):
        if start > end:
            return

        mid = (start + end) // 2
        if depth < len(depth_based_arr):             #기존 depth중에 있는 탐색을 하고 있다면, 알맞은 depth에 append.
            depth_based_arr[depth].append(arr[mid])
        else:
            depth_based_arr.append([arr[mid]])       # 기존depth(len(depth_based_arr)) 보다 깊어진 탐색 시작했다면, 새로운 depth를 생성.

        BFS(start, mid - 1, depth + 1, depth_based_arr)  #재귀. start부터 중간까지. depth 1 추가 => 1~7 사이의 중간값이 depth_based_arr의 depth:1 array에 추가됨.
        BFS(mid + 1, end, depth + 1, depth_based_arr)    #재귀. 중간부터 end까지 depth 1 추가 => 8~15 사이의 중간값이 depth_based_arr의 depth:1 array에 추가됨

    depth_based_arr = []                                 #depth_based_arr array 생성
    BFS(0,len(arr) - 1, 0, depth_based_arr)  #초깃값 세팅
    balance_maintain_arr = []                            #저장할 array 생성
    for depth in depth_based_arr:                        #각 depth에 있는 array extend
        balance_maintain_arr.extend(depth)
    return balance_maintain_arr

arr = [x for x in range(1, 16)]
print(make_balance(arr))
