# BIG O:
# O(m * n)

# EXPLANATION:
# Calculates the length of the longest common subsequence (LCS) between two input strings using dynamic programming. It
# iterates through each character in the strings and updates a 2D array dp to store LCS lengths. The final answer is
# stored in dp[len(text1)][len(text2)].


def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


output = longest_common_subsequence("abcde", "ace")
print(output)
