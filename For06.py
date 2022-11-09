def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    s=[]
    for i in range(A,B):
        s.append(i)

    return sum(s)
print(main(3,6))