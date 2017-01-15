def get_nth_term(t1, t2, N):
    # t(i+2) = t(i) + (t(i+1))^2
    # t3 = t1 + t2 ** 2
    for i in xrange(3, N+1):
        t3 = t1 + t2 ** 2
        t1 = t2
        t2 = t3

    return t3
