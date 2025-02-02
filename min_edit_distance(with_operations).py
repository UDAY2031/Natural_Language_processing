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

    # Backtracking to count operations
    i, j = m, n
    i_count = d_count = s_count = 0  # i = insertions, d = deletions, s = substitutions

    while i > 0 or j > 0:
        if i > 0 and j > 0 and source[i - 1] == target[j - 1]:
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            d_count += 1  # Deletion
            i -= 1
        elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
            i_count += 1  # Insertion
            j -= 1
        else:
            s_count += 1  # Substitution
            i -= 1
            j -= 1

    total_operations = i_count + d_count + s_count

    return dp[m][n], i_count, d_count, s_count, total_operations


# Example usage
source1, target1 = "intention", "execution"
source2, target2 = "Piece", "Peace"

distance1, i1, d1, s1, total1 = min_edit_distance(source1, target1)
distance2, i2, d2, s2, total2 = min_edit_distance(source2, target2)

print("Minimum edit distance:", distance1)
print("Number of insertions (i):", i1)
print("Number of deletions (d):", d1)
print("Number of substitutions (s):", s1)
print("Total number of operations:", total1)

print("\nMinimum edit distance:", distance2)
print("Number of insertions (i):", i2)
print("Number of deletions (d):", d2)
print("Number of substitutions (s):", s2)
print("Total number of operations:", total2)
