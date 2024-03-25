def brute_force_string_match(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:  # Nếu tất cả các ký tự trong pattern khớp với text
            return i  # Trả về vị trí xuất hiện đầu tiên của pattern trong text
    return -1  # Trả về -1 nếu không tìm thấy pattern trong text

# Test
text = "ababcabcacbab"
pattern = "abcac"
print(brute_force_string_match(text, pattern))  