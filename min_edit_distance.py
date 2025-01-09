def min_edit_distance(source, target):
    m, n = len(source), len(target)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j  # Cost of inserting characters
            elif j == 0:
                dp[i][j] = i  # Cost of deleting characters
            elif source[i - 1] == target[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No cost if characters are the same
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],    # Deletion
                                   dp[i][j - 1],    # Insertion
                                   dp[i - 1][j - 1])  # Substitution

    return dp[m][n]


# Example usage
source1, target1 = "intention", "execution"
source2, target2 = "Piece", "Peace"

print("Edit Distance (intention -> execution):", min_edit_distance(source1, target1))
print("Edit Distance (Piece -> Peace):", min_edit_distance(source2, target2))
