for n in range(1, 40):
    for k in range(1, 40):
        for m in range(1, 40):
            if 28 * n + 30 * k + 31 * m == 365:
                print('n =', n, 'k =', k, 'm =', m)