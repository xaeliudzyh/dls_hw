MOD = 998_244_353

MAX_A = 1000
is_comp = [False]*(MAX_A + 1)
primes = []
for p in range(2, MAX_A + 1):
    if not is_comp[p]:
        primes.append(p)
        for q in range(p*p, MAX_A + 1, p):
            is_comp[q] = True


def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    ans = 1

    for p in primes:
        v, M = [], 0
        for x in a:
            c = 0
            while x % p == 0:
                x //= p
                c += 1
            v.append(c)
            M += c                   

        if M == 0:                   
            continue

        pow_p = [1]*(M+1)
        for k in range(1, M+1):
            pow_p[k] = (pow_p[k-1] * p) % MOD

        cur0 = [0]*(M+1)             
        cur1 = [0]*(M+1)             
        cur1[0] = 1                
        for k in range(1, M+1):       
            cur0[k] = pow_p[k]

        for d in v:
            nxt0 = [0]*(M+1)
            nxt1 = [0]*(M+1)

            if d == 0:            
                for x in range(M+1):
                    if cur0[x]:
                        w = (cur0[x] * pow_p[x]) % MOD
                        nxt0[x] = (nxt0[x] + w) % MOD
                    if cur1[x]:
                        w = (cur1[x] * pow_p[x]) % MOD
                        nxt1[x] = (nxt1[x] + w) % MOD
            else:
                for x in range(M+1):
                    if cur0[x]:
                        up = x + d
                        if up <= M:
                            w = (cur0[x] * pow_p[up]) % MOD
                            nxt0[up] = (nxt0[up] + w) % MOD
                        if x >= d:
                            dn = x - d
                            w = (cur0[x] * pow_p[dn]) % MOD
                            if dn == 0:
                                nxt1[dn] = (nxt1[dn] + w) % MOD
                            else:
                                nxt0[dn] = (nxt0[dn] + w) % MOD

                    if cur1[x]:
                        up = x + d
                        if up <= M:
                            w = (cur1[x] * pow_p[up]) % MOD
                            nxt1[up] = (nxt1[up] + w) % MOD
                        if x >= d:
                            dn = x - d
                            w = (cur1[x] * pow_p[dn]) % MOD
                            nxt1[dn] = (nxt1[dn] + w) % MOD

            cur0, cur1 = nxt0, nxt1  

        contrib = sum(cur1) % MOD
        ans = (ans * contrib) % MOD

    print(ans)


if __name__ == "__main__":
    main()