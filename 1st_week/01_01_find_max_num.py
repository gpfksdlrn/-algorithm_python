# def find_max_num(array):
#     a = 0
#     for x in array:
#         if x > a:
#             a = x
#     return a

# max 함수 이용
def find_max_num(array):
    return max(array)


print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))