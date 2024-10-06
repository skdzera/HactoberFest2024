def merge3_array(A, B, C):
    index1, index2, index3 = 0, 0, 0
    previous = float('-inf')
    results = []
    
    while index1 < len(A) or index2 < len(B) or index3 < len(C):
        a = A[index1] if index1 < len(A) else float('inf')
        b = B[index2] if index2 < len(B) else float('inf')
        c = C[index3] if index3 < len(C) else float('inf')
        
        min_value = min(a, b, c)
        
        if min_value > previous:
            results.append(min_value)
            previous = min_value
        
        if index1 < len(A) and A[index1] == min_value:
            index1 += 1
        if index2 < len(B) and B[index2] == min_value:
            index2 += 1
        if index3 < len(C) and C[index3] == min_value:
            index3 += 1
            
    return results
