#
# def manipulate_insertion_to_maintain_balanced_in_BST(sorted_arr, arr, arr_length):
#     # for i in range(1, arr_length):
#     #     if len(sorted_arr) <= i:
#     #         arr.extend(sorted_arr)
#     #     else:
#     #         for k in range(round(len(sorted_arr)//i),len(sorted_arr),k):
#     #             arr.append(sorted_arr.pop(k))
#
#     i = 1
#     while i < len(sorted_arr):
#         for k in range(i-1, i):
#             arr1 = sorted_arr[k : len(sorted_arr) // k if k != 0 else len(sorted_arr)]
#             arr.append(arr1.pop(round(len(arr1) // 2)))
#         i += 1
#
#
# arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# arr1 = []
# arr_length = len(arr)
# manipulate_insertion_to_maintain_balanced_in_BST(arr,arr1,arr_length)
# print(arr1)
left_cnt, right_cnt = 0, 0
balanced_arr = []
def sorted_array_to_balanced_bst_order(sorted_array, right_cnt, left_cnt, balanced_arr):
    mid = len(sorted_array) // 2
    # 중간 요소를 먼저 추가
    balanced_arr.append(sorted_array[mid])

    if left_cnt >= right_cnt:# 왼쪽 서브트리의 요소들 추가
        right_cnt += 1
        sorted_array_to_balanced_bst_order(sorted_array[mid+1:],right_cnt,left_cnt,balanced_arr)
    else: # 오른쪽 서브트리의 요소들 추가
        sorted_array_to_balanced_bst_order(sorted_array[:mid],right_cnt,left_cnt,balanced_arr)

    return balanced_arr

# 사용 예시
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
balanced_order = sorted_array_to_balanced_bst_order(sorted_array,left_cnt,right_cnt,balanced_arr)
print(balanced_order)
