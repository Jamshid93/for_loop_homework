def main(k,n):
    """
    Repeat the number k n times and return to the list view.
    Args:
        k: int
        n: int
    Returns:
        list: return  answer
    """
    s=[]
    for i in range(n):
        i=k
        s.append(i)

    return s
print(main(-1,4))