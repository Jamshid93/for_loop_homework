def main(n):
    """
    Return numbers from zero to n in a list view.
    Args:
        n: int
    Returns:
        list: return  answer
    """
    s=[]
    for i in range(0,n,1):
        s.append(i)

    return s 
print(main(5))


    