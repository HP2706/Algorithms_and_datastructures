def maximum_mystery(A, n):
    """
    Calculates the length of the longest non-decreasing subsequence in array A.
    
    Args:
        A: A list of integers
        n: The length of the list
        
    Returns:
        The length of the longest non-decreasing subsequence
    """
    # Initialize array r
    r = [0] * (n + 1)  # Using 1-indexed array to match pseudocode
    
    # Base case
    r[1] = 1
    
    # Dynamic programming approach
    for j in range(2, n + 1):
        q = 1
        for i in range(1, j):
            # Check if A[j] is not less than A[i] (i.e., A[j] >= A[i])
            if not (A[j-1] < A[i-1]):  # Adjusting for 0-indexed Python arrays
                q = max(q, r[i] + 1)
        r[j] = q
    
    # Return the maximum value in r
    return max(r[1:n+1]), r

print(maximum_mystery([0, 1, 1, 0, 2], 5))
