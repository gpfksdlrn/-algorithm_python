def find_max_occurred_alphabet(string):
    alphabet_array = [0] * 26

    for char in string:
        if char.isalpha():
            alphabet_array[ord(char) - 97] += 1

    max_count = 0
    max_index = 0

    for i in range(len(alphabet_array)):
        count = alphabet_array[i]
        if count > max_count:
            max_count = count
            max_index = i

    return chr(max_index + 97)


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))