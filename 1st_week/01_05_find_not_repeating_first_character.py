def find_not_repeating_first_character(string):
    # 각 알파벳의 빈도를 저장
    alphabet_occurrence_arr = {}

    for char in string:
        if char in alphabet_occurrence_arr:
            alphabet_occurrence_arr[char] += 1
        else:
            alphabet_occurrence_arr[char] = 1

    for char in string:
        if alphabet_occurrence_arr[char] == 1:
            return char
    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))